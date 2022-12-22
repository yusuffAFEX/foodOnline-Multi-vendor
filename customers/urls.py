from django.urls import path
from accounts import views as accounts_view
from . import views


urlpatterns = [
    path('', accounts_view.customer_dashboard, name='customer_dashboard'),
    path('profile/', views.customer_profile, name='customer_profile'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('order_detail/<int:order_number>/', views.order_details, name='order_details'),
]