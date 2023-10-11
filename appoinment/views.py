from rest_framework import viewsets, response, status
from rest_framework.generics import CreateAPIView

from .models import Appointment
from .serializers import AppointmentSerializer
from rest_framework.views import APIView

from rest_framework import viewsets, response, status
from rest_framework.generics import CreateAPIView

from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentView(CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        response_data = {
            "success": True,
            "message": "Ma'lumotlar muvaffaqiyatli saqlandi"
        }
        return response.Response(response_data, status=status.HTTP_201_CREATED)

    def handle_exception(self, exc):
        response_data = {
            "success": False,
            "message": f"Xatolik yuz berdi: {str(exc)}"
        }
        return response.Response(response_data, status=status.HTTP_400_BAD_REQUEST)
