from django.urls import path
from . import views



app_name = 'vision_logs'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('new_topics/', views.new_topics, name='new_topics'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

]
