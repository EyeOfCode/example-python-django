from user_app import views

from django.urls import path

urlpatterns = [
    path('', views.UserList),
    path('<int:id>/', views.UserDetail),
]