from django.shortcuts import render
from .models import Price
from django.utils import timezone
# Create your views here.

def price_list(request):
    prices = Price.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'graph/price_list.html', {'prices': prices})