from rest_framework import serializers

from university.models import *


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction_of_studying
        fields = "__all__"


class SubjectSerializerView(serializers.ModelSerializer):
    direction_name = serializers.CharField(source='direction_name.direction')

    class Meta:
        model = Subject
        fields = ("id", "subject_name", "direction_name")


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"
