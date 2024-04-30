from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_seller/', views.add_seller, name='add_seller'),
    path('add_manager/', views.add_manager, name='add_manager'),
    path('seller_list/', views.seller_list, name='seller_list'),
    # Add more URLs as needed for additional functionalities
]
