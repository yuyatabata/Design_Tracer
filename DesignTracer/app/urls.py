from django.contrib import path
from . import views

app_name = "app"
urlpattern = [
    path('',views.index, name='index'),
    path('users/<int:pk>/',views.users_detail, name='users_detail'),
]