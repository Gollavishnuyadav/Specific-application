from app2.views import *

from django.urls import path

app_name="two"


urlpatterns=[
    path("two/",two,name="two"),
]