from django.urls import path
from . import views

app_name = 'sns_apps'

urlpatterns = [
    path('', views.index, name='index')
]