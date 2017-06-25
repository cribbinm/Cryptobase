from django.shortcuts import render
from .models import Price
from django.utils import timezone
# Create your views here.
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import LineChart
from graphos.sources.model import ModelDataSource


# def price_list(request):
#     prices = Price.objects.order_by('entry')
#     return render(request, 'graph/price_list.html', {'prices': prices})


def graphoo(request):

	queryset = Price.objects.all()
	data_source = ModelDataSource(queryset,
	                              fields=['entry', 'xbt'])
	# Chart object
	chart = LineChart(data_source)
	context = {'chart': chart}
	return render(request, 'graph/price_list.html', context)