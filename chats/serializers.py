from rest_framework import serializers

from .models import Chat_room, Chat_message


class ChatRoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat_room
        fields = '__all__'


class ChatMsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat_message
        fields = '__all__'
