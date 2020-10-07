"""prototype URL Configuration

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
from django.conf.urls import url
# from filebrowser.sites import site
from django.contrib import admin
from django.urls import path, include
from core import views
from django.conf.urls.static import static
from prototype.settings import settings
from simple_sso.sso_server.server import Server
from simple_sso.sso_client.client import Client

sso_server = Server()
sso_client = Client(settings.SSO_SERVER, settings.SSO_PUBLIC_KEY, settings.SSO_PRIVATE_KEY)

urlpatterns = [
    # path('admin/filebrowser/', site.urls),
    # path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    url(r'^server/', include(sso_server.get_urls())),
    path('authorize/', views.authorize, name='authorize'),
    path('client/', include(sso_client.get_urls()))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
