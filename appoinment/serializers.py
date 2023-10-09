from rest_framework import serializers, exceptions
from rest_framework.exceptions import ValidationError

from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('id', 'identifier_system', 'identifier_value', 'patient', 'practitioner', 'organization')

    def validate(self, data):
        patient = data.get("patient", None)
        organization = data.get("organization", None)
        identifier_system = data.get('identifier_system', None)
        identifier_value = data.get('identifier_value', None)
        if Appointment.objects.filter(identifier_system=identifier_system).exists():
            data = {
                "success": False,
                "message": "This identifier_system already exists in the database "
            }
            raise ValidationError(data)
        elif Appointment.objects.filter(identifier_value=identifier_value).exists():
            data = {
                "success": False,
                "message": "This identifier_value already exists in the database"
            }
            raise ValidationError(data)

        return data