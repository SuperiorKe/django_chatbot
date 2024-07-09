
# Django Chatbot

A simple Django-based chatbot application with user authentication, chat history functionality, and a mobile-responsive design.

## Features

- User authentication (login and logout)
- Persistent chat history for each user
- Mobile-responsive design
- Welcome message on chat load

## Prerequisites

- Python 3.8+
- Django 3.0+
- An OpenAI API key

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/django_chatbot.git
   cd django_chatbot
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root directory and add your OpenAI API key:

   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   ```

5. **Apply database migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**

   ```bash
   python manage.py runserver
   ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:8000/login/`.
2. Log in using the superuser credentials you created.
3. You will be redirected to the chatbot page where you can start interacting with the chatbot.

## Project Structure

- **chatbot/**: Contains the Django app for the chatbot.
  - **migrations/**: Database migrations for the chatbot app.
  - **templates/**: HTML templates for the chatbot app.
    - **chatbot/**: Contains the `chatbot.html` template.
    - **registration/**: Contains the `login.html` template for user authentication.
  - **admin.py**: Admin configuration for the chatbot app.
  - **apps.py**: App configuration for the chatbot app.
  - **models.py**: Database models for the chatbot app.
  - **views.py**: Views for the chatbot app.
  - **urls.py**: URL configuration for the chatbot app.
- **django_chatbot/**: Project settings and configurations.
  - **settings.py**: Project settings.
  - **urls.py**: Project URL configuration.
  - **wsgi.py**: WSGI configuration.
- **venv/**: Virtual environment directory.
- **requirements.txt**: List of required Python packages.
- **.env**: Environment variables for the project.

## Code Explanation

### `models.py`

Defines the `Message` model to store user and bot messages.

```python
from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    sender = models.CharField(max_length=10)  # 'user' or 'bot'
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} ({self.sender}): {self.message[:50]}'
```

### `views.py`

Handles the chat logic and authentication.

```python
from django.shortcuts import render
from django.http import JsonResponse
from .models import Message
from django.contrib.auth.decorators import login_required

@login_required
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        user = request.user

        # Save user message to the database
        Message.objects.create(user=user, message=message, sender='user')

        response_text = ask_openai(message)

        # Save bot response to the database
        Message.objects.create(user=user, message=response_text, sender='bot')

        return JsonResponse({'message': message, 'response': response_text})

    else:
        # Load chat history
        messages = Message.objects.filter(user=request.user).order_by('timestamp')
        return render(request, 'chatbot/chatbot.html', {'messages': messages})
```

### `chatbot.html`

HTML template for the chatbot interface.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chatbot</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
        }
        #chat-container {
            width: 90%;
            max-width: 600px;
            margin: 50px auto;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        #chat-title {
            background-color: #007bff;
            color: #ffffff;
            padding: 10px;
            border-radius: 10px 10px 0 0;
            text-align: center;
        }
        #chatbox {
            padding: 10px;
            height: 400px;
            overflow-y: scroll;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
        }
        .message {
            margin: 10px 0;
            padding: 10px;
            border-radius: 10px;
            width: fit-content;
            max-width: 70%;
        }
        .message.user {
            background-color: #007bff;
            color: #ffffff;
            align-self: flex-end;
        }
        .message.bot {
            background-color: #e9ecef;
            align-self: flex-start.
        }
        #inputBox {
            display: flex;
            padding: 10px;
        }
        #inputBox input {
            flex: 1;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ced4da;
        }
        #inputBox button {
            margin-left: 10px;
            padding: 10px 20px;
            border-radius: 5px;
            border: none;
            background-color: #007bff;
            color: #ffffff;
        }
    </style>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
</head>
<body>
    <div id="chat-container">
        <div id="chat-title">Chatbot</div>
        <div id="chatbox">
            {% for message in messages %}
                <div class="message {{ message.sender }}">{{ message.message }}</div>
            {% endfor %}
            <div class="message bot">Welcome! How can I help you today?</div>
        </div>
        <div id="inputBox">
            <input type="text" id="message" placeholder="Type your message here...">
            <button id="send">Send</button>
        </div>
    </div>

    <script>
        $(document).ready(function() {
            $('#send').click(function() {
                sendMessage();
            });

            $('#message').keypress(function(e) {
                if (e.which == 13) { // Enter key pressed
                    sendMessage();
                }
            });

            function sendMessage() {
                var message = $('#message').val();
                if (message.trim() === "") return;
                
                $('#chatbox').append('<div class="message user">' + message + '</div>');
                $('#message').val('');

                $.ajax({
                    type: 'POST',
                    url: '',
                    data: {
                        'message': message,
                        'csrfmiddlewaretoken': '{{ csrf_token }}'
                    },
                    success: function(response) {
                        $('#chatbox').append('<div class="message bot">' + response.response + '</div>');
                        $('#chatbox').scrollTop($('#chatbox')[0].scrollHeight);
                    }
                });
            }
        });
    </script>
</body>
</html>
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Replace `yourusername` in the Git clone URL with your actual GitHub username or the URL of your repository.
