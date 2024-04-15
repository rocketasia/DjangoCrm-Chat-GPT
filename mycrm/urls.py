from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from crm import views as crm_views
from crm.views import edit_customer, delete_customer, add_customer
from django.views.generic.base import TemplateView  # new
# from crm.views import delete_customer


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crm.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('customer/edit/<int:pk>/', edit_customer, name='edit_customer'),
    path('customer/delete/<int:pk>/', delete_customer, name='delete_customer'),
    path('registration/signup/', crm_views.signup, name='signup'),
     path('customer/add/', add_customer, name='add_customer'),
     path("", TemplateView.as_view(template_name="customer_list.html"), name="customer_list"),
]