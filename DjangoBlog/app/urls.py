from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('index/Blog/<str:pk>', views.BlogDetails, name='BlogDetails'),
    path('Blog/<str:pk>', views.BlogDetails, name='BlogDetails')
]
