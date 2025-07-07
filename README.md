# Personalized Problem Solver

Hi! My name is Mohammad Aslam, and this is my Django web application called **Personalized Problem Solver**. I built this project to help users get actionable, step-by-step solutions to their personal problems using the power of Large Language Models (LLMs).

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Tech Stack](#tech-stack)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contact](#contact)
- [License](#license)

## Project Overview
This web app collects some basic information about the user (name, gender, hobbies, and a description of a problem) and then uses the Google Gemini LLM API to generate a personalized, practical solution path. The goal is to provide encouragement and actionable steps for anyone facing a challenge.

## Features
- Clean, modern UI with Tailwind CSS
- Collects user info: name, gender, hobbies (multiple or custom), and problem description
- Validates user input and provides helpful error messages
- Integrates with Google Gemini LLM API to generate solutions
- Displays the solution in a readable, styled format
- Handles API/network errors gracefully
- Keeps form fields populated after submission for a smooth user experience

## How It Works
1. The user fills out a form with their details and problem.
2. On submission, the app validates the input.
3. If valid, it sends a prompt to the Gemini LLM API.
4. The API returns a step-by-step solution, which is displayed to the user.
5. If there are errors (validation or API), the app shows clear feedback.

## Tech Stack
- **Backend:** Django 5.2.4 (Python)
- **Frontend:** HTML, Tailwind CSS
- **API:** Google Gemini LLM (via HTTP requests)
- **Other:** Custom Django template filters for formatting

## Setup & Installation
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd care_app
   ```
2. **Create a virtual environment:**
   ```bash
   python3 -m venv app_venv
   source app_venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
6. **Open your browser and visit:**
   ```
   http://127.0.0.1:8000/
   ```

## Project Structure
```
care_app/
├── app_venv/                # Virtual environment (excluded from git)
├── care_app/                # Django project settings
├── problem_solver_app/      # Main Django app
│   ├── templates/
│   │   └── problem_solver_app/
│   │       └── index.html   # Main HTML template
│   ├── templatetags/
│   │   └── custom_filters.py# Custom template filters
│   ├── views.py             # Main view logic
│   ├── urls.py              # App URL config
│   └── ...
├── db.sqlite3               # SQLite database
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
└── .gitignore               # Git ignore file
```

## Contact
- **Name:** Mohammad Aslam
- **Email:** aslammohammad336@gmail.com
- **Location:** Bihar, India

## License
See [LICENSE](LICENSE) for details. This project is proprietary and may not be used, copied, or distributed without my explicit permission.
