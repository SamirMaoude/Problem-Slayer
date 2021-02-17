from django.urls import path, include

from rest_framework import routers

from .viewsets import ProblemList, ProblemDetail,ContestViewSet,SubmissionList

route = routers.DefaultRouter()

#route.register('problem', ProblemViewSet)
route.register('contests',ContestViewSet)





urlpatterns = [

    path('problems/', ProblemList.as_view(),name='problem-list'),
    path('problems/<int:pk>/', ProblemDetail.as_view(),name='problem-detail'),
    path('submissions/',SubmissionList.as_view(),name='submission-list')
]+route.urls
