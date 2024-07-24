from django.urls import path, include
from . import views


urlpatterns = [


    path('', views.home, name='home'),


    path('designer_list', views.designer_list, name='designer_list'),
    path('<slug:designer_slug>/', views.designer_detail, name='designer_detail'),



    path('architect_list', views.architect_list, name='architect_list'),
    path('architects/<slug:architect_slug>/', views.architect_detail, name='architect_detail'),


    path('builder_list', views.builder_list, name='builder_list'),
    path('builder/<slug:builder_slug>/', views.builder_detail, name='builder_detail'),








    path('services', views.services, name='services'),
    path('pricing', views.pricing, name='pricing'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('success/' , views.send_success , name='send_success'),
    path('join_as_pro' , views.join_as_pro , name='join_as_pro'),




    


]