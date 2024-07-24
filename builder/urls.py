from django.urls import path, include
from . import views
from accounts import views as AccountViews



urlpatterns =[
    path('', AccountViews.builderDashboard, name='builder'),
    path('bprofile/', views.bprofile, name='bprofile'),

    path('builder_porfolio-builder/', views.builder_portfolio_builder, name='builder_portfolio_builder'),
    path('builder_porfolio-builder/category/<int:pk>/', views.builder_portfolioitems_by_category, name='builder_portfolioitems_by_category'),

    path('builder_portfolio-builder/category/add/', views.builder_add_category, name='builder_add_category'),
    path('builder_portfolio-builder/category/edit/<int:pk>/', views.builder_edit_category, name='builder_edit_category'),
    path('builder_portfolio-builder/category/delete/<int:pk>/', views.builder_delete_category, name='builder_delete_category'),


    path('builder_portfolio-builder/portfolio/add/', views.builder_add_portfolio, name='builder_add_portfolio'),
    path('builder_portfolio-builder/portfolio/edit/<int:pk>/', views.builder_edit_portfolio, name='builder_edit_portfolio'),
    path('builder_portfolio-builder/portfolio/delete/<int:pk>/', views.builder_delete_portfolio, name='builder_delete_portfolio'),


    path('builder_opening-hours/', views.builder_opening_hours, name='builder_opening_hours'),
    path('builder_opening-hours/add/', views.builder_add_opening_hours, name='builder_add_opening_hours'),
    path('builder_opening-hours/edit/<int:pk>/', views.builder_edit_opening_hours, name='builder_edit_opening_hours'),
    path('builder_opening-hours/delete/<int:pk>/', views.builder_delete_opening_hours, name='builder_delete_opening_hours'),


    path('b_appointment', views.b_appointment, name="b_appointment"),
    path('builder_update_status/<int:pid> ', views.builder_update_status, name="builder_update_status"),
    path('builder_cancel_appointment<int:pid>', views.builder_cancel_appointment, name="builder_cancel_appointment"),
    path('confirmed_b_appointment', views.confirmed_b_appointment, name="confirmed_b_appointment"),
]
