from django.shortcuts import render

# Create your views here.
from .models import Contact

def contact_detail_view(request):
    obj = Contact.objects.get(id=1)

    context = {
        'object': obj,
    }
    return render(request,'contact.html',context)