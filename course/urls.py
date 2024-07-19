from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug>/', views.more, name='more'),
    path('about/<slug>/', views.about, name='about'),

]
