from django.shortcuts import render

# Create your views here.
from .models import About

def about_detail_view(request):
    obj = About.objects.get(id=1)

    context = {
        'object': obj,
    }
    return render(request,'about.html',context)