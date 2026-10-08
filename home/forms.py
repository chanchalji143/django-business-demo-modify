from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment

        fields = [
            'name',
            'phone',
            'email',
            'service',
            'preferred_date',
            'message',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),

            'service': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter required service'
            }),

            'preferred_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your message',
                'rows': 4
            }),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if not phone.isdigit():
            raise forms.ValidationError(
            'Please enter a valid phone number.'
        )

        if len(phone) < 10:
            raise forms.ValidationError(
            'Phone number must be at least 10 digits.'
        )

        return phone