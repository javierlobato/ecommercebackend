from django.urls import path
from .views import HelloWorldView

urlpatterns = [
    path('hello/', HelloWorldView.as_view(), name='hello-world'),  #Ahora el endpoint será: http://127.0.0.1:8000/api/hello
]