from django.shortcuts import render, redirect, get_object_or_404
from .forms import AppointmentForm
from django.contrib import messages
from .models import Clinic, Service, Doctor, Gallery, Testimonial, FAQ

def home(request):
    clinic = Clinic.objects.first()
    services = Service.objects.filter(is_active=True)
    doctor = Doctor.objects.filter(is_active=True).first()

    return render(
        request,
        'home/index.html',
        {
            'clinic': clinic,
            'services': services,
            'doctor': doctor,
        }
    )


def about(request):

    clinic = Clinic.objects.first()

    return render(
        request,
        'home/about.html',
        {
            'clinic': clinic
        }
    )

def contact(request):
    clinic = Clinic.objects.first()
    return render(request, 'home/contact.html', {
        "clinic": clinic
    })


def doctor(request):
    doctor = Doctor.objects.filter(is_active=True).first()
    clinic = Clinic.objects.first()

    return render(
        request,
        'home/doctor.html',
        {'doctor': doctor, 'clinic': clinic}
    )

def services(request):
    clinic = Clinic.objects.first()
    services = Service.objects.filter(is_active=True)
    return render(request, 'home/services.html', {
        'services': services,
        'clinic': clinic
    })


def service_detail(request, slug):
    clinic = Clinic.objects.first()
    service = get_object_or_404(
        Service,
        slug=slug,
        is_active=True
    )

    return render(
        request,
        'home/service_detail.html',
        {'service': service, 'clinic': clinic}
    )


def gallery(request):
    gallery_images = Gallery.objects.filter(is_active=True)
    clinic = Clinic.objects.first()

    return render(
        request,
        'home/gallery.html',
        {'gallery_images': gallery_images, 'clinic': clinic }
    )


def testimonials(request):
    testimonials = Testimonial.objects.filter(is_active=True)
    clinic = Clinic.objects.first()

    return render(
        request,
        'home/testimonials.html',
        {'testimonials': testimonials, 'clinic': clinic}
    )


def faq(request):
    faqs = FAQ.objects.filter(is_active=True)
    clinic = Clinic.objects.first()

    return render(
        request,
        'home/faq.html',
        {'faqs': faqs, 'clinic': clinic}
    )


def appointment(request):
    clinic = Clinic.objects.first()

    if request.method == 'POST':

        form = AppointmentForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Appointment submitted successfully! We will contact you soon.'
            )

            return redirect('appointment')

    else:
        form = AppointmentForm()

    return render(
        request,
        'home/appointment.html',
        {
            'form': form,
            'clinic': clinic
        }
    )