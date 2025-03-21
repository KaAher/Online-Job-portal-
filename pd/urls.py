"""
URL configuration for pd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from pd1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('jobseeker/',views.jobseeker,name='jobseeker'),
    path('jobprovider/',views.jobprovider ,name='jobprovider'),
    path('jobpage/',views.jobpage ,name='jobpage' ),
    path('login/',views.login,name='login'),
    path('joblogin/',views.joblogin,name='joblogin'),
    path('succesful/',views.succesful,name='succesful'),
    path('notification/',views.notification,name='notification'),
    path('manage/',views.manage,name='manage'),
    path('applyed/',views.applyed,name='applyed'),
    path('create_account/',views.create_account,name='create_account'),
    path('create_account_job/',views.create_account_job,name='create_account_job')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

