from rest_framework import serializers

class TaskSerializer(serializers.Serializer):
    prompt = serializers.CharField(max_length=1000)