from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HotelNameSerializer
from django.shortcuts import render
import openai
import os

openai.api_key = os.environ['openai.api_key']


class HotelNameView(APIView):
    def post(self, request):
        
        prompt = "hello how are you?"
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
        return Response({'response': generated_text})
    


def render_index(request):
    return render(request, 'index.html')