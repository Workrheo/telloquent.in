from django.urls import path, include
from . import views
from accounts import views as AccountViews


urlpatterns = [
    path('', AccountViews.designerDashboard, name='designer'),
    path('profile/', views.dprofile, name='dprofile'),

    path('porfolio-builder/', views.portfolio_builder, name='portfolio_builder'),
    path('porfolio-builder/category/<int:pk>/', views.portfolioitems_by_category, name='portfolioitems_by_category'),

    path('portfolio-builder/category/add/', views.add_category, name='add_category'),
    path('portfolio-builder/category/edit/<int:pk>/', views.edit_category, name='edit_category'),
    path('portfolio-builder/category/delete/<int:pk>/', views.delete_category, name='delete_category'),

    path('portfolio-builder/portfolio/add/', views.add_portfolio, name='add_portfolio'),
    path('portfolio-builder/portfolio/edit/<int:pk>/', views.edit_portfolio, name='edit_portfolio'),
    path('portfolio-builder/portfolio/delete/<int:pk>/', views.delete_portfolio, name='delete_portfolio'),


    path('opening-hours/', views.opening_hours, name='opening_hours'),
    path('opening-hours/add/', views.add_opening_hours, name='add_opening_hours'),
    path('opening-hours/edit/<int:pk>/', views.edit_opening_hours, name='edit_opening_hours'),
    path('opening-hours/delete/<int:pk>/', views.delete_opening_hours, name='delete_opening_hours'),



    path('d_appointment', views.d_appointment, name="d_appointment"),
    path('update_status/<int:pid> ', views.update_status, name="update_status"),
    path('designer_cancel_appointment<int:pid>', views.designer_cancel_appointment, name="designer_cancel_appointment"),
    path('confirmed_d_appointment', views.confirmed_d_appointment, name="confirmed_d_appointment"),

    path('d_checklist', views.d_checklist, name="d_checklist"),
    path('checklist_status/<int:pid>', views.checklist_status, name="checklist_status"),











    


]