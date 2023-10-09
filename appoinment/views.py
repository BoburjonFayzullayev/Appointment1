from rest_framework import viewsets, response, status
from rest_framework.generics import CreateAPIView

from .models import Appointment
from .serializers import AppointmentSerializer
from rest_framework.views import APIView


class AppointmentView(CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    # def post(self, request):
    #     serializer = AppointmentSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return response.Response(data={
    #         "success": True,
    #         "message": "Appointment created successfully"
    #     }, status=status.HTTP_201_CREATED)
