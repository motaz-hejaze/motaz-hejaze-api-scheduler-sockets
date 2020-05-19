from django.urls import path
from . import views

# all urls for api_fetcher app
urlpatterns = [
    #home page to show data
    path('', views.index, name='index'),
]