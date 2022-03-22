from django.urls import path
from practicalTestApp import views

app_name = 'practicalTestApp'
urlpatterns = [
    path('', views.course, name='course'),
]