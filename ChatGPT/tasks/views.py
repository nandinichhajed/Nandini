from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
import openai
import os

openai.api_key = os.environ['openai.api_key']


class TaskView(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        prompt = serializer.validated_data['prompt']

        system_prompt = f'{{"role": "system", "content": "{prompt}"}}'

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt}
            ],
            temperature = 0.7,

        )

        generated_text = response.choices[0].message.content.strip()

        return Response({'response': generated_text})