from django.urls import path

from . import views


app_name = 'robots'

urlpatterns = [
    path('create-robot/', views.create_robot, name='create-robot'),
]
