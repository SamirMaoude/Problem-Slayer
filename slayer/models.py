from django.db import models
from django.contrib.auth.models import User

def problem_file_name(instance, filename):
    return '/'.join(['problems', 'contest', filename])

def submission_file_name(instance, filename):
    return '/'.join(['submission', instance.user.username, filename])




class Contest(models.Model):

    """

        This class represents a contest that takes place during a given time interval.


    """

    name = models.CharField(max_length=200)

    creators = models.ManyToManyField(User,related_name='contests')

    startTime = models.DateTimeField()

    endTime = models.DateTimeField()

    def __str__(self):

        return self.name


class Problem(models.Model):

    """
        A problem is represented is characterized by: 
        1. its statement, 
        2. input/output files to test the results of the submissions
        3. time limit that must be respected by the programs.
    """

    name = models.CharField(max_length=200)

    creators = models.ManyToManyField(User,related_name='problems')

    contest = models.ForeignKey(Contest,on_delete=models.CASCADE)

    statement = models.FileField(upload_to=problem_file_name)

    time_limit = models.PositiveIntegerField()

    test_case_input = models.FileField(upload_to=problem_file_name)

    test_case_output = models.FileField(upload_to=problem_file_name)

    def __str__(self):

        return self.name


class Submission(models.Model):

    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    language = models.CharField(max_length=200,choices=[
        ('C','C'),
        ('C++','C++'),
        ('Python 3','Python 3')
        ],
        default="Python 3")

    code = models.FileField(upload_to=submission_file_name)


"""
class SubmissionVerdict(models.Model):

    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)

    def __init__(self):

        import os

        path = 'submission/'+self.submission.user.username

        os.system("cd "+path)

        if self.submission.language.lower() == "python 3":

            os.system("python "+self.submission.code)

"""




    




