from rest_framework import serializers

class HotelNameSerializer(serializers.Serializer):
    prompt = serializers.CharField(max_length=1000)