from django.db import models


class Appointment(models.Model):

    name = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    email = models.EmailField(blank=True)

    service = models.CharField(max_length=100)

    preferred_date = models.DateField(blank=True, null=True)

    message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    def __str__(self):
        return f"{self.name} - {self.phone}"


class Clinic(models.Model):

    name = models.CharField(
        max_length=200,
        default='City Dental Hospital'
    )

    tagline = models.CharField(
        max_length=200,
        default='Your Smile, Our Priority'
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    address = models.CharField(
        max_length=300,
        blank=True
    )

    about = models.TextField(
        blank=True
    )

    years_experience = models.PositiveIntegerField(
        default=10
    )

    patients_count = models.PositiveIntegerField(
        default=10
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=4.9
    )

    logo = models.ImageField(
        upload_to='clinic/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name



class Service(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    qualification = models.CharField(max_length=300, blank=True)
    specialization = models.CharField(max_length=300, blank=True)
    experience = models.PositiveIntegerField(default=0)
    about = models.TextField(blank=True)
    photo = models.ImageField(upload_to='doctors/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title or "Gallery Image"


class Testimonial(models.Model):
    patient_name = models.CharField(max_length=200)
    message = models.TextField()
    rating = models.PositiveIntegerField(default=5)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_name


class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question