from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from functools import reduce
from django.db.models import Q
import operator


def home(request):
    return render(request, 'portfolio/home.html',
                  {'portfolio': home})


def tutor_list(request):
    tutor = Tutor.objects.filter()
    return render(request, 'portfolio/tutor_list.html',
                  {'tutors': tutor})


@login_required
def tutor_new(request):
    if request.method == "POST":
        form = TutorForm(request.POST)
        if form.is_valid():
            tutor = form.save(commit=False)
            tutor.save()
            tutors = Tutor.objects.filter()
            return render(request, 'portfolio/tutor_list.html',
                          {'tutors': tutors})
    else:
        form = TutorForm()
        # print("Else")
    return render(request, 'portfolio/tutor_new.html', {'form': form})


@login_required
def tutor_edit(request, pk):
    tutor = get_object_or_404(Tutor, pk=pk)
    if request.method == "POST":
        # update
        form = TutorForm(request.POST, instance=tutor)
        if form.is_valid():
            tutor = form.save(commit=False)
            tutor.save()
            tutor = Tutor.objects.filter()
            return render(request, 'portfolio/tutor_list.html',
                          {'tutors': tutor})
    else:
        # edit
        form = TutorForm(instance=tutor)
    return render(request, 'portfolio/tutor_edit.html', {'form': form})


@login_required
def tutor_delete(request, pk):
    tutor = get_object_or_404(Tutor, pk=pk)
    tutor.delete()
    return redirect('portfolio:tutor_list')


@login_required
def subject_list(request):
    subjects = Subject.objects.filter()
    return render(request, 'portfolio/subject_list.html', {'subjects': subjects})


