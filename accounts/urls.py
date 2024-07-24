from django.urls import path , include
from . import views



urlpatterns = [
    path('', views.myAccount),
    path('registerUser/', views.registerUser, name='registerUser'),
    path('registerDesigner/', views.registerDesigner, name='registerDesigner'),
    path('registerArchitect/', views.registerArchitect, name='registerArchitect'),
    path('registerBuilder/', views.registerBuilder, name='registerBuilder'),




    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('myAccount/', views.myAccount, name='myAccount'),
    path('custDashboard/', views.custDashboard, name='custDashboard'),
    path('designerDashboard/', views.designerDashboard, name='designerDashboard'),
    path('architectDashboard/', views.architectDashboard, name='architectDashboard'),
    path('builderDashboard/', views.builderDashboard, name='builderDashboard'),



    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password_validate/<uidb64>/<token>/', views.reset_password_validate, name='reset_password_validate'),
    path('reset_password/', views.reset_password, name='reset_password'),


    path('designer/', include('designer.urls')),
    path('customer/', include('customers.urls')),
    path('architect/', include('architects.urls')),
    path('builder/', include('builder.urls')),









]