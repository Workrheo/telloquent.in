from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse, JsonResponse

from django.db import IntegrityError
import datetime



from .forms import ArchitectForm , Architect_OpeningHourForm
from accounts.forms import UserProfileForm
from accounts.models import User, UserProfile
from .models import Architect , Architect_OpeningHour
from customers.models import Appointment , Checklist , Architect_Appointment

from django.contrib import messages
from django.contrib.auth.decorators import login_required , user_passes_test
from accounts.views import check_role_architect
from portfolio.models import Architect_Category , Architect_PortfolioItem

from portfolio.forms import Architect_CategoryForm, Architect_PortfolioItemForm
from django.template.defaultfilters import slugify
from customers.forms import AppointmentForm , ChecklistForm , Architect_AppointmentForm



# Create your views here.

def get_architect(request):
    architect = Architect.objects.get(user=request.user)
    return architect






@login_required(login_url='login')
@user_passes_test(check_role_architect)
def aprofile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    architect = get_object_or_404(Architect, user=request.user)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        architect_form = ArchitectForm(request.POST, request.FILES, instance=architect)
        if profile_form.is_valid() and architect_form.is_valid():
            profile_form.save()
            architect_form.save()
            messages.success(request, 'Profile updated.')
            return redirect('aprofile')
        else:
            print(profile_form.errors)
            print(architect_form.errors)
    else:
        profile_form = UserProfileForm(instance = profile)
        architect_form = ArchitectForm(instance = architect)    


    context = {
        'profile_form' : profile_form,
        'architect_form' : architect_form,
        'profile' : profile,
        'architect' : architect,
    }

    return render(request, 'architects/aprofile.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_architect)
def architect_portfolio_builder(request):
    architect = get_architect(request)
    categories = Architect_Category.objects.filter(architect=architect)
    context = {
        'categories': categories,
    }
    return render(request, 'architects/portfolio_builder.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_architect)
def architect_portfolioitems_by_category(request, pk=None):
    architect = get_architect(request)
    category = get_object_or_404(Architect_Category, pk=pk)
    portfolioitems = Architect_PortfolioItem.objects.filter(architect=architect, category=category)
    context = {
        'portfolioitems': portfolioitems,
        'category': category,
    }
    return render(request , 'architects/architect_portfolioitems_by_category.html' , context)


@login_required(login_url='login')
@user_passes_test(check_role_architect)
def architect_add_category(request):
    if request.method == 'POST':
        form = Architect_CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            category = form.save(commit=False)
            category.architect = get_architect(request)
            
            category.save() # here the category id will be generated
            category.slug = slugify(category_name)+'-'+str(category.id)
            category.save()
            messages.success(request, 'Category added successfully!')
            return redirect('architect_portfolio_builder')
        else:
            print(form.errors)

    else:
        form = Architect_CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'architects/arc_add_category.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_architect)
def architect_edit_category(request, pk=None):
    category = get_object_or_404(Architect_Category, pk=pk)
    if request.method == 'POST':
        form = Architect_CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            category = form.save(commit=False)
            category.architect = get_architect(request)
            category.slug = slugify(category_name)
            form.save()
            messages.success(request, 'Category updated successfully!')
            return redirect('architect_portfolio_builder')
        else:
            print(form.errors)

    else:
        form = Architect_CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'architects/arc_edit_category.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_architect)
def architect_delete_category(request, pk=None):
    category = get_object_or_404(Architect_Category, pk=pk)
    category.delete()
    messages.success(request, 'Category has been deleted successfully!')
    return redirect('architect_portfolio_builder')



@login_required(login_url='login')
@user_passes_test(check_role_architect)
def architect_add_portfolio(request):
    if request.method == 'POST':
        form = Architect_PortfolioItemForm(request.POST, request.FILES)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.architect = get_architect(request)
            form.save()
            messages.success(request, 'Portfolio Item added successfully!')
            return redirect('architect_portfolioitems_by_category', portfolio.category.id)
        else:
            print(form.errors)
    else:
        form = Architect_PortfolioItemForm()
        # modify this form
        form.fields['category'].queryset = Architect_Category.objects.filter(architect=get_architect(request))
    context = {
        'form': form,
    }
    return render(request, 'architects/architect_add_portfolio.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_architect)
def architect_edit_portfolio(request, pk=None):
    portfolio = get_object_or_404(Architect_PortfolioItem, pk=pk)
    if request.method == 'POST':
        form = Architect_PortfolioItemForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.architect = get_architect(request)
            form.save()
            messages.success(request, 'Portfolio Item updated successfully!')
            return redirect('architect_portfolioitems_by_category', portfolio.category.id)
        else:
            print(form.errors)

    else:
        form = Architect_PortfolioItemForm(instance=portfolio)
        form.fields['category'].queryset = Architect_Category.objects.filter(architect=get_architect(request))
    context = {
        'form': form,
        'portfolio': portfolio,
    }
    return render(request, 'architects/architect_edit_portfolio.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_architect)
def architect_delete_portfolio(request, pk=None):
    portfolio = get_object_or_404( Architect_PortfolioItem, pk=pk)
    portfolio.delete()
    messages.success(request, 'portfolio Item has been deleted successfully!')
    return redirect('architect_portfolioitems_by_category', portfolio.category.id)




def architect_opening_hours(request):
    opening_hours = Architect_OpeningHour.objects.filter(architect=get_architect(request))
    form = Architect_OpeningHourForm()
    context = {
        'form': form,
        'opening_hours': opening_hours,
    }
    return render(request, 'architects/architect_opening_hours.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_architect)
def architect_add_opening_hours(request):
    if request.method == 'POST':
        form = Architect_OpeningHourForm(request.POST, request.FILES)
        if form.is_valid():
            day = form.cleaned_data['day']
            opening_hours = form.save(commit=False)
            opening_hours.architect = get_architect(request)
            form.save()
            messages.success(request, 'Opening Hours added successfully!')
            return redirect('architect_opening_hours' )
        else:
            print(form.errors)
    else:
        form = Architect_OpeningHourForm()
        # modify this form
        #form.fields['category'].queryset = Category.objects.filter(architect=get_architect(request))
    context = {
        'form': form,
    }
    return render(request, 'architects/architect_add_opening_hours.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_architect)
def architect_edit_opening_hours(request, pk=None):
    opening_hours = get_object_or_404(Architect_OpeningHour, pk=pk)
    if request.method == 'POST':
        form = Architect_OpeningHourForm(request.POST, request.FILES, instance=opening_hours)
        if form.is_valid():
            day = form.cleaned_data['day']
            opening_hours = form.save(commit=False)
            opening_hours.architect = get_architect(request)
            form.save()
            messages.success(request, 'Timings updated successfully!')
            return redirect('architect_opening_hours')
        else:
            print(form.errors)

    else:
        form = Architect_OpeningHourForm(instance=opening_hours)
        #form.fields['category'].queryset = Category.objects.filter(architect=get_architect(request))
    context = {
        'form': form,
        'opening_hours': opening_hours,
    }
    return render(request, 'architects/architect_edit_opening_hours.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_architect)
def architect_delete_opening_hours(request, pk=None):
    opening_hours = get_object_or_404( Architect_OpeningHour, pk=pk)
    opening_hours.delete()
    messages.success(request, 'Timings has been deleted successfully!')
    return redirect('architect_opening_hours')
        


@login_required(login_url='login')
@user_passes_test(check_role_architect)
def a_appointment(request):
    data = Architect_Appointment.objects.filter(architect=request.user, status="pending")
    context = {'data': data}
    return render(request, 'architects/a_appointment.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_architect)
def architect_update_status(request, pid):
    
    data = Architect_Appointment.objects.get(id=pid)
    form = Architect_AppointmentForm(request.POST or None, instance=data)
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
    return render(request, 'architects/architect_update_status.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_architect)
def architect_cancel_appointment(request, pid):
    cus = Architect_Appointment.objects.get(id=pid)
    cus.delete()
    messages.success(request, 'Appointment Cancelled Successfully')
    return redirect('a_appointment')





@login_required(login_url='login')
@user_passes_test(check_role_architect)
def confirmed_a_appointment(request):
    today = datetime.date.today()
    data = Architect_Appointment.objects.filter(architect=request.user, status="confirmed")
    context = {'data': data}
    return render(request, 'architects/confirmed_a_appointment.html', context)





