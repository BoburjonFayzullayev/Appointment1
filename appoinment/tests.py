from django.test import TestCase
from rest_framework.reverse import reverse
from .models import Appointment
from rest_framework import status
from rest_framework import serializers
from rest_framework.test import APITestCase
from .serializers import AppointmentSerializer
from rest_framework.exceptions import ValidationError



class CreateTestCase(APITestCase):

    def setUp(self):
        self.url = reverse('appointment')

    def test_create_app(self):
        data = {
            'id': 9,
            'identifier_system': "https://shifonur.uz/",
            'identifier_value': 1234,
            'patient': 1234567890,
            'practitioner': 1234567890,
            'organization': 1234567890
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        appoint_count = Appointment.objects.count()
        self.assertEqual(appoint_count, 1)
        appoint = Appointment.objects.get(id=9)

        self.assertEquals(appoint.identifier_system, "https://shifonur.uz/")
        self.assertEquals(appoint.identifier_value, '1234')
        self.assertEquals(appoint.patient, '1234567890')
        self.assertEquals(appoint.practitioner, '1234567890')
        self.assertEquals(appoint.organization, '1234567890')




class RegexAPITestCase(APITestCase):

    def test_valid(self):
        data = {
            'id': 9,
            'identifier_system': "https://shifonur.uz/",
            'identifier_value': 1234,
            'patient': 1234567890,
            'practitioner': 1234567890,
            'organization': 1234567890
        }

        response = self.client.post(reverse('appointment'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        appoint = Appointment.objects.get(id=9)

        self.assertRegex(appoint.patient, r'^[1-9][0-9]{9}$')
        self.assertRegex(appoint.practitioner, r'^[1-9][0-9]{9}$')
        self.assertRegex(appoint.organization, r'^[1-9][0-9]{9}$')



    def test_invalid(self):
        data = {
            'id': 10,
            'identifier_system': "https://shifonur.uz/",
            'identifier_value': 1234,
            'patient': 12345678,
            'practitioner': 123456,
            'organization': 123456789025
        }

        response = self.client.post(reverse('appointment'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)




class InvalidAPITestCase(APITestCase):
    def test_invalid_appointment(self):
        data = {
            'id': 4,
            'identifier_system': "https://shifonur.uz/",
            'identifier_value': '1234'
        }

        response = self.client.post(reverse('appointment'), data=data, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST)

        # Check if the 'patient' field is required
        errors = response.data
        self.assertIn('patient', errors)
        self.assertIn('practitioner', errors)
        self.assertIn('organization', errors)

class AppointmentSerializerTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('appointment')

    def test_duplicate_identifier_system(self):
        existing_appointment = Appointment.objects.create(
            id=1,
            identifier_system="https://example.com/",
            identifier_value="12345",
            patient="1234567890",
            practitioner="1234567890",
            organization="1234567890"
        )

        data = {
            "id": 2,
            "identifier_system": "https://example.com/",
            "identifier_value": "67890",
            "patient": "1234567891",
            "practitioner": "1234567891",
            "organization": "1234567891"
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



    def test_duplicate_identifier_value(self):
        existing_appointment = Appointment.objects.create(
            id=1,
            identifier_system="https://example.com/",
            identifier_value="12345",
            patient="1234567890",
            practitioner="1234567890",
            organization="1234567890"
        )

        data = {
            "id": 2,
            "identifier_system": "https://example2.com/",
            "identifier_value": "12345",
            "patient": "1234567891",
            "practitioner": "1234567891",
            "organization": "1234567891"
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



class InvalidMessageAPITestCase(APITestCase):
    def test_duplicate_identifier_system(self):
        existing_appointment = Appointment.objects.create(
            id=1,
            identifier_system="https://example.com/",
            identifier_value="12345",
            patient="1234567890",
            practitioner="1234567890",
            organization="1234567890"
        )

        serializer_data = {
            "id": 2,
            "identifier_system": "https://example.com/",
            "identifier_value": "67890",
            "patient": "1234567891",
            "practitioner": "1234567891",
            "organization": "1234567891"
        }

        serializer = AppointmentSerializer(data=serializer_data)

        with self.assertRaisesMessage(ValidationError, "This identifier_system already exists in the database"):
            serializer.is_valid(raise_exception=True)


    def test_duplicate_identifier_value(self):
        existing_appointment = Appointment.objects.create(
            id=1,
            identifier_system="https://example.com/",
            identifier_value="12345",
            patient="1234567890",
            practitioner="1234567890",
            organization="1234567890"
        )

        serializer_data = {
            "id": 2,
            "identifier_system": "https://example.uz/",
            "identifier_value": "12345",
            "patient": "1234567891",
            "practitioner": "1234567891",
            "organization": "1234567891"
        }

        serializer = AppointmentSerializer(data=serializer_data)

        with self.assertRaisesMessage(ValidationError, "This identifier_value already exists in the database"):
            serializer.is_valid(raise_exception=True)



