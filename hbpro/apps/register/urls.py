from django.conf.urls import url

from apps.register.views import register_db

urlpatterns = [
    url(r'^',register_db, name='register'),    
]
