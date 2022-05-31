from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Student, Gender
from main.serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    #queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Student.objects.all()[::3]
        return Student.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def gender(self, request, pk=None):
        genders = Gender.objects.get(pk=pk)
        return Response({'genders': genders.name})



















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



