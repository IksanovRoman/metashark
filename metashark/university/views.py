from django.shortcuts import render

# Create your views here.
from rest_framework.generics import *
from rest_framework.permissions import *

from university.models import *
from university.permissions import IsAdminOrReadOnly
from university.serializers import *


class DirectionAPIViewCreate(ListCreateAPIView):
    queryset = Direction_of_studying.objects.all()
    serializer_class = DirectionSerializer
    permission_classes = (IsAdminOrReadOnly,)


class DirectionAPIUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Direction_of_studying.objects.all()
    serializer_class = DirectionSerializer
    permission_classes = (IsAdminUser,)


class SubjectAPIView(ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializerView


class SubjectAPICreate(CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (IsAdminUser,)


class SubjectAPIUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (IsAdminUser,)


class StudentAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializerView


class StudentAPICreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated,)


class StudentAPIUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated,)

class GroupAPIView(ListAPIView):
    queryset = Education_group.objects.all()
    serializer_class = GroupSerializerCreateView
    permission_classes = (IsAuthenticatedOrReadOnly,)

class GroupAPICreate(CreateAPIView):
    queryset = Education_group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class GroupAPIUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Education_group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)