

# chatbot_app/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from telegram import Bot, Update
from .models import UserProfile , Conversation


telegram.api_key = "6507712205:AAGlSy9rl6C3k5z5EjQ0B32Zxt1ORZPbq2w"  # Replace with your telegram API key

@csrf_exempt
def handle_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data['user_id']
        message = data['message']

        # Process message and get response
        response = process_message(user_id, message)

        # Save conversation
        user_profile = UserProfile.objects.get(user_id=user_id)
        Conversation.objects.create(user=user_profile, message=message)

        return JsonResponse({'response': response})
    else:
        return JsonResponse({'error': 'Invalid request method'})

def process_message(user_id, message):
    # Use OpenAI to generate a response
    response = telegram.Completion.create(
        engine="text-davinci-003",
        prompt=message,
        max_tokens=50
    )

    return response.choices[0].text.strip()
