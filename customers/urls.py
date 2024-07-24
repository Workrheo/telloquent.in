from django.urls import path , include
from accounts import views as AccountViews
from . import views


urlpatterns = [
    path('', AccountViews.custDashboard, name='customer'),
    path('cprofile/', views.cprofile, name='cprofile'),

    path('appointment<int:pid>/', views.appointment, name='appointment'),
    path('booking-success<int:pid>', views.payment_success, name="booking-success"),


    path('c_appointment', views.c_appointment, name="c_appointment"),
    path('cancel_appointment<int:pid>', views.cancel_appointment, name="cancel_appointment"),

    path('confirmed_c_appointment', views.confirmed_c_appointment, name="confirmed_c_appointment"),

    path('checklist<int:pid>/', views.checklist, name='checklist'),
    path('checklist-success<int:pid>', views.checklist_success, name="checklist-success"),


    path('architect_appointment<int:pid>/', views.architect_appointment, name='architect_appointment'),
    path('architect_booking-success<int:pid>', views.architect_payment_success, name="architect_booking-success"),


    path('architect_c_appointment', views.architect_c_appointment, name="architect_c_appointment"),
    path('architect_cancel_appointment<int:pid>', views.architect_cancel_appointment, name="architect_cancel_appointment"),

    path('architect_confirmed_c_appointment', views.architect_confirmed_c_appointment, name="architect_confirmed_c_appointment"),



    path('builder_appointment<int:pid>/', views.builder_appointment, name='builder_appointment'),
    path('builder_booking-success<int:pid>', views.builder_payment_success, name="builder_booking-success"),


    path('builder_c_appointment', views.builder_c_appointment, name="builder_c_appointment"),
    path('builder_cancel_appointment<int:pid>', views.builder_cancel_appointment, name="builder_cancel_appointment"),

    path('builder_confirmed_c_appointment', views.builder_confirmed_c_appointment, name="builder_confirmed_c_appointment"),








]