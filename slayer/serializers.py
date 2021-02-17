from rest_framework import serializers
from .models import Problem,Contest,Submission


class ProblemSerializer(serializers.ModelSerializer):

    class Meta:

        model = Problem
        fields = ['name','creators','contest','statement','time_limit','test_case_input','test_case_output']


class ContestSerializer(serializers.ModelSerializer):

    class Meta:

        model = Contest
        exclude = []


class SubmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Submission

        exclude = []

        read_only_fields = ['user']

    


