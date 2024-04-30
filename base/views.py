# authentication/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Seller


from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, ManagerForm, SellerForm

def add_manager(request):
    if request.user.is_superuser:  # Check if user is Admin
        if request.method == 'POST':
            form = ManagerForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('manager_list')
        else:
            form = ManagerForm()
        return render(request, 'base/add_manager.html', {'form': form})
    else:
        return redirect('dashboard')

def add_seller(request):
    if request.user.is_superuser or request.user.user_role == 'Manager':  # Check if user is Admin or Manager
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

def manager_list(request):
    if request.user.is_superuser:  # Check if user is Admin
        managers = Manager.objects.all()
        return render(request, 'manager_list.html', {'managers': managers})
    else:
        return redirect('dashboard')

def seller_list(request):
    sellers = Seller.objects.all()
    return render(request, 'base/seller_list.html', {'sellers': sellers})

def update_manager(request, manager_id):
    if request.user.is_superuser:  # Check if user is Admin
        manager = Manager.objects.get(pk=manager_id)
        if request.method == 'POST':
            form = ManagerForm(request.POST, instance=manager)
            if form.is_valid():
                form.save()
                return redirect('manager_list')
        else:
            form = ManagerForm(instance=manager)
        return render(request, 'update_manager.html', {'form': form})
    else:
        return redirect('dashboard')

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
        return render(request, 'update_seller.html', {'form': form})
    else:
        return redirect('dashboard')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or dashboard
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'base/register.html', {'form': form})

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
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
        # Logic for admin dashboard
        return render(request, 'admin_dashboard.html')
    elif user_role == 'Manager':
        # Logic for manager dashboard
        return render(request, 'manager_dashboard.html')
    elif user_role == 'Seller':
        # Logic for seller dashboard
        return render(request, 'seller_dashboard.html')
    else:
        return render(request, 'base/dashboard.html')  # Default dashboard for unknown roles
