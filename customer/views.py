from django.shortcuts import render
from .models import *
from django.views import View
from django.db.models import Q
from django.core.mail import send_mail
# Create your views here.


def Index(request):

  return render(request,'customer/index.html')




def About(request):

  return render(request,'customer/about.html')


class Order(View):
  def get(self, request, *args, **kwargs):
    appetizers = MenuItem.objects.filter(category__name__contains='Appetizer')
    entres = MenuItem.objects.filter(category__name__contains='Entre')
    desserts = MenuItem.objects.filter(category__name__contains='Dessert')
    drinks = MenuItem.objects.filter(category__name__contains='Drink')
    
    
    context = {
      'appetizers':appetizers, 
      'entres':entres,
      'desserts':desserts,
      'drinks':drinks,
    }
    
    return render(request, 'customer/order.html',context)
  
  
  def post(self, request, *args, **kwargs):
    name = request.POST.get('name')
    email = request.POST.get('email')
    location = request.POST.get('location')
    
    
    order_items = {
      'items':[]
    }
    items = request.POST.getlist('items[]')
    for item in items:
      menu_item = MenuItem.objects.get(pk__contains=int(item))
      item_data = {
        'id':menu_item.pk,
        'name':menu_item.name,
        'price':menu_item.price
      }
      
      order_items['items'].append(item_data)
      price = 0
      
      item_ids = []
      
    for item in order_items['items']:
      price += item['price']
      item_ids.append(item['id'])
        
      order = OrderModel.objects.create(
        price=price,
        name =name,
        email = email,
        location= location,
        )
      order.items.add(*item_ids)
      
      #Order Confirmation mail 
      body = ('Thank you for your oder!')
      send_mail(
        'Oder Received',
        body,
        'deliver@de.com',
        [email],
        fail_silently=False
      
      )
      context = {
        
        'items':order_items['items'],
        'price':price
        
      }
      
      return render(request,'customer/order_confirmation.html',context)



def Search(request):

  menus = MenuItem.objects.all()
  query = request.GET.get('q')
  if query:
    menus = MenuItem.objects.all().filter(
      Q(name__icontains=query)|
      Q(price__icontains=query)|
      Q(category__name__icontains=query)
    )


  context = {
    'menus':menus,
  }
  return render(request,'customer/search.html',context)
      
    
