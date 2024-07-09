Django Chatbot
A simple Django-based chatbot application with user authentication, chat history functionality, and a mobile-responsive design.

Features
User authentication (login and logout)
Persistent chat history for each user
Mobile-responsive design
Welcome message on chat load
Prerequisites
Python 3.8+
Django 3.0+
An OpenAI API key
Installation
Clone the repository

bash
Copy code
git clone https://github.com/yourusername/django_chatbot.git
cd django_chatbot
Create and activate a virtual environment

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages

bash
Copy code
pip install -r requirements.txt
Set up environment variables

Create a .env file in the project root directory and add your OpenAI API key:

plaintext
Copy code
OPENAI_API_KEY=your_openai_api_key
Apply database migrations

bash
Copy code
python manage.py migrate
Create a superuser

bash
Copy code
python manage.py createsuperuser
Run the development server

bash
Copy code
python manage.py runserver
Usage
Open your web browser and go to http://127.0.0.1:8000/login/.
Log in using the superuser credentials you created.
You will be redirected to the chatbot page where you can start interacting with the chatbot.

Project Structure
chatbot/: Contains the Django app for the chatbot.
migrations/: Database migrations for the chatbot app.
templates/: HTML templates for the chatbot app.
chatbot/: Contains the chatbot.html template.
registration/: Contains the login.html template for user authentication.
admin.py: Admin configuration for the chatbot app.
apps.py: App configuration for the chatbot app.
models.py: Database models for the chatbot app.
views.py: Views for the chatbot app.
urls.py: URL configuration for the chatbot app.
django_chatbot/: Project settings and configurations.
settings.py: Project settings.
urls.py: Project URL configuration.
wsgi.py: WSGI configuration.
venv/: Virtual environment directory.
requirements.txt: List of required Python packages.
.env: Environment variables for the project.
