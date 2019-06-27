from django.conf.urls import url, include

from apps.login.views import login, contentuser, contentuseruser

urlpatterns = [
    #url(r'^qa', chamgePercemtage, name='chamgepercemtage'),
    url(r'^$', login, name='login'),
    url(r'^contentuser/memdex.html', contentuser, name='contentuser'),  # For mentor
    url(r'^contentuser/userimdex.html', contentuseruser, name='contentuseruser'), #For Student
   
    #url(r'^contentuser/', include('apps.contentuser.urls'),  name='login'),
    #url(r'^$', contentuser, name='contentuser'),
]
