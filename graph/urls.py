from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.price_list, name='price_list'),
]