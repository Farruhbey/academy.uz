from django.urls import path, include
from .views import LoginAPI
from .views import RegisterAPI
from rest_framework.routers import DefaultRouter
from .views import *
from loyiha.views import *

router = DefaultRouter()
# router.register('registratsiya', RegisterAPI)
# router.register('login', LoginAPI)


urlpatterns = [
    path('', include(router.urls)), 
    path('register/', RegisterAPI.as_view(), name='register'),   
    path('api/login/', LoginAPI.as_view(), name='login'),
]
