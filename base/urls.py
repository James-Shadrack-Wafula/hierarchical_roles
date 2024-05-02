from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_seller/', views.add_seller, name='add_seller'),
    path('add_manager/', views.add_manager, name='add_manager'),
    path('manager_list/', views.manager_list, name='manager_list'),
    path('seller_list/', views.seller_list, name='seller_list'),
    path('update_seller/', views.update_seller, name='update_seller'),
    path('update_manager/', views.update_manager, name='update_manager'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('update_manager/<int:manager_id>/', views.update_manager, name='update_manager'),
    path('update_seller/<int:seller_id>/', views.update_seller, name='update_seller'),
  
]
