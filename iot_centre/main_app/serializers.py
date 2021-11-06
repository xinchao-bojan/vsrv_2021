from rest_framework import serializers

from .models import Room, MotionData


class RoomSerializerInput(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('title', 'acceptable_motion_level')


class MotionDataSerializerInput(serializers.ModelSerializer):
    class Meta:
        model = MotionData
        fields = ('room', 'motion')


class MotionDataSerializer(serializers.ModelSerializer):
    room = serializers.StringRelatedField()

    class Meta:
        model = MotionData
        fields = ('room', 'motion', 'date')


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id','title', 'acceptable_motion_level')
