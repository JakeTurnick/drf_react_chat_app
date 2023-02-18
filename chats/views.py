from django.shortcuts import render
from rest_framework import generics
from django.shortcuts import get_object_or_404

from .models import Chat_room, Chat_message
from .serializers import ChatRoomsSerializer, ChatMsgSerializer


# Create your views here.
class ChatRoomsListAPIView(generics.ListCreateAPIView):
    queryset = Chat_room.objects.all()
    serializer_class = ChatRoomsSerializer


class ChatRoomListAPIView(generics.ListAPIView):
    serializer_class = ChatRoomsSerializer

    def get_queryset(self):
        room = self.kwargs['roomid']
        return Chat_room.objects.filter(id=room)


class ChatRoomsMsgsAPIView(generics.ListAPIView):
    serializer_class = ChatMsgSerializer
    queryset = Chat_message.objects.all()


class ChatRoomMsgsAPIView(generics.ListCreateAPIView):
    serializer_class = ChatMsgSerializer

    def get_queryset(self):
        room = self.kwargs['roomid']
        return Chat_message.objects.filter(room=room)
