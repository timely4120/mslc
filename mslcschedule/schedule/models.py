from django.db import models
from django.utils import timezone

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
    ('08:30AM', '08:30'),
    ('09:00AM', '09:00'),
    ('09:30AM', '09:30'),
    ('10:00AM', '10:00'),
    ('10:30AM', '10:30'),
    ('11:00AM', '11:00'),
    ('11:30AM', '11:30'),
    ('12:00PM', '12:00'),
    ('12:30PM', '12:30'),
    ('01:00PM', '13:00'),
    ('01:30PM', '13:30'),
    ('02:00PM', '14:00'),
    ('02:30PM', '14:30'),
    ('03:00PM', '15:00'),
    ('03:30PM', '15:30'),
    ('04:00PM', '16:00'),
    ('04:30PM', '16:30'),
    ('05:00PM', '17:00'),
    ('05:30PM', '17:30'),
    ('06:00PM', '18:00'),
    ('06:30PM', '18:30'),
    ('07:00PM', '19:00'),
    ('07:30PM', '19:30'),
    ('08:00PM', '20:00'),
    ('08:30PM', '20:30'),
    ('09:00PM', '21:00'),
    ('09:30PM', '21:30'),
    ('10:00PM', '22:00'),
    ('10:30PM', '22:30'),
    ('11:00PM', '23:00'),
    ('11:30PM', '23:30'),
]


class Tutor(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100)
    PhoneNumber = models.CharField(max_length=10)
    RequestedHours = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return str(self.FirstName + " " + self.LastName)


class Subject(models.Model):
    Area = models.CharField(max_length=20)

    def __str__(self):
        return str(self.Area)


class Shift(models.Model):
    TutorID = models.ForeignKey(Tutor, related_name='tutor')
    SubjectID = models.ForeignKey(Subject, related_name='subject')
    Day = models.CharField(max_length=20, choices=DAYS)
    StartTime = models.CharField(max_length=20, choices=TIMES)
    EndTime = models.CharField(max_length=20, choices=TIMES)
