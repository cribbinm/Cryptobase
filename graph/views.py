from django.shortcuts import render

# Create your views here.

def price_list(request):
    return render(request, 'graph/price_list.html', {})