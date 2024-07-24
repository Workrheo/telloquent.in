from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required , user_passes_test

from accounts.forms import UserInfoForm, UserProfileForm

from accounts.models import UserProfile , User
from designer.models import Designer 
from architects.models import Architect
from builder.models import Builder

from .models import Appointment , Checklist , Architect_Appointment , Builder_Appointment
from accounts.views import check_role_customer
from django.contrib import messages , auth
from .forms import ChecklistForm
import datetime









# Create your views here.
def get_customer(request):
    customer = User.objects.get(user=request.user)
    return customer

@login_required(login_url='login')
def cprofile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        user_form = UserInfoForm(request.POST, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, 'Profile updated')
            return redirect('cprofile')
        else:
            print(profile_form.errors)
            print(user_form.errors)
    else:
        profile_form = UserProfileForm(instance=profile)
        user_form = UserInfoForm(instance=request.user)

    context = {
        'profile_form': profile_form,
        'user_form' : user_form,
        'profile': profile,
    }
    return render(request, 'customers/cprofile.html', context)

@login_required(login_url='login')
@user_passes_test(check_role_customer)
def appointment(request, pid):
    designer = Designer.objects.get(id=pid)
    designer_detail = User.objects.get(user=designer)

    if request.method == "POST":
        a_date = request.POST['a_date']
        a_timing = request.POST['a_timing']

        app = Appointment.objects.create(
            designer=designer_detail, customer=request.user, a_date=a_date, a_timing=a_timing,
            status="pending", c_status="pending"
        )
        
        messages.success(request, 'Your appointment request sent Succesfully. Please wait for Appointment Confirmation.')
        return redirect('booking-success', app.id)

    context = {'designer': designer}
    return render(request, 'customers/appointment1.html', context)



def payment_success(request, pid):
    data = Appointment.objects.get(id=pid)
    context = {'data': data}
    return render(request, 'customers/booking-success.html', context)




def checklist_success(request, pid):
    data = Checklist.objects.get(id=pid)
    context = {'data': data}
    return render(request, 'customers/checklikst-success1.html', context)




def c_appointment(request):
    data = Appointment.objects.filter(customer=request.user, status="pending")
    context = {'data': data}
    return render(request, 'customers/c_appointment.html', context)




def cancel_appointment(request, pid):
    cus = Appointment.objects.get(id=pid)
    cus.delete()
    messages.success(request, 'Appointment Cancelled Successfully')
    return redirect('c_appointment')






def confirmed_c_appointment(request):
    tod = datetime.date.today()
    data = Appointment.objects.filter(customer=request.user, status="confirmed")
    context = {'data': data}
    return render(request, 'customers/confirmed_c_appointment' , context)



@login_required(login_url='login')
@user_passes_test(check_role_customer)
def checklist(request, pid):
    designer = Designer.objects.get(id=pid)
    designer_detail = User.objects.get(user=designer)

    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        project_category = request.POST.get('project_category')
        project_type = request.POST.get('project_type')

        # Kitchen Checklist Items
        kitchen_finish = request.POST.get('kitchen_finish')
        kitchen_countertop = request.POST.get('kitchen_countertop')
        kitchen_dado = request.POST.get('kitchen_dado')
        kitchen_loft = request.POST.get('kitchen_loft')

        utility = request.POST.get('utility')


        # Master Bedroom Checklist Items
        MBR_Wardrobe = request.POST.get('MBR_Wardrobe')
        MBR_COT = request.POST.get('MBR_COT')
        MBR_Reqs = request.POST.get('MBR_Reqs')


        # Kids Bedroom Checklist Items
        KBR_Wardrobe = request.POST.get('KBR_Wardrobe')
        KBR_COT = request.POST.get('KBR_COT')
        KBR_Reqs = request.POST.get('KBR_Reqs')

        # Guest Bedroom Checklist Items
        GBR_Wardrobe = request.POST.get('GBR_Wardrobe')
        GBR_COT = request.POST.get('GBR_COT')
        GBR_Reqs = request.POST.get('GBR_Reqs')


        Four_BR_Wardrobe = request.POST.get('Four_BR_Wardrobe')
        Four_BR_COT = request.POST.get('Four_BR_COT')
        Four_BR_Reqs = request.POST.get('Four_BR_Reqs')   

        Five_BR_Wardrobe = request.POST.get('Five_BR_Wardrobe')
        Five_BR_COT = request.POST.get('Five_BR_COT')
        Five_BR_Reqs = request.POST.get('Five_BR_Reqs')




        # Living Room Checklist Items
        Livingroom = request.POST.get('Livingroom')

        # Dining Room Checklist Items
        Diningroom = request.POST.get('Diningroom')

        # Washroom Checklist Items
        Washroom = request.POST.get('Washroom')

        # Foyer Checklist Items
        Foyer = request.POST.get('Foyer')

        Requirements = request.POST.get('Requirements')
        
        # Assuming you have a Checklist model with all these fields
        checklist = Checklist.objects.create(
            designer=designer_detail,
            customer=request.user,
            project_name=project_name,
            project_category=project_category,
            project_type=project_type,

            kitchen_finish=kitchen_finish,
            kitchen_countertop=kitchen_countertop,
            kitchen_dado=kitchen_dado,
            kitchen_loft=kitchen_loft,

            utility=utility,


            MBR_Wardrobe=MBR_Wardrobe,
            MBR_COT=MBR_COT,
            MBR_Reqs=MBR_Reqs,


            KBR_Wardrobe=KBR_Wardrobe,
            KBR_COT=KBR_COT,
            KBR_Reqs=KBR_Reqs,

            GBR_Wardrobe=GBR_Wardrobe,
            GBR_COT=GBR_COT,
            GBR_Reqs=GBR_Reqs,


            Four_BR_Wardrobe=Four_BR_Wardrobe,
            Four_BR_COT=Four_BR_COT,
            Four_BR_Reqs=Four_BR_Reqs,

            Five_BR_Wardrobe=Five_BR_Wardrobe,
            Five_BR_COT=Five_BR_COT,
            Five_BR_Reqs=Five_BR_Reqs,



            Livingroom=Livingroom,

            Diningroom=Diningroom,

            Washroom=Washroom,

            Foyer=Foyer,

            Requirements=Requirements,
        )

        messages.success(request, 'Your Checklist request sent Succesfully. Please wait for Estimate Confirmation.')
        return redirect('checklist-success', checklist.id)

    context = {'designer': designer}
    return render(request, 'customers/checklist1.html', context)




