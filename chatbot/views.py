from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import openai
import os
from .models import Message
from django.contrib.auth.models import User

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_openai(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return str(e)

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

@login_required
def profile(request):
    return render(request, 'chatbot/profile.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'chatbot/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'chatbot/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')
