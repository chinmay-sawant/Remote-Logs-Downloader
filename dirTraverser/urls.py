from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('checkIT/', views.checkIT, name='checkIT'),
    path('SharedPath/', views.SharedPath, name='SharedPath'),
    path('downloadLog/', views.downloadLog, name='downloadLog'),
  

]