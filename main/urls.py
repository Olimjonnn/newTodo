from django.urls import path
from .views import *

urlpatterns = [
    path("works/<int:pk>", WorksGETbyID.as_view()),
    path("works/", WorksView.as_view()),
    path("works/true/", WorkTrue.as_view()),
    path("works/false/", WorkFalse.as_view()),
]