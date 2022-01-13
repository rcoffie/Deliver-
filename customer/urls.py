from django.urls import path
from . import views 
from .views import Index, About, Order, Search


app_name = 'customer'

urlpatterns = [
  path('',views.Index,name='home'),
  path('about/',views.About,name='about'),
  path('order/',Order.as_view(), name='order'),
  path('search/',views.Search,name="search"),
  # path('serach/',Search.as_view(),name='search')
]
