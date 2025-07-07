# problem_solver_app/views.py
# This file contains the logic for your web application, including LLM interaction.

import json
import requests
from django.shortcuts import render
from django.http import JsonResponse
import os # To potentially load API key from environment variables

def problem_solver_view(request):
    """
    Handles the main view for the problem solver application.
    - Displays the input form on GET requests.
    - Processes form submission, calls the LLM, and displays the solution on POST requests.
    """
    solution_path = None
    error_message = None
    name = ''
    gender = ''
    hobbies = []
    custom_hobby = ''
    problem = ''

    if request.method == 'POST':
        # Retrieve form data from the POST request
        name = request.POST.get('name', '').strip()
        gender = request.POST.get('gender', '').strip()
        hobbies = request.POST.getlist('hobbies') # getlist for multiple checkboxes
        custom_hobby = request.POST.get('customHobby', '').strip()
        problem = request.POST.get('problem', '').strip()

        # Input validation
        if not name:
            error_message = 'Please enter your name.'
        elif not gender:
            error_message = 'Please enter your gender.'
        elif not (hobbies or custom_hobby):
            error_message = 'Please select at least one hobby or enter a custom hobby.'
        elif not problem:
            error_message = 'Please describe the problem you are facing.'
        else:
            try:
                # Combine selected and custom hobbies
                all_hobbies = list(hobbies)
                if custom_hobby:
                    all_hobbies.append(custom_hobby)
                hobbies_string = ', '.join(all_hobbies) if all_hobbies else 'None specified'

                # Construct the prompt for the LLM
                prompt = (
                    f"Hello, my name is {name}. My gender is {gender}. My hobbies include {hobbies_string}. "
                    f"I am currently facing the following problem: \"{problem}\". "
                    f"Please provide a detailed, step-by-step actionable path to help me get out of this problem. "
                    f"Focus on practical and encouraging steps."
                )

                # Prepare the payload for the Gemini API call
                chat_history = []
                chat_history.append({"role": "user", "parts": [{"text": prompt}]})
                payload = {"contents": chat_history}

                # In a real application, load the API key from environment variables for security:
                # API_KEY = os.environ.get("GEMINI_API_KEY", "")
                # For this example, we'll keep it as an empty string as per Canvas instructions.
                api_key = "AIzaSyBCoCSecgySGV1BR81p-giODeCq4YGe6do" # Canvas will automatically provide the API key in runtime

                api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

                # Make the API call using requests
                response = requests.post(api_url, headers={'Content-Type': 'application/json'}, json=payload)
                response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)

                result = response.json()

                # Process the LLM's response
                if result.get('candidates') and len(result['candidates']) > 0 and \
                   result['candidates'][0].get('content') and \
                   result['candidates'][0]['content'].get('parts') and \
                   len(result['candidates'][0]['content']['parts']) > 0:
                    solution_path = result['candidates'][0]['content']['parts'][0]['text']
                else:
                    error_message = 'Failed to generate a solution. LLM response structure unexpected.'
                    print(f"LLM response structure unexpected: {result}") # Log for debugging

            except requests.exceptions.RequestException as e:
                error_message = f'Network error or API issue: {e}'
                print(f"Error calling LLM API: {e}")
            except Exception as e:
                error_message = f'An unexpected error occurred: {e}'
                print(f"Unexpected error: {e}")

    # Prepare context to pass to the template
    context = {
        'name': name,
        'hobbies': hobbies,
        'custom_hobby': custom_hobby,
        'problem': problem,
        'solution_path': solution_path,
        'error_message': error_message,
        'common_hobbies': [
            'Reading', 'Sports', 'Music', 'Art', 'Cooking', 'Gaming', 'Hiking',
            'Photography', 'Writing', 'Gardening', 'Travel', 'Coding'
        ],
    }
    return render(request, 'problem_solver_app/index.html', context)