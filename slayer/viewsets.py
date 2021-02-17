from rest_framework import viewsets, generics,mixins

from .serializers import ProblemSerializer,ContestSerializer, SubmissionSerializer

from .models import Problem,Contest,Submission

from django.http import Http404
from django.shortcuts import get_object_or_404


class ProblemList(generics.ListCreateAPIView):

    queryset = Problem.objects.all()

    serializer_class = ProblemSerializer

class ProblemDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Problem.objects.all()

    serializer_class = ProblemSerializer

    def get_object(self):
        try:
            return get_object_or_404(Problem,pk=self.kwargs.get('pk'))
        except Problem.DoesNotExist:
            raise Http404




class ContestViewSet(viewsets.ModelViewSet):

    queryset = Contest.objects.all()
    serializer_class = ContestSerializer

class SubmissionList(mixins.CreateModelMixin,mixins.ListModelMixin, generics.GenericAPIView):

    queryset = Submission.objects.all()

    serializer_class = SubmissionSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):

        serializer.save(user=self.request.user)