from django import forms
from .models import Appointment
from doctor.models import Doctor,AvailableTime

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['time', 'symptoms', 'type']
        labels = {
            'doctor': 'Select Doctor',
            'paitent': 'Select Patient',
            'time': 'Select Time Slot',
            'symptoms': 'Describe Symptoms',
            'type': 'Appointment Type',
        }

    def __init__(self,*args,**kwargs):
        doctor = kwargs.pop('doctor', None) 
        super(AppointmentForm, self).__init__(*args, **kwargs)
        if doctor:
            self.fields['time'].queryset = AvailableTime.objects.filter(doctor=doctor)

class AppointmentEditForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['time','status','doctor_review']

    def __init__(self,*args,**kwargs):
        super(AppointmentEditForm, self).__init__(*args, **kwargs)
        doctor = self.instance.doctor
        self.fields['time'].queryset = doctor.available_time



