"""
URL configuration for zetflix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.zetflix, name='zetflix')
Class-based views
    1. Add an import:  from other_app.views import zetflix
    2. Add a URL to urlpatterns:  path('', zetflix.as_view(), name='zetflix')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from ..zapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('zapp.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
