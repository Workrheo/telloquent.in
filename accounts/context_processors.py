from designer.models import Designer
from django.conf import settings



def get_designer(request):
    try:
        designer = Designer.objects.get(user=request.user)
    except:
        designer = None
    return dict(designer=designer)



def get_google_api(request):
    return {'GOOGLE_API_KEY': settings.GOOGLE_API_KEY}