from django.shortcuts import render

# Create your views here.
from .models import Blog

def blog_detail_view(request):
    obj = Blog.objects.get(id=1)

    context = {
        'object': obj,
    }
    return render(request,'blog.html',context)