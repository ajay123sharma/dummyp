from django.shortcuts import render

# Create your views here.
from .models import Service

def service_detail_view(request):
    obj = Service.objects.get(id=1)

    context = {
        'object': obj,
    }
    return render(request,'services.html',context)