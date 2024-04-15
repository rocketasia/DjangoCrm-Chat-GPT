from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Customer
from .forms import CustomerForm


@login_required
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'crm/customer_list.html', {'customers': customers})

@require_POST  # Ensure that this view can only be accessed via POST request for safety
def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect('/')  # Redirect to a page that lists customers, adjust as necessary


@login_required
def edit_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to the customer list or detail view
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customers/edit_customer.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            success: True(user) # type: ignore
            login(request, user)
            messages.success(request, "You Registered...")
            return redirect('/')  # Adjust the redirect as necessary
            
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def logout_user(request):
     logout(request)
     messages.success(request, "You Have Been Logged Out...")
     return redirect('/')

@login_required
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            success: True
            return redirect('/')  # Redirect to your customers' list view
    else:
        form = CustomerForm()
    return render(request, 'customers/add_customer.html', {'form': form})