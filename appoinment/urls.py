from  django.urls import path
from .views import AppointmentView

urlpatterns = [
    path('api/', AppointmentView.as_view(), name="appointment")

]