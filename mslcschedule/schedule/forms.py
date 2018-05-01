from django import forms
from .models import Tutor, Subject, Shift, Course, Availability


class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ('FirstName', 'LastName', 'Email', 'PhoneNumber', 'RequestedHours', 'TutorImage')
        labels = {
            'FirstName': 'First Name',
            'LastName': 'Last Name',
            'Email': 'Email',
            'PhoneNumber': 'Phone Number',
            'RequestedHours': 'Requested Hours',
            'TutorImage': 'Upload Image',
        }

    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all())

    def __init__(self, *args, **kwargs):
        # Only in case we build the form from an instance
        # (otherwise, 'toppings' list should be empty)
        if kwargs.get('instance'):
            # We get the 'initial' keyword argument or initialize it
            # as a dict if it didn't exist.
            initial = kwargs.setdefault('initial', {})
            # The widget for a ModelMultipleChoiceField expects
            # a list of primary key for the selected data.
            initial['courses'] = [t.pk for t in kwargs['instance'].course_set.all()]

        forms.ModelForm.__init__(self, *args, **kwargs)

        # Overriding save allows us to process the value of 'toppings' field
    def save(self, commit=True):
            # Get the unsaved Pizza instance
        instance = forms.ModelForm.save(self, False)

        # Prepare a 'save_m2m' method for the form,
        old_save_m2m = self.save_m2m

        def save_m2m():
            old_save_m2m()
            # This is where we actually link the pizza with toppings
            instance.course_set.clear()
            for course in self.cleaned_data['courses']:
                instance.course_set.add(course)

        self.save_m2m = save_m2m

        # Do we need to save all changes now?
        # if commit:
        instance.save()
        self.save_m2m()

        return instance


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('Area',)


class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ('SubjectID', 'TutorID', 'Day', 'StartTime', 'EndTime',)
        labels = {
            'TutorID': 'Tutor',
            'SubjectID': 'Subject',
            'Day': 'Day',
            'StartTime': 'Start Time',
            'EndTime': 'End Time',
        }


class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ('TutorID', 'Day', 'StartTime', 'EndTime',)
        labels = {
            'TutorID': 'Tutor',
            'Day': 'Day',
            'StartTime': 'Start Time',
            'EndTime': 'End Time',
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('SubjectID', 'Department', 'Number', 'Name')
        labels = {
            'SubjectID': 'Subject',
            'Department': 'Department',
            'Number': 'Number',
            'Name': 'Name'
        }
