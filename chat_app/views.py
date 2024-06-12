from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json

def chat_view(request):
    if 'messages' not in request.session:
        request.session['messages'] = []

    if request.method == 'POST':
        query = request.POST.get('query')
        response = call_gemini_api(query)
        messages = request.session['messages']
        messages.append(f'You: {query}')
        messages.append(f'Gemini: {response}')
        request.session['messages'] = messages[-6:] 

        return render(request, 'chat_app/chat.html', {'messages': messages})

    return render(request, 'chat_app/chat.html', {'messages': request.session['messages']})

def call_gemini_api(query):
    url = 'https://api.gemini.com/v1/query' 
    payload = {'query': query}
    headers = {'Authorization': 'AIzaSyCxF0qc3MQMCpFg4fXnaJY_wvj9C-PEc0g'}
    response = requests.post(url, json=payload, headers=headers)
    return response.json().get('response', 'No response from Gemini')
