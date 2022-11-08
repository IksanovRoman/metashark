from django.shortcuts import render

# Create your views here.
from rest_framework.generics import *
from rest_framework.permissions import IsAdminUser

from university.models import Direction_of_studying
from university.permissions import IsAdminOrReadOnly
from university.serializers import DirectionSerializer


class DirectionAPIViewCreate(ListCreateAPIView):
    queryset = Direction_of_studying.objects.all()
    serializer_class = DirectionSerializer
    permission_classes = (IsAdminOrReadOnly, )

class DirectionAPIUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Direction_of_studying.objects.all()
    serializer_class = DirectionSerializer
    permission_classes = (IsAdminUser,)