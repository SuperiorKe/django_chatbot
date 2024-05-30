from django.urls import path
from .views import chatbot

urlpatterns = [
    path('', chatbot, name='home'),  # Ensure this is defined
    # Add other URL patterns as needed
]
