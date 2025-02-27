from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from evaluations.models import Evaluation
from hr.models import Employee

class EvaluationTests(APITestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            first_name="Jane", last_name="Doe", email="jane.doe@example.com", department_id=1
        )
        self.evaluation_data = {
            "employee": self.employee.id,
            "evaluator": "Manager",
            "score": 8,
            "comments": "Good performance"
        }
        self.url = reverse('evaluation-list')

    def test_create_evaluation(self):
        response = self.client.post(self.url, self.evaluation_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)