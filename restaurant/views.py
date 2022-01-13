from django.shortcuts import render
from django.views import View 
from django.utils.timezone import datetime
from customer.models import *
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

# Create your views here.

""" def Dashboard(request):

  return render(request,'restaurant/dashboard.html') """

class Dashboard(LoginRequiredMixin, UserPassesTestMixin, View):
  def get(self, request, *args, **kwargs):

    today = datetime.today()
    orders =  OrderModel.objects.filter(created_on__year=today.year, created_on__month=today.month, created_on__day=today.day)

    total_revenue = 0
    for order in orders:
      total_revenue += order.price

    context ={
      'orders':orders,
      'total_revenue':total_revenue,
      'total_orders':len(orders)
    }

    return render(request,'restaurant/dashboard.html',context)


 



  def test_func(self):
    return self.request.user.groups.filter(name='Staff').exists()



class OrderDetails(LoginRequiredMixin, UserPassesTestMixin, View):
  def get(self, request, pk, *args, **kwargs):
    order = OrderModel.objects.get(pk=pk)
    context = {
      'order':order 

    }

    return render(request,'restaurant/order-details.html',context)


  

  def post(self , request, pk, *args, **kwargs ):
    order = OrderModel.objects.get(pk=pk)
    order.order_completed = True
    order.save()

    context = {
      'order': order
    }

    return render(request, 'restaurant/order-details.html',context)



  def test_func(self):
    return self.request.user.groups.filter(name='Staff').exists()


class Orders_Pending(LoginRequiredMixin, UserPassesTestMixin, View):
  def get(self, request, *args, **kwargs):

    today = datetime.today()
    orders =  OrderModel.objects.filter(created_on__year=today.year, created_on__month=today.month, created_on__day=today.day)


    orders_pending = []
    total_revenue = 0
    for order in orders:
      total_revenue += order.price

      if not order.order_completed:
        orders_pending.append(order)

    context ={
      'orders':orders_pending,
      'total_revenue':total_revenue, 
      'total_orders':len(orders)
    }

    return render(request,'restaurant/orders-pending.html',context)


 



  def test_func(self):
    return self.request.user.groups.filter(name='Staff').exists()



class ordersComplete(LoginRequiredMixin, UserPassesTestMixin, View):
  def get(self, request, *args, **kwargs):

    today = datetime.today()
    orders =  OrderModel.objects.filter(created_on__year=today.year, created_on__month=today.month, created_on__day=today.day)


    orders_completed = []
    total_revenue = 0
    for order in orders:
      total_revenue += order.price

      if  order.order_completed:
        orders_completed.append(order)

    context ={
      'orders':orders_completed,
      'total_revenue':total_revenue, 
      'total_orders':len(orders)
    }

    return render(request,'restaurant/orders-completed.html',context)


 



  def test_func(self):
    return self.request.user.groups.filter(name='Staff').exists()
