from django.contrib import admin
from .models import Chat_room
from .models import Chat_message

# Register your models here.
admin.site.register(Chat_room)
admin.site.register(Chat_message)