@login_required
def subject_new(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.save()
            subjects = Subject.objects.filter()
            return render(request, 'portfolio/subject_list.html',
                          {'subjects': subjects})
    else:
        form = SubjectForm()
        # print("Else")
    return render(request, 'portfolio/subject_new.html', {'form': form})


@login_required
def subject_edit(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == "POST":
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            subject = form.save()
            subject.save()
            subjects = Subject.objects.filter()
            return render(request, 'portfolio/subject_list.html', {'subjects': subjects})
    else:
        # print("else")
        form = SubjectForm(instance=subject)
    return render(request, 'portfolio/subject_edit.html', {'form': form})


@login_required
def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    subject.delete()
    subjects = Subject.objects.filter()
    return render(request, 'portfolio/subject_list.html', {'subjects': subjects})


def shift_list(request):
    try:
        a = request.GET.get('shift')
    except KeyError:
        a = None
    if a:
        if a == "All Shifts":
            shifts = Shift.objects.filter()
        else:
            a_list = a.split()
            shifts = Shift.objects.filter(
                reduce(operator.and_,
                       (Q(Day__icontains=a) for a in a_list)) |
                reduce(operator.and_,
                       (Q(TutorID__FirstName__icontains=a) for a in a_list)) |
                reduce(operator.and_,
                       (Q(SubjectID__Area__icontains=a) for a in a_list)) |
                reduce(operator.and_,
                       (Q(StartTime__icontains=a) for a in a_list))
            )
    else:
        shifts = ""
    return render(request, 'portfolio/shift_list.html', {'shifts': shifts})


@login_required
def shift_new(request):
    if request.method == "POST":
        form = ShiftForm(request.POST)
        if form.is_valid():
            shift = form.save(commit=False)
            shift.save()
            shifts = Shift.objects.filter()
            return render(request, 'portfolio/shift_list.html', {'shifts': shifts})
    else:
        form = ShiftForm()
    return render(request, 'portfolio/shift_new.html', {'form': form})


@login_required
def shift_edit(request, pk):
    shift = get_object_or_404(Shift, pk=pk)
    if request.method == "POST":
        form = ShiftForm(request.POST, instance=shift)
        if form.is_valid():
            shift = form.save()
            shift.save()
            shifts = Shift.objects.filter()
            return render(request, 'portfolio/shift_list.html', {'shifts': shifts})
    else:
        # print("else")
        form = ShiftForm(instance=shift)
    return render(request, 'portfolio/shift_edit.html', {'form': form})


@login_required
def shift_delete(request, pk):
    shift = get_object_or_404(Shift, pk=pk)
    shift.delete()
    shifts = Shift.objects.filter()
    return render(request, 'portfolio/shift_list.html', {'shifts': shifts})


def profile(request, pk):
    tutor = get_object_or_404(Tutor, pk=pk)
    tutors = Tutor.objects.filter()
    courses = Course.objects.filter(TutorForCourse=pk)

    return render(request, 'portfolio/profile.html', {'tutors': tutors, 'tutor': tutor, 'courses': courses})


@login_required
def availability_list(request):
    try:
        a = request.GET.get('availabilities')
    except KeyError:
        a = None
    if a:
        if a == "All Availabilities":
            availabilities = Availability.objects.filter()
        else:
            a_list = a.split()
            availabilities = Availability.objects.filter(
                reduce(operator.and_,
                       (Q(Day__icontains=a) for a in a_list)) |
                reduce(operator.and_,
                       (Q(TutorID__FirstName__icontains=a) for a in a_list)) |
                reduce(operator.and_,
                       (Q(SubjectID__Area__icontains=a) for a in a_list)) |
                reduce(operator.and_,
                       (Q(StartTime__icontains=a) for a in a_list))
            )
    else:
        availabilities = ""
    return render(request, 'portfolio/availability_list.html', {'availabilities': availabilities})


@login_required
def availability_new(request):
    if request.method == "POST":
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            availability = form.save(commit=False)
            availability.save()
            availabilities = Availability.objects.filter()
            return render(request, 'portfolio/availability_list.html', {'availabilities': availabilities})
    else:
        form = AvailabilityForm()
    return render(request, 'portfolio/availability_new.html', {'form': form})


@login_required
def availability_edit(request, pk):
    availability = get_object_or_404(Availability, pk=pk)
    if request.method == "POST":
        form = AvailabilityForm(request.POST, instance=availability)
        if form.is_valid():
            availability = form.save()
            availability.save()
            availabilities = Availability.objects.filter()
            return render(request, 'portfolio/availability_list.html', {'availabilities': availabilities})
    else:
        # print("else")
        form = AvailabilityForm(instance=availability)
    return render(request, 'portfolio/shift_edit.html', {'form': form})


@login_required
def availability_delete(request, pk):
    availability = get_object_or_404(Availability, pk=pk)
    availability.delete()
    availabilities = Availability.objects.filter()
    return render(request, 'portfolio/availability_list.html', {'availabilities': availabilities})


def course_list(request):
    try:
        a = request.GET.get('course')
    except KeyError:
        a = None
    if a:
        a_list = a.split()
        courses = Course.objects.filter(
            reduce(operator.and_,
                   (Q(Department__icontains=a) for a in a_list)) |
            reduce(operator.and_,
                   (Q(Number__icontains=a) for a in a_list)) |
            reduce(operator.and_,
                   (Q(Name__icontains=a) for a in a_list))
        )
    else:
        courses = Course.objects.filter()
    return render(request, 'portfolio/course_list.html', {'courses': courses})


@login_required
def course_new(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            courses = Course.objects.filter()
            return render(request, 'portfolio/course_list.html', {'courses': courses})
    else:
        form = CourseForm()
    return render(request, 'portfolio/course_new.html', {'form': form})


@login_required
def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            course.save()
            courses = Course.objects.filter()
            return render(request, 'portfolio/course_list.html', {'courses': courses})
    else:
        # print("else")
        form = CourseForm(instance=course)
    return render(request, 'portfolio/course_edit.html', {'form': form})


@login_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.delete()
    courses = Course.objects.filter()
    return render(request, 'portfolio/course_list.html', {'courses': courses})

