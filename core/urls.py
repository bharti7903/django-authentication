from django.urls import path
from core.views import index, secret
urlpatterns = [
   
    path('index/', index, name = 'index'),
    path('secret/', secret, name= 'secret'),
]
