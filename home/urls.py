from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('about/', views.about, name='about'),

    
    path('contact/', views.contact, name='contact'),

    path('doctor/', views.doctor, name='doctor'),

    path('services/', views.services, name='services'),

    path(
        'services/<slug:slug>/',
        views.service_detail,
        name='service_detail'
    ),

    path('gallery/', views.gallery, name='gallery'),

    path(
        'testimonials/',
        views.testimonials,
        name='testimonials'
    ),

    path('faq/', views.faq, name='faq'),
    path('appointment/', views.appointment, name='appointment'),
]