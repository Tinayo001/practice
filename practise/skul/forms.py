from django import forms
from .models import Student, Subject

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'marks', 'student']

