from app1.views import *

from django.urls import path

app_name="one"


urlpatterns=[
    path("one/",one,name="one"),
]