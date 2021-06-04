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
    path('report', views.report, name='pie-chart'),
    path('',views.loginForm),
    path('login',views.login),
    path('addDefect', views.addDefect),
    path('addModel', views.addModel),
    path('logout',views.logout),
    path('collector',views.collector),
    path('choose_defect_on_glass',views.choose_defect_on_glass),
    path('add_no_defect',views.add_no_defect),
    path('add_have_defect',views.add_have_defect),
    path('filtering',views.filtering),
    path('add_defect1',views.add_defect1),
    path('add_defect2',views.add_defect2),
    path('add_defect3',views.add_defect3),
    path('add_defect4',views.add_defect4),
    path('add_defect5',views.add_defect5),
    path('add_defect6',views.add_defect6),
    path('add_defect7',views.add_defect7),
    path('add_defect8',views.add_defect8),
    path('add_defect9',views.add_defect9),
    path('add_defect10',views.add_defect10),
    path('add_defect11',views.add_defect11),
    path('add_defect12',views.add_defect12),
    path('add_defect13',views.add_defect13),
    path('add_defect14',views.add_defect14),
    path('add_defect15',views.add_defect15),
    path('add_defect16',views.add_defect16),
    path('add_defect17',views.add_defect17),
    path('add_defect18',views.add_defect18),
    path('add_defect19',views.add_defect19),
    path('add_defect20',views.add_defect20),
    path('add_defect21',views.add_defect21),
    path('add_defect22',views.add_defect22),
    path('add_defect23',views.add_defect23),
    path('add_defect24',views.add_defect24),
    path('add_defect25',views.add_defect25),
    path('add_defect26',views.add_defect26),
    path('add_defect27',views.add_defect27),
    path('add_defect28',views.add_defect28),
    path('add_defect29',views.add_defect29),
    path('add_defect30',views.add_defect30),
    path('add_defect31',views.add_defect31),
    path('add_defect32',views.add_defect32),
    path('add_defect33',views.add_defect33),
    path('add_defect34',views.add_defect34),
    path('add_defect35',views.add_defect35),
    path('add_defect36',views.add_defect36),
    path('add_defect37',views.add_defect37),
    path('add_defect38',views.add_defect38),
    path('add_defect39',views.add_defect39),
    path('add_defect40',views.add_defect40),
    path('add_defect41',views.add_defect41),
    path('add_defect42',views.add_defect42),
    path('add_defect43',views.add_defect43),
    path('add_defect44',views.add_defect44),
    path('add_defect45',views.add_defect45),
    path('add_defect46',views.add_defect46),
    path('add_defect47',views.add_defect47),
    path('add_defect48',views.add_defect48),
    path('add_defect49',views.add_defect49),
    path('add_defect50',views.add_defect50),
    path('add_defect51',views.add_defect51),
    path('add_defect52',views.add_defect52),
    path('add_defect53',views.add_defect53),
    path('add_defect54',views.add_defect54),
    path('add_defect55',views.add_defect55),
    path('add_defect56',views.add_defect56),
    path('add_defect57',views.add_defect57),
    path('add_defect58',views.add_defect58),
    path('add_defect59',views.add_defect59),
    path('add_defect60',views.add_defect60)
 

] 


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)