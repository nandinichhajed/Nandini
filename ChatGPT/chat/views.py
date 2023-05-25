from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from django.shortcuts import render
from .models import *
import openai
import os
from django.http import JsonResponse


openai.api_key = os.environ['openai.api_key']


class HotelNameView(APIView):
    def post(self, request):
        
        prompt = request.data.get('prompt', '')
        print(prompt)
        system_prompt = f'{{"role": "system", "content": "{prompt}"}}'

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt}
            ],
            temperature = 0.7,
        )

        generated_text = response.choices[0].message.content.strip()
        print(generated_text)
        
        chat = Chat.objects.create(
            text=prompt,
            gpt=generated_text
        )
        
        return Response({'response': generated_text})
    
    
    
def processPrompt(request):
    if request.method == 'POST':
        user_prompt = request.POST.get('message', '')
        print(user_prompt)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "system message"},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
        )

        assistant_response = response.choices[0].message.content.strip()
        print(assistant_response)

        return JsonResponse({'response': assistant_response})

    return render(request, 'prompt.html')



def render_index(request):
    data = Hotel.objects.all() 
    return render(request, 'index.html', {'data': data})



class ProcessView(APIView):
    def get(self, request):
        data = Processes.objects.all() 
        return render(request, 'process.html', {'data': data})
    
