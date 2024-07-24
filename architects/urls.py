from django.urls import path, include
from . import views
from accounts import views as AccountViews



urlpatterns =[
    path('', AccountViews.architectDashboard, name='architect'),
    path('aprofile/', views.aprofile, name='aprofile'),

    path('architect_porfolio-builder/', views.architect_portfolio_builder, name='architect_portfolio_builder'),
    path('architect_porfolio-builder/category/<int:pk>/', views.architect_portfolioitems_by_category, name='architect_portfolioitems_by_category'),

    path('architect_portfolio-builder/category/add/', views.architect_add_category, name='architect_add_category'),
    path('architect_portfolio-builder/category/edit/<int:pk>/', views.architect_edit_category, name='architect_edit_category'),
    path('architect_portfolio-builder/category/delete/<int:pk>/', views.architect_delete_category, name='architect_delete_category'),


    path('architect_portfolio-builder/portfolio/add/', views.architect_add_portfolio, name='architect_add_portfolio'),
    path('architect_portfolio-builder/portfolio/edit/<int:pk>/', views.architect_edit_portfolio, name='architect_edit_portfolio'),
    path('architect_portfolio-builder/portfolio/delete/<int:pk>/', views.architect_delete_portfolio, name='architect_delete_portfolio'),


    path('architect_opening-hours/', views.architect_opening_hours, name='architect_opening_hours'),
    path('architect_opening-hours/add/', views.architect_add_opening_hours, name='architect_add_opening_hours'),
    path('architect_opening-hours/edit/<int:pk>/', views.architect_edit_opening_hours, name='architect_edit_opening_hours'),
    path('architect_opening-hours/delete/<int:pk>/', views.architect_delete_opening_hours, name='architect_delete_opening_hours'),


    path('a_appointment', views.a_appointment, name="a_appointment"),
    path('architect_update_status/<int:pid> ', views.architect_update_status, name="architect_update_status"),
    path('architect_cancel_appointment<int:pid>', views.architect_cancel_appointment, name="architect_cancel_appointment"),
    path('confirmed_a_appointment', views.confirmed_a_appointment, name="confirmed_a_appointment"),
]
