from members_app import views

from django.urls import path

urlpatterns = [
    path('', views.MemberList),
    path('create', views.MemberCreate),
    path('update/<int:id>', views.MemberUpdate),
    path('delete/<int:id>', views.MemberDelete),
    path('<int:id>/', views.MemberDetail),
]