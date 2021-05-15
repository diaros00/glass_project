"""glass_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from blogs import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.hello),
    path('createForm/', views.createForm),
    path('addForm', views.addUser),
    path('',views.loginForm),
    path('login',views.login),
    path('addDefect', views.addDefect),
    path('addModel', views.addModel),
    path('logout',views.logout),
    path('collector',views.collector),
    path('choose_defect_on_glass',views.choose_defect_on_glass),
    path('add_defect',views.add_defect),
 

] 


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)