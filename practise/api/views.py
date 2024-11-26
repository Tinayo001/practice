from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import StudentSerializer, SubjectSerializer, serializers
from skul.models import Student, Subject
from skul.views import calculate_total_marks_by_name, show_all_students 


@api_view(['POST'])
def add_student(request):
    student_data = request.data
    serializer = StudentSerializer(data=student_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['POST'])
def add_subject(request):
    subject_data = request.data
    serializer = SubjectSerializer(data=subject_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def get_total(request):
    student_name = request.data.get("name")
    student_marks = calculate_total_marks_by_name(student_name)
    return Response(student_marks)

@api_view(['GET'])
def get_all(request):
    all_students = show_all_students()
    serializer = StudentSerializer(all_students, many=True)  # Serialize them
    return Response(serializer.data) 
