from django.shortcuts import render
from .models import Student
from django.db import models  # This is needed for 'models.Sum'

def add_student(request):
    return render(request, 'add_student.html')

def add_subject(request):
    return render(request, 'add_subject.html')

def show_all_students():
    pens = Student.objects.all()
    return pens


def calculate_total_marks_by_name(student_name):
    """
    Function to calculate the total marks for a given student by name.

    Args:
        student_name (str): The name of the student whose total marks are to be calculated.

    Returns:
        dict: A dictionary containing the student's name and their total marks.
    """
    # Retrieve the student object by name
    try:
        student = Student.objects.get(name=student_name)
    except Student.DoesNotExist:
        return {"error": "Student not found"}

    # Calculate the total marks
    total_marks = student.subjects.aggregate(total=models.Sum('marks'))['total'] or 0
    

    # Return the total marks as part of a dictionary
    return {
        "student": student.name,
        "total_marks": total_marks
    }
 
