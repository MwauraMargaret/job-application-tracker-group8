from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import User, Company, Job, Application, Interview
from .serializers import UserSerializer, CompanySerializer, JobSerializer, ApplicationSerializer, InterviewSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class InterviewViewSet(ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
