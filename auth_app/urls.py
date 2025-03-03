from auth_app import views

from django.urls import path

urlpatterns = [
    path('login', views.Login),
    path('register', views.Register),
    path('info', views.GetMembers)
]