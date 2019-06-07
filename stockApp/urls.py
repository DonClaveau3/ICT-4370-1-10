"""urls for the stock app"""

from django.urls import path

from . import views

app_name = 'stockApp'
urlpatterns = [
    #Home page
    path('',views.index, name='index')
]