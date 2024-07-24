from django.shortcuts import render ,redirect
from .forms import UserForm
from designer.forms import DesignerForm 
from architects.forms import ArchitectForm 
from builder.forms import BuilderForm

from .models import User , UserProfile
from django.http.response import HttpResponse
from django.contrib import messages , auth
from .utils import detectUser , send_verification_email
from django.contrib.auth.decorators import login_required , user_passes_test
from django.core.exceptions import PermissionDenied
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.template.defaultfilters import slugify
from designer.models import Designer
from customers.models import Appointment , Architect_Appointment , Builder_Appointment
import datetime






# Create your views here.


# Restrict the Designer from accessing the customer page
def check_role_designer(user):
    if user.role == 1:
        return True
    else:
        raise PermissionDenied


# Restrict the customer from accessing the designer page
def check_role_customer(user):
    if user.role == 2:
        return True
    else:
        raise PermissionDenied
    


# Restrict the customer from accessing the Architect page
def check_role_architect(user):
    if user.role == 3:
        return True
    else:
        raise PermissionDenied
    

def check_role_builder(user):
    if user.role == 4:
        return True
    else:
        raise PermissionDenied

def registerUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Create the user using the form
            # password = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # user.save()

            # Create the user using create_user method
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.CUSTOMER
            user.save()
            mail_subject = 'Please activate your account'
            email_template = 'accounts/emails/account_verification_email.html'
            send_verification_email(request, user, mail_subject, email_template)
            messages.success(request, 'Your account has been registered succesfully')
            return redirect('registerUser')


    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/registerUser.html', context)


