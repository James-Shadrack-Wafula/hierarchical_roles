# authentication/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Seller,Manager


from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, ManagerForm, SellerForm

from django.shortcuts import render

def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('login')

@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html', {'user': request.user})

@login_required
def add_manager(request):
    if request.user.is_superuser or request.user.user_role == 'Admin':  # Check if user is Admin
        if request.method == 'POST':
            form = ManagerForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('manager_list')
        else:
            form = ManagerForm()
        return render(request, 'base/add_manager.html', {'form': form})
    else:
        return render(request,'base/seller_dashboard.html', {'message': "Error: Unauthorized Access"})

@login_required
def add_seller(request):
    if request.user.is_superuser or request.user.user_role == 'Manager' or request.user.user_role == 'Admin':  # Check if user is Admin or Manager
        if request.method == 'POST':
            form = SellerForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('seller_list')
        else:
            form = SellerForm()
        return render(request, 'base/add_seller.html', {'form': form})
    else:
        return redirect('dashboard')

@login_required
def manager_list(request):
    # if request.user.is_superuser:  
    user = CustomUser.objects.get(username=request.user)

    managers = Manager.objects.all()
    return render(request, 'base/manager_list.html', {'managers': managers})
    #     else:
    #         return render(request, 'base/dashboard.html', {'massage': 'Warning: You have not been commisioned by Admin!'})
    # except Manager.DoesNotExist:
    #     manager2 = Manager.objects.create(user=user)
    #     manager2.save()
    #     return render(request, 'manager_list.html', {'managers': managers})

@login_required
def seller_list(request):
    sellers = Seller.objects.all()
    user = CustomUser.objects.get(username=request.user)
    return render(request, 'base/seller_list.html', {'sellers': sellers, 'user': user})

@login_required
def update_manager(request, manager_id):
    if request.user.is_superuser or request.user.user_role == 'Admin':  
        manager = Manager.objects.get(pk=manager_id)
        if request.method == 'POST':
            form = ManagerForm(request.POST, instance=manager)
            if form.is_valid():
                form.save()
                return redirect('manager_list')
        else:
            form = ManagerForm(instance=manager)
        return render(request, 'base/update_manager.html', {'form': form})
    else:
        return redirect('dashboard')
    
@login_required
def update_seller(request, seller_id):
    if request.user.is_superuser or request.user.user_role == 'Manager':  # Check if user is Admin or Manager
        seller = Seller.objects.get(pk=seller_id)
        if request.method == 'POST':
            form = SellerForm(request.POST, instance=seller)
            if form.is_valid():
                form.save()
                return redirect('seller_list')
        else:
            form = SellerForm(instance=seller)
        return render(request, 'base/update_seller.html', {'form': form})
    else:
        return redirect('dashboard')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'base/register.html', {'form': form})

# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'base/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'base/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    user_role = request.user.user_role
    if user_role == 'Admin':
        
        return render(request, 'base/admin_dashboard.html')
    elif user_role == 'Manager':
        
        return render(request, 'base/manager_dashboard.html')
    elif user_role == 'Seller':
        try:
            seller_username = request.user
            print(seller_username)
            usr = CustomUser.objects.get(username=seller_username)
            seller = Seller.objects.get(user=usr)
            # seller = Seller.objects.get(user__username=seller_username)
            print(seller)
            return render(request, 'base/seller_dashboard.html', {'seller': seller})
        except Seller.DoesNotExist:
            return render(request, 'base/dashboard.html', context={'massage': "Warning: You have not been commissioned as a Seller by the Admin or Manager", 'not_s': True})

    else:
        return render(request, 'base/dashboard.html')  # Default dashboard for unknown roles
