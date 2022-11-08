from rest_framework import serializers

from university.models import Direction_of_studying


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction_of_studying
        fields = "__all__"
