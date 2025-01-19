from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Experience, Booking

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'english_title', 'duration', 'price')
    search_fields = ('title', 'english_title')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'experience', 'date', 'time')
    list_filter = ('date', 'experience')
    search_fields = ('name', 'email')
