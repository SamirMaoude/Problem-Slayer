from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Contest
from django.urls import reverse
from datetime import datetime


class ContestTestCase(APITestCase):

    def setUp(self):

        Contest.objects.create(name="ICPC",startTime="2021-02-17T10:12:00Z",endTime="2021-02-17T10:12:00Z")
        self.client = APIClient()

        self.contest= Contest.objects.get(name="ICPC")




    def test_detail_page_return_200(self):

        url = reverse('contest-detail',args=(self.contest.id,))


        response = self.client.get(url)

        self.assertEqual(response.status_code,200)
    
    def test_detail_page_return_404(self):

        
        url = reverse('contest-detail',args=(self.contest.id+1,))

        response = self.client.get(url)

        self.assertEqual(response.status_code,404)

        

        

        




# Create your tests here.
