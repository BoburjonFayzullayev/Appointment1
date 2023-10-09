from django.core.validators import RegexValidator
from django.db import models



class Appointment(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier_system = models.URLField(null=True, blank=True)
    identifier_value = models.CharField(max_length=20, null=True, blank=True, validators=[RegexValidator(r'^[1-9][0-9]*$')])
    patient = models.CharField(max_length=10, validators=[RegexValidator(r'^[1-9][0-9]{9}$')])
    practitioner = models.CharField(max_length=10, validators=[RegexValidator(r'^[1-9][0-9]{9}$')])
    organization = models.CharField(max_length=10, validators=[RegexValidator(r'^[1-9][0-9]{9}$')])

    def __str__(self):
        return str(self.id)
