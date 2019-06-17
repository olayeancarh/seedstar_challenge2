from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    # /index.html
    path('', views.index, name='index'),

    # /listings
    path('list', views.lists, name='list'),

    # /create
    path('add', views.add, name='add'),
]
