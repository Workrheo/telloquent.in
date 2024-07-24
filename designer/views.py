from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse, JsonResponse

from django.db import IntegrityError
import datetime



from .forms import DesignerForm , OpeningHourForm
from accounts.forms import UserProfileForm
from accounts.models import User, UserProfile
from .models import Designer , OpeningHour
from customers.models import Appointment , Checklist 

from django.contrib import messages
from django.contrib.auth.decorators import login_required , user_passes_test
from accounts.views import check_role_designer
from portfolio.models import Category , PortfolioItem

from portfolio.forms import CategoryForm, PortfolioItemForm
from django.template.defaultfilters import slugify
from customers.forms import AppointmentForm , ChecklistForm



# Create your views here.

def get_designer(request):
    designer = Designer.objects.get(user=request.user)
    return designer






@login_required(login_url='login')
@user_passes_test(check_role_designer)
def dprofile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    designer = get_object_or_404(Designer, user=request.user)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        designer_form = DesignerForm(request.POST, request.FILES, instance=designer)
        if profile_form.is_valid() and designer_form.is_valid():
            profile_form.save()
            designer_form.save()
            messages.success(request, 'Profile updated.')
            return redirect('dprofile')
        else:
            print(profile_form.errors)
            print(designer_form.errors)
    else:
        profile_form = UserProfileForm(instance = profile)
        designer_form = DesignerForm(instance = designer)    


    context = {
        'profile_form' : profile_form,
        'designer_form' : designer_form,
        'profile' : profile,
        'designer' : designer,
    }

    return render(request, 'designer/dprofile.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_designer)
def portfolio_builder(request):
    designer = get_designer(request)
    categories = Category.objects.filter(designer=designer)
    context = {
        'categories': categories,
    }
    return render(request, 'designer/portfolio_builder.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_designer)
def portfolioitems_by_category(request, pk=None):
    designer = get_designer(request)
    category = get_object_or_404(Category , pk=pk)
    portfolioitems = PortfolioItem.objects.filter(designer=designer, category=category)
    context = {
        'portfolioitems': portfolioitems,
        'category': category,
    }
    return render(request , 'designer/portfolioitems_by_category.html' , context)


@login_required(login_url='login')
@user_passes_test(check_role_designer)
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            category = form.save(commit=False)
            category.designer = get_designer(request)
            
            category.save() # here the category id will be generated
            category.slug = slugify(category_name)+'-'+str(category.id)
            category.save()
            messages.success(request, 'Category added successfully!')
            return redirect('portfolio_builder')
        else:
            print(form.errors)

    else:
        form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'designer/add_category.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_designer)
def edit_category(request, pk=None):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            category = form.save(commit=False)
            category.designer = get_designer(request)
            category.slug = slugify(category_name)
            form.save()
            messages.success(request, 'Category updated successfully!')
            return redirect('portfolio_builder')
        else:
            print(form.errors)

    else:
        form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'designer/edit_category.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_designer)
def delete_category(request, pk=None):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    messages.success(request, 'Category has been deleted successfully!')
    return redirect('portfolio_builder')



@login_required(login_url='login')
@user_passes_test(check_role_designer)
def add_portfolio(request):
    if request.method == 'POST':
        form = PortfolioItemForm(request.POST, request.FILES)
        if form.is_valid():
            projecttitle = form.cleaned_data['project_title']
            portfolio = form.save(commit=False)
            portfolio.designer = get_designer(request)
            portfolio.slug = slugify(projecttitle)
            form.save()
            messages.success(request, 'Portfolio Item added successfully!')
            return redirect('portfolioitems_by_category', portfolio.category.id)
        else:
            print(form.errors)
    else:
        form = PortfolioItemForm()
        # modify this form
        form.fields['category'].queryset = Category.objects.filter(designer=get_designer(request))
    context = {
        'form': form,
    }
    return render(request, 'designer/add_portfolio.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_designer)
def edit_portfolio(request, pk=None):
    portfolio = get_object_or_404(PortfolioItem, pk=pk)
    if request.method == 'POST':
        form = PortfolioItemForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            projecttitle = form.cleaned_data['project_title']
            portfolio = form.save(commit=False)
            portfolio.designer = get_designer(request)
            portfolio.slug = slugify(projecttitle)
            form.save()
            messages.success(request, 'Portfolio Item updated successfully!')
            return redirect('portfolioitems_by_category', portfolio.category.id)
        else:
            print(form.errors)

    else:
        form = PortfolioItemForm(instance=portfolio)
        form.fields['category'].queryset = Category.objects.filter(designer=get_designer(request))
    context = {
        'form': form,
        'portfolio': portfolio,
    }
    return render(request, 'designer/edit_portfolio.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_designer)
def delete_portfolio(request, pk=None):
    portfolio = get_object_or_404( PortfolioItem, pk=pk)
    portfolio.delete()
    messages.success(request, 'portfolio Item has been deleted successfully!')
    return redirect('portfolioitems_by_category', portfolio.category.id)




def opening_hours(request):
    opening_hours = OpeningHour.objects.filter(designer=get_designer(request))
    form = OpeningHourForm()
    context = {
        'form': form,
        'opening_hours': opening_hours,
    }
    return render(request, 'designer/opening_hours.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_designer)
def add_opening_hours(request):
    if request.method == 'POST':
        form = OpeningHourForm(request.POST, request.FILES)
        if form.is_valid():
            day = form.cleaned_data['day']
            opening_hours = form.save(commit=False)
            opening_hours.designer = get_designer(request)
            form.save()
            messages.success(request, 'Opening Hours added successfully!')
            return redirect('opening_hours' )
        else:
            print(form.errors)
    else:
        form = OpeningHourForm()
        # modify this form
        #form.fields['category'].queryset = Category.objects.filter(designer=get_designer(request))
    context = {
        'form': form,
    }
    return render(request, 'designer/add_opening_hours.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_designer)
def edit_opening_hours(request, pk=None):
    opening_hours = get_object_or_404(OpeningHour, pk=pk)
    if request.method == 'POST':
        form = OpeningHourForm(request.POST, request.FILES, instance=opening_hours)
        if form.is_valid():
            day = form.cleaned_data['day']
            opening_hours = form.save(commit=False)
            opening_hours.designer = get_designer(request)
            form.save()
            messages.success(request, 'Timings updated successfully!')
            return redirect('opening_hours')
        else:
            print(form.errors)

    else:
        form = OpeningHourForm(instance=opening_hours)
        #form.fields['category'].queryset = Category.objects.filter(designer=get_designer(request))
    context = {
        'form': form,
        'opening_hours': opening_hours,
    }
    return render(request, 'designer/edit_opening_hours.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_designer)
def delete_opening_hours(request, pk=None):
    opening_hours = get_object_or_404( OpeningHour, pk=pk)
    opening_hours.delete()
    messages.success(request, 'Timings has been deleted successfully!')
    return redirect('opening_hours')
        


@login_required(login_url='login')
@user_passes_test(check_role_designer)
def d_appointment(request):
    data = Appointment.objects.filter(designer=request.user, status="pending")
    context = {'data': data}
    return render(request, 'Designer/d_appointment.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_designer)
def update_status(request, pid):
    
    data = Appointment.objects.get(id=pid)
    form = AppointmentForm(request.POST or None, instance=data)
    if request.method == "POST":
        u = request.POST['a_date']
        v = request.POST['a_timing']
        data.a_date = u
        data.a_timing = v
        data.status = "confirmed"
        data.save()
        messages.success(request, "Appointment status updated Successfully")
        return redirect('d_appointment')
    context = {'form': form, 'data': data}
    return render(request, 'Designer/update_status.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_designer)
def designer_cancel_appointment(request, pid):
    cus = Appointment.objects.get(id=pid)
    cus.delete()
    messages.success(request, 'Appointment Cancelled Successfully')
    return redirect('d_appointment')





@login_required(login_url='login')
@user_passes_test(check_role_designer)
def confirmed_d_appointment(request):
    today = datetime.date.today()
    data = Appointment.objects.filter(designer=request.user, status="confirmed")
    context = {'data': data}
    return render(request, 'Designer/confirmed_d_appointment.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_designer)
def d_checklist(request):
    data = Checklist.objects.filter(designer=request.user)
    context = {'data': data}
    return render(request, 'Designer/d_checklist.html', context)


def checklist_status(request, pid):
    
    data = Checklist.objects.get(id=pid)
    form = ChecklistForm(instance=data)
    
    context = {'data': data , 'form':form}
    return render(request, 'Designer/checklist_status.html', context)

