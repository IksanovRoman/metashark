from rest_framework import serializers
from university.models import *


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction_of_studying
        fields = ("id", "direction")


class SubjectSerializerView(serializers.ModelSerializer):
    direction_name = serializers.CharField(source='direction_name.direction')

    class Meta:
        model = Subject
        fields = ("id", "subject_name", "direction_name")


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class GroupSerializerCreateView(serializers.ModelSerializer):
    direction = DirectionSerializer()

    class Meta:
        model = Education_group
        fields = ("id", "group_number", "direction")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education_group
        fields = "__all__"


class StudentSerializerView(serializers.ModelSerializer):
    studying_group = GroupSerializerCreateView()

    class Meta:
        model = Student
        fields = ("id", "first_name", "last_name", "patronymic", "studying_group")
        depth = 2


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
