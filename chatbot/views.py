from django.shortcuts import render
from django.http import JsonResponse
import openai
import os
from .models import Message
from django.contrib.auth.decorators import login_required

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_openai(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Replace with the appropriate model
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
