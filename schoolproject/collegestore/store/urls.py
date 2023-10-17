from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginn, name='login'),
    path('register/', views.register, name='register'),
    path('department/',views.department,name='department'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('get_courses/', views.get_courses, name='get_courses'),
    path('page/', views.page, name='page'),
]
