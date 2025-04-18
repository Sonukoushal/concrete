from django.urls import path
from .views import StudentListCreateAPI, StudentRetrieveUpdateDeleteAPI

urlpatterns = [
    path('students/', StudentListCreateAPI.as_view()),         # GET all, POST
    path('students/<int:id>/', StudentRetrieveUpdateDeleteAPI.as_view()),  # GET one, PUT, DELETE
]
