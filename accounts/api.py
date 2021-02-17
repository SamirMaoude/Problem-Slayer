from django.contrib.auth.models import User

from rest_framework import viewsets, generics

from .serializers import ProblemSlayerUserSerializer


class ProblemSlayerUserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.filter(is_superuser=False)

    serializer_class = ProblemSlayerUserSerializer

