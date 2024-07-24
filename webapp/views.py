from django.shortcuts import get_object_or_404, redirect, render
from designer.models import Designer , OpeningHour , OfficeImages , ProjectImages
from architects.models import Architect , Architect_OfficeImages , Architect_OpeningHour , Architect_ProjectImages
from builder.models import Builder, Builder_OfficeImages , Builder_OpeningHour , Builder_ProjectImages
from portfolio.models import Category, PortfolioItem , Architect_Category , Architect_PortfolioItem , Builder_Category , Builder_PortfolioItem
from django.db.models import Prefetch
from datetime import date, datetime
from .models import Client , Testimonial , Ad_image , ContactDetails
from django.core.mail import send_mail as sm 
from django.core.mail import BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm





# Create your views here.

def home(request):
    client_list = Client.objects.all()
    testimonials = Testimonial.objects.all()
    
    designers = Designer.objects.filter(is_approved=True, user__is_active=True)
    architects = Architect.objects.filter(is_approved=True, user__is_active=True)
    builder = Builder.objects.filter(is_approved=True, user__is_active=True)


    builder_count = builder.count()    
    designer_count = designers.count()
    architect_count = architects.count()




    
    context = { 'client_list' : client_list ,
                'designers' : designers ,
                'designer_count' : designer_count ,
                'testimonials' : testimonials ,
                'architects': architects ,
                'architect_count' : architect_count ,
                'builder' : builder,
                'builder_count' : builder_count, 


    }
    return render(request, 'Webapp/index.html' , context)







def services(request):
    return render(request, 'Webapp/services.html')


def pricing(request):
    return render(request, 'Webapp/pricing.html')

def about(request):
    client_list = Client.objects.all()
    testimonials = Testimonial.objects.all()
    
    



    
    context = { 'client_list' : client_list ,
                'testimonials' : testimonials ,
    }
    return render(request, 'Webapp/about.html' , context)


def subs_sucess(request):
    return render(request, 'Webapp/subs_sucess.html')


def subs_cancel(request):
    return render(request, 'Webapp/subs_cancel.html')  



def subs_failed(request):
    return render(request, 'Webapp/subs_failed.html')




def designer_list(request):
    designers = Designer.objects.filter(is_approved=True, user__is_active=True)
    designer_count = designers.count()

    ads = Ad_image.objects.all()

    context = {
        'designers': designers,
        'designer_count': designer_count,
        'ads' : ads ,

    }
    return render(request, 'Webapp/listing.html', context)



def designer_detail(request, designer_slug):
    designer = get_object_or_404(Designer, designer_slug=designer_slug)
    project_images = ProjectImages.objects.filter(designer=designer)
    #opening_hours = OpeningHour.objects.filter(designer=designer)
    designer_office_images = OfficeImages.objects.filter(designer=designer)


    categories = Category.objects.filter(designer=designer).prefetch_related(
        Prefetch(
            'portfolioitems',
            queryset = PortfolioItem.objects.filter(is_available=True)
        )
    )

    opening_hours = OpeningHour.objects.filter(designer=designer).order_by('day', 'from_hour')
    
    # Check current day's opening hours.
    today_date = date.today()
    today = today_date.isoweekday()
    
    current_opening_hours = OpeningHour.objects.filter(designer=designer, day=today)
    #if request.user.is_authenticated:
        #cart_items = Cart.objects.filter(user=request.user)
    #else:
        #cart_items = None
    context = {
        'designer': designer,
        'categories': categories,
        'project_images' : project_images,
        'opening_hours': opening_hours ,
        'designer_office_images' : designer_office_images ,
        #'cart_items': cart_items,
        'current_opening_hours': current_opening_hours,
    }
    return render(request, 'Webapp/detail.html', context)



def architect_list(request):
    architects = Architect.objects.filter(is_approved=True, user__is_active=True)
    architect_count = architects.count()

    ads = Ad_image.objects.all()

    context = {
        'architects': architects,
        'architect_count': architect_count,
        'ads' : ads ,

    }
    return render(request, 'Webapp/architect_listing.html', context)



def architect_detail(request, architect_slug):
    architect = get_object_or_404(Architect, architect_slug=architect_slug)
    project_images = Architect_ProjectImages.objects.filter(architect=architect)
    architect_office_images = Architect_OfficeImages.objects.filter(architect=architect)


    categories = Architect_Category.objects.filter(architect=architect).prefetch_related(
        Prefetch(
            'architect_portfolioitems',
            queryset = Architect_PortfolioItem.objects.filter(is_available=True)
        )
    )

    opening_hours = Architect_OpeningHour.objects.filter(architect=architect).order_by('day', 'from_hour')
    
    # Check current day's opening hours.
    today_date = date.today()
    today = today_date.isoweekday()
    
    current_opening_hours = Architect_OpeningHour.objects.filter(architect=architect, day=today)
    #if request.user.is_authenticated:
        #cart_items = Cart.objects.filter(user=request.user)
    #else:
        #cart_items = None
    context = {
        'architect': architect,
        'categories': categories,
        'project_images' : project_images,
        'opening_hours': opening_hours ,
        'architect_office_images' : architect_office_images ,
        #'cart_items': cart_items,
        'current_opening_hours': current_opening_hours,
    }
    return render(request, 'Webapp/architect_detail.html', context)





def builder_list(request):
    builder = Builder.objects.filter(is_approved=True, user__is_active=True)
    builder_count = builder.count()

    ads = Ad_image.objects.all()

    context = {
        'builder': builder,
        'builder_count': builder_count,
        'ads' : ads ,

    }
    return render(request, 'Webapp/prop_listing.html', context)




def builder_detail(request, builder_slug):
    builder = get_object_or_404(Builder, builder_slug=builder_slug)
    project_images = Builder_ProjectImages.objects.filter(builder=builder)
    builder_office_images = Builder_OfficeImages.objects.filter(builder=builder)


    categories = Builder_Category.objects.filter(builder=builder).prefetch_related(
        Prefetch(
            'builder_portfolioitems',
            queryset = Builder_PortfolioItem.objects.filter(is_available=True)
        )
    )

    opening_hours = Builder_OpeningHour.objects.filter(builder=builder).order_by('day', 'from_hour')
    
    # Check current day's opening hours.
    today_date = date.today()
    today = today_date.isoweekday()
    
    current_opening_hours = Builder_OpeningHour.objects.filter(builder=builder, day=today)
    #if request.user.is_authenticated:
        #cart_items = Cart.objects.filter(user=request.user)
    #else:
        #cart_items = None
    context = {
        'builder': builder,
        'categories': categories,
        'project_images' : project_images,
        'opening_hours': opening_hours ,
        'builder_office_images' : builder_office_images ,
        #'cart_items': cart_items,
        'current_opening_hours': current_opening_hours,
    }
    return render(request, 'Webapp/builder_detail.html', context)



    
def contact(request):

    contactdetails = ContactDetails.objects.last()
    template = 'Webapp/contact.html'

    if request.method == 'POST' : 
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = contact_form.cleaned_data['subject']
            from_email = contact_form.cleaned_data['from_email']
            message = contact_form.cleaned_data['message']

            try : 
                sm(subject , message ,from_email , ['dharshan@combinedesign.in'] )
            
            except BadHeaderError : 
                return HttpResponse('invalid header')

            return redirect('send_success')

    else:
        contact_form = ContactForm()


    context = {
        'contactdetails' : contactdetails  , 
        'contact_form' : contact_form
    }


    return render(request, template , context)





def send_success(request):
    return HttpResponse('thanks you for you email ^_^')


def join_as_pro(request):
    return render(request, 'Webapp/join_as_pro.html')





