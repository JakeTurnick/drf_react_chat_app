from django.urls import path
from . import views

urlpatterns = [
    path('rooms/<int:roomid>/messages/', views.ChatRoomMsgsAPIView.as_view()),
    path('rooms/<int:roomid>/', views.ChatRoomListAPIView.as_view()),
    path('rooms/messages/', views.ChatRoomsMsgsAPIView.as_view()),
    path('rooms/', views.ChatRoomsListAPIView.as_view())
]
