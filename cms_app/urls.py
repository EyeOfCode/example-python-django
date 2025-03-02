from cms_app import views

from django.urls import path

urlpatterns = [
    path('', views.index, name='cms_index'),
    path('about', views.about, name='cms_about'),
]