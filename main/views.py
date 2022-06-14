from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Student, Gender, User
from main.serializers import StudentSerializer, UserSerializer


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Student.objects.all()
        return Student.objects.filter(pk=pk)


class UserViewSet(viewsets.ModelViewSet):
        serializer_class = UserSerializer

        def get_queryset(self):
            pk = self.kwargs.get('pk')
            if not pk:
                return User.objects.all()
            return User.objects.filter(pk=pk)










# class StudentAPIView(generics.ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
# class StudentsAPIList(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# class StudentAPIUpdate(generics.UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# class StudentAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer



