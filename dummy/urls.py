"""dummy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from home.views import home_detail_view
from contact.views import contact_detail_view
from about.views import about_detail_view
from service.views import service_detail_view
from product.views import product_detail_view
from blog.views import blog_detail_view

from django.conf.urls.static import static
from dummy import settings

urlpatterns = [
    path('', home_detail_view,name='home'),
    path('home/', home_detail_view, name='home'),
    path('contact/', contact_detail_view, name='contact'),
    path('about/', about_detail_view, name='about'),
    path('services/', service_detail_view , name='services'),
    path('products/', product_detail_view , name='products'),
    path('blog/', blog_detail_view , name='blog'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
