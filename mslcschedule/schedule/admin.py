from django.contrib import admin
from .models import Tutor, Subject, Shift, Course


class TutorList(admin.ModelAdmin):
    list_display = ('FirstName', 'LastName', 'Email', 'PhoneNumber', 'RequestedHours')
    list_filter = ('FirstName', 'LastName')
    search_fields = ('FirstName', 'LastName')
    ordering = ['FirstName', 'LastName']


class SubjectList(admin.ModelAdmin):
    list_display = ('id', 'Area')
    list_filter = ('id', 'Area')
    search_fields = ('id', 'Area')
    ordering = ['Area']


class ShiftList(admin.ModelAdmin):
    list_display = ('TutorID', 'SubjectID', 'Day', 'StartTime', 'EndTime')
    list_filter = ('TutorID', 'SubjectID', 'Day', 'StartTime', 'EndTime')
    search_fields = ('TutorID', 'SubjectID', 'Day', 'StartTime', 'EndTime')
    ordering = ['TutorID']


class CourseList(admin.ModelAdmin):
    list_display = ('SubjectID', 'Department', 'Number', 'Name',)
    list_filter = ('SubjectID', 'Department', 'Number', 'Name', 'TutorForCourse')
    search_fields = ('SubjectID', 'Department', 'Number', 'Name', 'TutorForCourse')
    ordering = ['SubjectID', 'Department', 'Number']


admin.site.register(Tutor, TutorList)
admin.site.register(Subject, SubjectList)
admin.site.register(Shift, ShiftList)
admin.site.register(Course, CourseList)
