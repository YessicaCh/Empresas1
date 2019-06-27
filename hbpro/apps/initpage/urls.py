from django.conf.urls import url

from apps.initpage.views import index

urlpatterns = [
    url(r'^$',index),
    
]
