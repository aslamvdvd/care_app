# problem_solver_app/urls.py
# This file defines the URL routing specific to your problem_solver_app.

from django.urls import path
from . import views

urlpatterns = [
    path('', views.problem_solver_view, name='home'), # Maps the root URL to your view
]