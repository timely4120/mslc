from django.db import models
import datetime

DAYS = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
]


TIMES = [
    (datetime.time(8, 30, 0), '08:30 AM'),
    (datetime.time(9, 0, 0), '09:00 AM'),
    (datetime.time(9, 30, 0), '09:30 AM'),
    (datetime.time(10, 0, 0), '10:00 AM'),
    (datetime.time(10, 30, 0), '10:30 AM'),
    (datetime.time(11, 0, 0), '11:00 AM'),
    (datetime.time(11, 30, 0), '11:30 AM'),
    (datetime.time(12, 0, 0), '12:00 PM'),
    (datetime.time(12, 30, 0), '12:30 PM'),
    (datetime.time(13, 0, 0), '1:00 PM'),
    (datetime.time(13, 30, 0), '1:30 PM'),
    (datetime.time(14, 0, 0), '2:00 PM'),
    (datetime.time(14, 30, 0), '2:30 PM'),
    (datetime.time(15, 0, 0), '3:00 PM'),
    (datetime.time(15, 30, 0), '3:30 PM'),
    (datetime.time(16, 0, 0), '4:00 PM'),
    (datetime.time(16, 30, 0), '4:30 PM'),
    (datetime.time(17, 0, 0), '5:00 PM'),
    (datetime.time(17, 30, 0), '5:30 PM'),
    (datetime.time(18, 0, 0), '6:00 PM'),
    (datetime.time(18, 30, 0), '6:30 PM'),
    (datetime.time(19, 0, 0), '7:00 PM'),
    (datetime.time(19, 30, 0), '7:30 PM'),
    (datetime.time(20, 0, 0), '8:00 PM'),
    (datetime.time(20, 30, 0), '8:30 PM'),
    (datetime.time(21, 0, 0), '9:00 PM'),
    (datetime.time(21, 30, 0), '9:30 PM'),
    (datetime.time(22, 0, 0), '10:00 PM'),
    (datetime.time(22, 30, 0), '10:30 PM'),
    (datetime.time(23, 0, 0), '11:00 PM'),
    (datetime.time(23, 30, 0), '11:30 PM'),
]


class Tutor(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100)
    PhoneNumber = models.CharField(max_length=10, )
    RequestedHours = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return str(self.FirstName + " " + self.LastName)

    def phoneString(self):
        p = str(self.PhoneNumber)
        pString = p[:3] + '-' + p[3:6] + '-' + p[-4:]
        return pString


class Subject(models.Model):
    Area = models.CharField(max_length=20)

    def __str__(self):
        return str(self.Area)


class Shift(models.Model):
    TutorID = models.ForeignKey(Tutor, related_name='shiftTutor')
    SubjectID = models.ForeignKey(Subject, related_name='shiftSubject')
    Day = models.CharField(max_length=20, choices=DAYS)
    StartTime = models.TimeField(choices=TIMES)
    EndTime = models.TimeField(choices=TIMES)

    class Meta:
        ordering = ["Day", "StartTime", "SubjectID"]


class Course(models.Model):
    SubjectID = models.ForeignKey(Subject, related_name='subjectCourse')
    Department = models.CharField(max_length=4)
    Number = models.CharField(max_length=4)
    Name = models.CharField(max_length=200)
    TutorForCourse = models.ManyToManyField(Tutor)

    def __str__(self):
        return str(self.Department + " " + self.Number + ": " + self.Name)


class Availability(models.Model):
    TutorID = models.ForeignKey(Tutor, related_name='availabilityTutor')
    Day = models.CharField(max_length=20, choices=DAYS)
    StartTime = models.TimeField(choices=TIMES)
    EndTime = models.TimeField(choices=TIMES)

    class Meta:
        ordering = ["Day", "StartTime",]


# Add TutorForCourse field to Tutor
Tutor.add_to_class('TutorForCourse', models.ManyToManyField('self', through=Course, related_name='followers', symmetrical=False))