@login_required(login_url='login')
@user_passes_test(check_role_customer)
def architect_appointment(request, pid):
    architect = Architect.objects.get(id=pid)
    architect_detail = architect.user

    if request.method == "POST":
        a_date = request.POST['a_date']
        a_timing = request.POST['a_timing']

        app = Architect_Appointment.objects.create(
            architect=architect_detail, customer=request.user, a_date=a_date, a_timing=a_timing,
            status="pending", c_status="pending"
        )
        
        messages.success(request, 'Your appointment request sent Succesfully. Please wait for Appointment Confirmation.')
        return redirect('architect_booking-success', app.id)

    context = {'architect': architect}
    return render(request, 'customers/architect_appointment1.html', context)



def architect_payment_success(request, pid):
    data = Architect_Appointment.objects.get(id=pid)
    context = {'data': data}
    return render(request, 'customers/architect_booking-success.html', context)





def architect_c_appointment(request):
    data = Architect_Appointment.objects.filter(customer=request.user, status="pending")
    context = {'data': data}
    return render(request, 'customers/architect_c_appointment.html', context)




def architect_cancel_appointment(request, pid):
    cus = Architect_Appointment.objects.get(id=pid)
    cus.delete()
    messages.success(request, 'Appointment Cancelled Successfully')
    return redirect('architect_c_appointment')






def architect_confirmed_c_appointment(request):
    tod = datetime.date.today()
    data = Architect_Appointment.objects.filter(customer=request.user, status="confirmed")
    context = {'data': data}



    return render(request, 'customers/architect_confirmed_c_appointment' , context)


#---------------------------------------- Builder ----------------------------------------------#



@login_required(login_url='login')
@user_passes_test(check_role_customer)
def builder_appointment(request, pid):
    builder = Builder.objects.get(id=pid)
    builder_detail = builder.user

    if request.method == "POST":
        a_date = request.POST['a_date']
        a_timing = request.POST['a_timing']

        app = Builder_Appointment.objects.create(
            builder=builder_detail, customer=request.user, a_date=a_date, a_timing=a_timing,
            status="pending", c_status="pending"
        )
        
        messages.success(request, 'Your appointment request sent Succesfully. Please wait for Appointment Confirmation.')
        return redirect('builder_booking-success', app.id)

    context = {'builder': builder}
    return render(request, 'customers/builder_appointment1.html', context)



def builder_payment_success(request, pid):
    data = Builder_Appointment.objects.get(id=pid)
    context = {'data': data}
    return render(request, 'customers/builder_booking-success.html', context)





def builder_c_appointment(request):
    data = Builder_Appointment.objects.filter(customer=request.user, status="pending")
    context = {'data': data}
    return render(request, 'customers/builder_c_appointment.html', context)




def builder_cancel_appointment(request, pid):
    cus = Builder_Appointment.objects.get(id=pid)
    cus.delete()
    messages.success(request, 'Appointment Cancelled Successfully')
    return redirect('builderc_appointment')






def builder_confirmed_c_appointment(request):
    tod = datetime.date.today()
    data = Builder_Appointment.objects.filter(customer=request.user, status="confirmed")
    context = {'data': data}



    return render(request, 'customers/builder_confirmed_c_appointment' , context)




