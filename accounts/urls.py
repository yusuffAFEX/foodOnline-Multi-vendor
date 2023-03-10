from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.my_account),
    path('registerUser/', views.register_user, name='registerUser'),
    path('registerVendor/', views.register_vendor, name='registerVendor'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('MyAccount/', views.my_account, name='MyAccount'),
    path('customerDashboard/', views.customer_dashboard, name='customerDashboard'),
    path('vendorDashboard/', views.vendor_dashboard, name='vendorDashboard'),

    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password_validate/<uidb64>/<token>/', views.reset_password_validate, name='reset_password_validate'),
    path('reset_password/', views.reset_password, name='reset_password'),

    path('vendor/', include('vendor.urls')),
    path('customers/', include('customers.urls')),
]
