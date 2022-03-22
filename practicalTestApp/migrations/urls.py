from django.urls import path
from practicalTestApp import views

app_name = 'GA'
urlpatterns = [
    path('', views.course, name='course'),
]