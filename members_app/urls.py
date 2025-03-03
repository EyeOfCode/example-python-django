from members_app import views

from django.urls import path

urlpatterns = [
    path('', views.MemberList),
    path('<int:id>/', views.MemberDetail),
]