def registerDesigner(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        d_form = DesignerForm(request.POST , request.FILES)

        if form.is_valid() and d_form.is_valid:

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.DESIGNER
            user.save()
            designer = d_form.save(commit=False)
            designer.user = user
            designer_name = d_form.cleaned_data['designer_name']
            designer.designer_slug = slugify(designer_name)+'-'+str(user.id)
            user_profile = UserProfile.objects.get(user=user)
            designer.user_profile = user_profile
            designer.save()
            mail_subject = 'Please activate your account'
            email_template = 'accounts/emails/account_verification_email.html'
            send_verification_email(request, user, mail_subject, email_template)
            messages.success(request, 'Your account has been registered succesfully! Please wait for approval.')
            return redirect('login')
        else:
            print('invalid form')
            print(form.errors)
    else:
        form = UserForm()
        d_form = DesignerForm()




    context = {
        'form' : form ,
        'd_form' : d_form ,
    }
    
    return render(request, 'accounts/registerDesigner1.html' , context)


def registerArchitect(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        a_form = ArchitectForm(request.POST , request.FILES)

        if form.is_valid() and a_form.is_valid:

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.ARCHITECT
            user.save()
            architect = a_form.save(commit=False)
            architect.user = user
            architect_name = a_form.cleaned_data['architect_name']
            architect.architect_slug = slugify(architect_name)+'-'+str(user.id)
            user_profile = UserProfile.objects.get(user=user)
            architect.user_profile = user_profile
            architect.save()
            mail_subject = 'Please activate your account'
            email_template = 'accounts/emails/account_verification_email.html'
            send_verification_email(request, user, mail_subject, email_template)
            messages.success(request, 'Your account has been registered succesfully! Please wait for approval.')
            return redirect('login')
        else:
            print('invalid form')
            print(form.errors)
    else:
        form = UserForm()
        a_form = ArchitectForm()




    context = {
        'form' : form ,
        'a_form' : a_form ,
    }
    
    return render(request, 'accounts/registerArchitect.html' , context)



def registerBuilder(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        b_form = BuilderForm(request.POST , request.FILES)

        if form.is_valid() and b_form.is_valid:

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.BUILDER
            user.save()
            builder = b_form.save(commit=False)
            builder.user = user
            builder_name = b_form.cleaned_data['builder_name']
            builder.architect_slug = slugify(builder_name)+'-'+str(user.id)
            user_profile = UserProfile.objects.get(user=user)
            builder.user_profile = user_profile
            builder.save()
            mail_subject = 'Please activate your account'
            email_template = 'accounts/emails/account_verification_email.html'
            send_verification_email(request, user, mail_subject, email_template)
            messages.success(request, 'Your account has been registered succesfully! Please wait for approval.')
            return redirect('login')
        else:
            print('invalid form')
            print(form.errors)
    else:
        form = UserForm()
        b_form = BuilderForm()




    context = {
        'form' : form ,
        'b_form' : b_form ,
    }
    
    return render(request, 'accounts/registerBuilder.html' , context)


def activate(request , uidb64 , token):
    # Activate the user by setting the is_active status to True
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulation! Your account is activated.')
        return redirect('myAccount')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('myAccount')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            if 'next' in request.POST:
                messages.success(request, 'Logged in Successfully')
                return redirect(request.POST.get('next'))
            else:
                messages.success(request, 'Your logged in')
                return redirect('myAccount')

        else:
            messages.error(request, 'Invalid Login credentials')
            return redirect('login')
        
    return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    messages.info(request, 'Youre logged out')
    return redirect('login')


@login_required(login_url='login')
def myAccount(request):
    user = request.user
    redirectUrl = detectUser(user)
    return redirect(redirectUrl)


@login_required(login_url='login')
@user_passes_test(check_role_customer)
def custDashboard(request):
    tod = datetime.date.today()
    customer = Appointment.objects.filter(customer=request.user)
    pending = Appointment.objects.filter(customer=request.user, status="pending")
    count = Appointment.objects.filter(customer=request.user).count()
    upcoming = Appointment.objects.filter(customer=request.user, a_date__gte=tod).exclude(
        a_date=tod)
    today = Appointment.objects.filter(customer=request.user, a_date=tod)
    t_today = today.count()
    t_pending = pending.count()
    context = {'data': customer, 'total': count, 'up': upcoming, 'today': today, 't_today': t_today,
               't_pending': t_pending}
    return render(request, 'accounts/custdashboard.html')





@login_required(login_url='login')
@user_passes_test(check_role_designer)
def designerDashboard(request):
    tod = datetime.date.today()
    designer = Appointment.objects.filter(designer=request.user)
    pending = Appointment.objects.filter(designer=request.user, status="pending")
    count = Appointment.objects.filter(designer=request.user).count()
    upcoming = Appointment.objects.filter(designer=request.user, a_date__gte=tod).exclude(
        a_date=tod)
    today = Appointment.objects.filter(designer=request.user, a_date=tod)
    t_today = today.count()
    t_pending = pending.count()
    context = {'data': designer, 'total': count, 'up': upcoming, 'today': today, 't_today': t_today,
               't_pending': t_pending}

    return render(request, 'accounts/designerdashboard.html' , context)



@login_required(login_url='login')
@user_passes_test(check_role_architect)
def architectDashboard(request):
    tod = datetime.date.today()
    architect = Architect_Appointment.objects.filter(architect=request.user)
    pending = Architect_Appointment.objects.filter(architect=request.user, status="pending")
    count = Architect_Appointment.objects.filter(architect=request.user).count()
    upcoming = Architect_Appointment.objects.filter(architect=request.user, a_date__gte=tod).exclude(
        a_date=tod)
    today = Architect_Appointment.objects.filter(architect=request.user, a_date=tod)
    t_today = today.count()
    t_pending = pending.count()
    context = {'data': architect, 'total': count, 'up': upcoming, 'today': today, 't_today': t_today,
               't_pending': t_pending}
    

    return render(request, 'architects/architectdashboard.html' , context)



@login_required(login_url='login')
@user_passes_test(check_role_builder)
def builderDashboard(request):
    tod = datetime.date.today()
    builder = Builder_Appointment.objects.filter(builder=request.user)
    pending = Builder_Appointment.objects.filter(builder=request.user, status="pending")
    count = Builder_Appointment.objects.filter(builder=request.user).count()
    upcoming = Builder_Appointment.objects.filter(builder=request.user, a_date__gte=tod).exclude(
        a_date=tod)
    today = Builder_Appointment.objects.filter(builder=request.user, a_date=tod)
    t_today = today.count()
    t_pending = pending.count()
    context = {'data': builder, 'total': count, 'up': upcoming, 'today': today, 't_today': t_today,
               't_pending': t_pending}
    
    

    return render(request, 'builder/builderdashboard.html' , context)





    



def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact=email)

            # send reset password email
            mail_subject = 'Reset Your Password'
            email_template = 'accounts/emails/reset_password_email.html'
            send_verification_email(request, user, mail_subject, email_template)

            messages.success(request, 'Password reset link has been sent to your email address.')
            return redirect('login')
        else:
            messages.error(request, 'Account does not exist')
            return redirect('forgot_password')
    return render(request, 'accounts/forgot_password.html')



def reset_password_validate(request, uidb64, token):
    # validate the user by decoding the token and user pk
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.info(request, 'Please reset your password')
        return redirect('reset_password')
    else:
        messages.error(request, 'This link has been expired!')
        return redirect('myAccount')


def reset_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            pk = request.session.get('uid')
            user = User.objects.get(pk=pk)
            user.set_password(password)
            user.is_active = True
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('login')
        else:
            messages.error(request, 'Password do not match!')
            return redirect('reset_password')
    return render(request, 'accounts/reset_password.html')




