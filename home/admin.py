from django.contrib import admin
from .models import Appointment, Clinic, Service, Doctor, Gallery, Testimonial , FAQ


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'phone',
        'service',
        'preferred_date',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'service',
        'preferred_date',
    )

    search_fields = (
        'name',
        'phone',
        'email',
    )

    ordering = (
        '-created_at',
    )

    date_hierarchy = 'preferred_date'


@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'phone',
        'email',
        'address',
        'years_experience',
        'rating',
    )



@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'short_description', 'description')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)



@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'qualification',
        'specialization',
        'experience',
        'is_active',
    )

    list_filter = (
        'is_active',
        'specialization',
    )

    search_fields = (
        'name',
        'qualification',
        'specialization',
        'about',
    )

    ordering = ('name',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_active',
    )

    list_filter = (
        'is_active',
    )

    search_fields = (
        'title',
        'description',
    )

    ordering = ('title',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'patient_name',
        'rating',
        'is_active',
        'created_at',
    )

    list_filter = (
        'rating',
        'is_active',
    )

    search_fields = (
        'patient_name',
        'message',
    )

    ordering = ('-created_at',)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('question', 'answer')
    ordering = ('question',)