from django.shortcuts import render

# Create your views here.
from .models import Home

def home_detail_view(request):
    obj = Home.objects.get(id=1)

    context = {
        'object': obj,
    }
    return render(request,'index.html',context)