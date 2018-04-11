from django import forms
from .models import Tutor, Subject, Shift


class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ('FirstName', 'LastName', 'Email', 'PhoneNumber', 'RequestedHours',)
        labels = {
            'FirstName': 'First Name',
            'LastName': 'Last Name',
            'Email': 'Email',
            'PhoneNumber': 'Phone Number',
            'RequestedHours': 'Requested Hours',
        }


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('Area',)


class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ('TutorID', 'SubjectID', 'Day', 'StartTime', 'EndTime',)
        labels = {
            'TutorID': 'Tutor',
            'SubjectID': 'Subject',
            'Day': 'Day',
            'StartTime': 'Start Time',
            'EndTime': 'End Time',
        }

