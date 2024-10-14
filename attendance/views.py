from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Attendance
from .forms import AttendanceForm

# Create your views here.
def index(request):
    attendances = Attendance.objects.all()  # Fetch all attendance records
    return render(request, 'attendance/index.html', {'attendances': attendances})

def view_attendance(request, id):
    attendance = get_object_or_404(Attendance, pk=id)
    return render(request, 'attendance/view.html', {'attendance': attendance})

def add(request):
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()  # Use form.save() directly to save the instance
            return redirect('index')  # Redirect to the index page after successful save
    else:
        form = AttendanceForm()
    return render(request, 'attendance/add.html', {
        'form': form
    })

def edit(request, id):
    attendance = get_object_or_404(Attendance, pk=id)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the index page after successful save
    else:
        form = AttendanceForm(instance=attendance)
    return render(request, 'attendance/edit.html', {
        'form': form
    })

def delete(request, id):
    attendance = get_object_or_404(Attendance, pk=id)
    if request.method == 'POST':
        attendance.delete()
        return redirect('index')  # Redirect to the index page after deletion
    return render(request, 'attendance/delete.html', {'attendance': attendance})
