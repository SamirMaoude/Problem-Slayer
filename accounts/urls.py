from django.urls import path,include
from . import views

from rest_framework import routers
from .api import ProblemSlayerUserViewSet

router = routers.DefaultRouter()

router.register('users', ProblemSlayerUserViewSet)

urlpatterns = [
    
    path('signup', views.SignUpView.as_view(),name='signup'),
    path('api/',include(router.urls))
]
