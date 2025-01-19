from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Experience, Booking
from .serializers import ExperienceSerializer, BookingSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
from rest_framework import viewsets
from .models import Experience, Booking
from .serializers import ExperienceSerializer, BookingSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
