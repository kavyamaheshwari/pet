"""enterprice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('sign/', views.sign),
    path('signupcheck/', views.signupcheck),
    path('login/', views.login),
    path('logincheck/', views.logincheck),
    path('home/', views.home),
    path('display/', views.display),
	path('blog/',views.blog),
    path('contactus/', views.contactus),
    path('contactadd/', views.contactadd),
    path('ques/', views.ques),
    path('feed/', views.feed),
    path('donate/',views.donate),
    path('feedadd/', views.feedadd),
    path('search/', views.searchpettype1),
    path('searchpet/',views.searchpet),
    path('add/', views.add),
	path('logout/',views.logout),
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
