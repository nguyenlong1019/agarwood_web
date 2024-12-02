from django.urls import path, include 
from core.views.index import * 


urlpatterns = [
    path('', index_view, name='index'),
]
