from django.urls import path
from . import views 
from .views import Dashboard,OrderDetails,Orders_Pending,ordersComplete


app_name = 'restaurant'

urlpatterns = [
#  path('',views.Dashboard,name='dashboard')
path('',Dashboard.as_view(), name='dashboard'),
path('pending/',Orders_Pending.as_view(), name="ordersPending"),
path('orders-complete/', ordersComplete.as_view(), name="order-complete"),
path('orders/<int:pk>/', OrderDetails.as_view(), name='order-details')

]
  