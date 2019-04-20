from django.urls import path
from . import views

app_name = 'maths'

urlpatterns = [
    path('', views.index, name='index'),
]
