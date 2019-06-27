# chat/views.py
import json
from django.shortcuts import render
from django.utils.safestring import mark_safe
from chat.models import Message

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
	chat_messages = Message.objects.filter(group_name=room_name).order_by("created")[:100]
	return render(request, 'chat/room.html', {
        'chat_messages': chat_messages,
        'room_name_json': mark_safe(json.dumps(room_name))
    })
	"""return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })"""

