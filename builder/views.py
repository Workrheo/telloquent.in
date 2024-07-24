from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse, JsonResponse

from django.db import IntegrityError
import datetime



from .forms import BuilderForm , Builder_OpeningHourForm
from accounts.forms import UserProfileForm
from accounts.models import User, UserProfile
from .models import Builder , Builder_OpeningHour
from customers.models import Appointment , Checklist , Builder_Appointment

from django.contrib import messages
from django.contrib.auth.decorators import login_required , user_passes_test
from accounts.views import check_role_builder
from portfolio.models import Builder_Category , Builder_PortfolioItem

from portfolio.forms import Builder_CategoryForm, Builder_PortfolioItemForm
from django.template.defaultfilters import slugify
from customers.forms import AppointmentForm , ChecklistForm , Builder_AppointmentForm



# Create your views here.

def get_builder(request):
    builder= Builder.objects.get(user=request.user)
    return builder






@login_required(login_url='login')
@user_passes_test(check_role_builder)
def bprofile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    builder = get_object_or_404(Builder, user=request.user)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        builder_form = BuilderForm(request.POST, request.FILES, instance=builder)
        if profile_form.is_valid() and builder_form.is_valid():
            profile_form.save()
            builder_form.save()
            messages.success(request, 'Profile updated.')
            return redirect('bprofile')
        else:
            print(profile_form.errors)
            print(builder_form.errors)
    else:
        profile_form = UserProfileForm(instance = profile)
        builder_form = BuilderForm(instance = builder)    


    context = {
        'profile_form' : profile_form,
        'builder_form' : builder_form,
        'profile' : profile,
        'builder' : builder,
    }

    return render(request, 'builder/bprofile.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_builder)
def builder_portfolio_builder(request):
    builder = get_builder(request)
    categories = Builder_Category.objects.filter(builder=builder)
    context = {
        'categories': categories,
    }
    return render(request, 'builder/portfolio_builder.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_builder)
def builder_portfolioitems_by_category(request, pk=None):
    builder = get_builder(request)
    category = get_object_or_404(Builder_Category, pk=pk)
    portfolioitems = Builder_PortfolioItem.objects.filter(builder=builder, category=category)
    context = {
        'portfolioitems': portfolioitems,
        'category': category,
    }
    return render(request , 'builder/builder_portfolioitems_by_category.html' , context)


@login_required(login_url='login')
@user_passes_test(check_role_builder)
def builder_add_category(request):
    if request.method == 'POST':
        form = Builder_CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            category = form.save(commit=False)
            category.builder = get_builder(request)
            
            category.save() # here the category id will be generated
            category.slug = slugify(category_name)+'-'+str(category.id)
            category.save()
            messages.success(request, 'Category added successfully!')
            return redirect('builder_portfolio_builder')
        else:
            print(form.errors)

    else:
        form = Builder_CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'builder/builder_add_category.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_builder)
def builder_edit_category(request, pk=None):
    category = get_object_or_404(Builder_Category, pk=pk)
    if request.method == 'POST':
        form = Builder_CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            category = form.save(commit=False)
            category.builder = get_builder(request)
            category.slug = slugify(category_name)
            form.save()
            messages.success(request, 'Category updated successfully!')
            return redirect('builder_portfolio_builder')
        else:
            print(form.errors)

    else:
        form = Builder_CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'builder/builder_edit_category.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_builder)
def builder_delete_category(request, pk=None):
    category = get_object_or_404(Builder_Category, pk=pk)
    category.delete()
    messages.success(request, 'Category has been deleted successfully!')
    return redirect('builder_portfolio_builder')



@login_required(login_url='login')
@user_passes_test(check_role_builder)
def builder_add_portfolio(request):
    if request.method == 'POST':
        form = Builder_PortfolioItemForm(request.POST, request.FILES)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.builder = get_builder(request)
            form.save()
            messages.success(request, 'Portfolio Item added successfully!')
            return redirect('builder_portfolioitems_by_category', portfolio.category.id)
        else:
            print(form.errors)
    else:
        form = Builder_PortfolioItemForm()
        # modify this form
        form.fields['category'].queryset = Builder_Category.objects.filter(builder=get_builder(request))
    context = {
        'form': form,
    }
    return render(request, 'builder/builder_add_portfolio.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_builder)
def builder_edit_portfolio(request, pk=None):
    portfolio = get_object_or_404(Builder_PortfolioItem, pk=pk)
    if request.method == 'POST':
        form = Builder_PortfolioItemForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.builder = get_builder(request)
            form.save()
            messages.success(request, 'Portfolio Item updated successfully!')
            return redirect('builder_portfolioitems_by_category', portfolio.category.id)
        else:
            print(form.errors)

    else:
        form = Builder_PortfolioItemForm(instance=portfolio)
        form.fields['category'].queryset = Builder_Category.objects.filter(builder=get_builder(request))
    context = {
        'form': form,
        'portfolio': portfolio,
    }
    return render(request, 'builder/builder_edit_portfolio.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_builder)
def builder_delete_portfolio(request, pk=None):
    portfolio = get_object_or_404( Builder_PortfolioItem, pk=pk)
    portfolio.delete()
    messages.success(request, 'portfolio Item has been deleted successfully!')
    return redirect('builder_portfolioitems_by_category', portfolio.category.id)




def builder_opening_hours(request):
    opening_hours = Builder_OpeningHour.objects.filter(builder=get_builder(request))
    form = Builder_OpeningHourForm()
    context = {
        'form': form,
        'opening_hours': opening_hours,
    }
    return render(request, 'builder/builder_opening_hours.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_builder)
def builder_add_opening_hours(request):
    if request.method == 'POST':
        form = Builder_OpeningHourForm(request.POST, request.FILES)
        if form.is_valid():
            day = form.cleaned_data['day']
            opening_hours = form.save(commit=False)
            opening_hours.builder = get_builder(request)
            form.save()
            messages.success(request, 'Opening Hours added successfully!')
            return redirect('builder_opening_hours' )
        else:
            print(form.errors)
    else:
        form = Builder_OpeningHourForm()
        # modify this form
        #form.fields['category'].queryset = Category.objects.filter(builder=get_builder(request))
    context = {
        'form': form,
    }
    return render(request, 'builder/builder_add_opening_hours.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_builder)
def builder_edit_opening_hours(request, pk=None):
    opening_hours = get_object_or_404(Builder_OpeningHour, pk=pk)
    if request.method == 'POST':
        form = Builder_OpeningHourForm(request.POST, request.FILES, instance=opening_hours)
        if form.is_valid():
            day = form.cleaned_data['day']
            opening_hours = form.save(commit=False)
            opening_hours.builder = get_builder(request)
            form.save()
            messages.success(request, 'Timings updated successfully!')
            return redirect('builder_opening_hours')
        else:
            print(form.errors)

    else:
        form = Builder_OpeningHourForm(instance=opening_hours)
        #form.fields['category'].queryset = Category.objects.filter(builder=get_builder(request))
    context = {
        'form': form,
        'opening_hours': opening_hours,
    }
    return render(request, 'builder/builder_edit_opening_hours.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_builder)
def builder_delete_opening_hours(request, pk=None):
    opening_hours = get_object_or_404( Builder_OpeningHour, pk=pk)
    opening_hours.delete()
    messages.success(request, 'Timings has been deleted successfully!')
    return redirect('builder_opening_hours')
        


@login_required(login_url='login')
@user_passes_test(check_role_builder)
def b_appointment(request):
    data = Builder_Appointment.objects.filter(builder=request.user, status="pending")
    context = {'data': data}
    return render(request, 'builder/b_appointment.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_builder)
def builder_update_status(request, pid):
    
    data = Builder_Appointment.objects.get(id=pid)
    form = Builder_AppointmentForm(request.POST or None, instance=data)
    if request.method == "POST":
        u = request.POST['a_date']
        v = request.POST['a_timing']
        data.a_date = u
        data.a_timing = v
        data.status = "confirmed"
        data.save()
        messages.success(request, "Appointment status updated Successfully")
        return redirect('a_appointment')
    context = {'form': form, 'data': data}
    return render(request, 'builder/builder_update_status.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_builder)
def builder_cancel_appointment(request, pid):
    cus = Builder_Appointment.objects.get(id=pid)
    cus.delete()
    messages.success(request, 'Appointment Cancelled Successfully')
    return redirect('b_appointment')





@login_required(login_url='login')
@user_passes_test(check_role_builder)
def confirmed_b_appointment(request):
    today = datetime.date.today()
    data = Builder_Appointment.objects.filter(builder=request.user, status="confirmed")
    context = {'data': data}
    return render(request, 'builder/confirmed_b_appointment.html', context)





