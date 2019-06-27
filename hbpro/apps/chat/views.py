from django.shortcuts import render

# Create your views here.
import uuid

from django.shortcuts import render

from apps.chat.models import Message
from apps.user.models import Student2, Mentor, User, Courses_Student, Course, Students_Mentor


# Create your views here.
mem_glob = Mentor()
sm_glob = Students_Mentor()
studiamt = Student2()
def index(request):
    uid4 = str(uuid.uuid4())
    #import pudb; pudb.set_trace()
    return render(request, 'chat/index.html', {'uid4': uid4})


def room(request, room_name):
    chat_messages = Message.objects.filter(group_name=room_name).order_by("created")[:100]
    #import pudb; pudb.set_trace()
    #return render(request, 'contentuser/userimdex.html', {'stu': studiamt, 'sm': sm_glob})
    return render(request, 'chat/room.html', {
        'chat_messages': chat_messages,
        'room_name': room_name,
        'stu': studiamt,
        'sm': sm_glob

    })
