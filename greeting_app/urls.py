from django.urls import path
from .views import birthday

urlpatterns=[
    path("",birthday, name="birthday")
]