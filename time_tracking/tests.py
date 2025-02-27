from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import TimeEntry
from django.utils import timezone
from hr.models import Employee
from datetime import timedelta

class TimeEntryRegressionTests(APITestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            first_name="Test", last_name="User", email="test.user@example.com", department_id=1
        )
        self.entry_data = {
            "employee": self.employee.id,
            "clock_in": timezone.now(),
        }
        self.url = reverse('timeentry-list')

    def test_create_time_entry(self):
        response = self.client.post(self.url, self.entry_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_time_entry_clock_out(self):
        # Create an entry and then update with clock_out
        response = self.client.post(self.url, self.entry_data, format='json')
        entry_id = response.data['id']
        clock_out_time = timezone.now() + timedelta(hours=8)
        update_data = {"clock_out": clock_out_time}
        response = self.client.patch(reverse('timeentry-detail', args=[entry_id]), update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
