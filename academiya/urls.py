"""academiya URL Configuration

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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from loyiha.views import *
from rest_framework import viewsets
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from.settings import DEBUG, STATIC_URL,STATIC_ROOT,MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static
router = DefaultRouter()
router.register('talabalar',TalabalarViewSet)
router.register('loyiha', LoyihaViewSet)
router.register('eng_yaxshi_talabalar', Eng_yaxshiViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include("account.urls")),
    path('api/',include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if DEBUG:
    urlpatterns += static(STATIC_URL,docoment_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL,document_root = MEDIA_ROOT)
