# myproject/urls.py
# This file defines the URL routing for your entire Django project.

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('problem_solver_app.urls')), # Include URLs from your app
]

