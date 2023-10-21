from django.shortcuts import render
from django.views import View
from django.db.models import Q
from customer.models import Category, MenuItem, OrderModel
# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        menu_items=MenuItem.objects.all()
        context = {
            'menu_items': menu_items.order_by('category')[:5]
        }
        return render(request, 'customer/index.html', context)

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')

class Order(View):
    def get(self, request, *args, **kwargs):

        #get every item from each category
        appetizers = MenuItem.objects.filter(category__name__contains='Appetizer')
        entres = MenuItem.objects.filter(category__name__contains='Entre')
        desserts = MenuItem.objects.filter(category__name__contains='Dessert')
        drinks = MenuItem.objects.filter(category__name__contains='Drink')
        # pass into context
        context ={
            'appetizers': appetizers,
            'entres': entres,
            'desserts': desserts,
            'drinks':drinks,
        }
        #render the template     
        return render(request, 'customer/order.html',context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        ward = request.POST.get('ward')
        district = request.POST.get('district')
        city = request.POST.get('city')

        order_items ={
            'items': []
        }

        items = request.POST.getlist('items[]')

        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            item_data ={
                'id': menu_item.pk,
                'name':menu_item.name,
                'price': menu_item.price
            }   

            order_items['items'].append(item_data) 

        price = 0
        item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        order = OrderModel.objects.create(
            price=price,
            name=name,
            email=email,
            street=street,
            ward=ward,
            district=district,
            city=city
            )
        order.items.add(*item_ids)
            
        context = {
            'items': order_items['items'],
            'price':price
        }    

        return render(request, 'customer/order_confirmation.html', context)

class Menu(View):
    def get(self, request, *args, **kwargs):
        menu_items=MenuItem.objects.all()

        context = {
            'menu_items': menu_items.order_by('category')
        }

        return render(request, 'customer/menu.html',context)
class MenuSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get("q")

        menu_items=MenuItem.objects.filter(
            Q(name__icontains=query) |
            Q(price__icontains=query) |
            Q(description__icontains=query)
        ) 

        context = {
            'menu_items': menu_items
        }

        return render(request, 'customer/menu.html', context)
