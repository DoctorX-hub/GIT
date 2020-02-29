from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('good_ip/', views.index, name='good_ip'),
    path('bad_ip/', views.index, name='bad_ip'),
    path('all_ip/', views.index, name='all_ip'),
    path('which_ip/', views.index, name='which_ip'),
    path('is_ip_bad/', views.index, name='is_ip_bad'),
]