from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Student
from .serializers import StudentSerializer

# ListCreateAPIView: GET all + POST new
class StudentListCreateAPI(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# RetrieveUpdateDestroyAPIView: GET one + PUT + DELETE
class StudentRetrieveUpdateDeleteAPI(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'
