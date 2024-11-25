from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import StudentSerializer, SubjectSerializer, serializers
from skul.models import Student, Subject

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

