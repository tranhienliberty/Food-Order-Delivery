from datetime import datetime
from re import L
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from customer.models import OrderModel
from matplotlib.style import context

from customer.models import OrderModel
# Create your views here.

class Dashboard(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        #get the current date
        today = datetime.today()
        orders = OrderModel.objects.filter(created_on__year = today.year, created_on__month = today.month, created_on__day = today.day)
        #loop through the orders and add the price value 
        total_revenue = 0
        for order in orders:
            total_revenue += order.price
        #pass total number of orders and total revenue into template
        context = {
            'orders' : orders,
            'total_revenue' : total_revenue,
            'total_orders' : len(orders)
            }
        
        return render(request, 'restaurant/dashboard.html', context)
    def test_func(self):
        return self.request.user.groups.filter(name = 'Staff').exists()

class OrderDetails(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)
        context ={
            'order' : order,
        }
        return render(request, 'restaurant/order-details.html', context)
    
    def post (self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)
        order.is_shipped = True
        order.save()

        context = {
            'order' : order
        }
        return render(request, 'restaurant/order-details.html', context)

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()
