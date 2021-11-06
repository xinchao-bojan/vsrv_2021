from django.utils.timezone import make_aware
from rest_framework.views import APIView
from rest_framework import status
from .serializers import MotionDataSerializerInput, MotionDataSerializer, RoomSerializer
from .models import Room, MotionData
from rest_framework.response import Response
from dateutil.parser import parse
from django.db.models import Q
from django.core.mail import send_mail


class CreateMotionData(APIView):
    def post(self, request):
        serializer = MotionDataSerializerInput(data=request.data)
        if serializer.is_valid():
            instance = serializer.save(room=Room.objects.get(title=request.data['room']))
            if instance.need_to_alarm():
                send_mail(
                    'СИГНАЛИЗАЦИЯ',
                    f'Уровень в комнате {instance.room} превысил норму и составляет {instance.motion}',
                    'bojan.alarm@mail.ru',
                    ['sk.schooldude@gmail.com'],
                )
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetMotionDataByRoom(APIView):
    def get(self, request, room_id):
        date_query = Q()
        if request.GET.get('date_start', None) is not None:
            date_start = make_aware(parse(request.GET.get('date_start', None), dayfirst=True))
            date_query &= Q(date__date__gte=date_start.date())
        if request.GET.get('date_end', None) is not None:
            date_end = make_aware(parse(request.GET.get('date_end', None), dayfirst=True))
            date_query &= Q(date__date__lte=date_end.date())
        serializer = MotionDataSerializer(MotionData.objects.filter(Q(room__id=room_id) & date_query).order_by('-date'),
                                          context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetAllRooms(APIView):
    def get(self, request):
        serializer = RoomSerializer(Room.objects.all().order_by('title'),
                                    context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
