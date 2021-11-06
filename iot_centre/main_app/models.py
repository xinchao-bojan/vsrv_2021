from django.db import models


class Room(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название комнаты', unique=True)
    acceptable_motion_level = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class MotionData(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    motion = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def need_to_alarm(self):
        return self.motion > self.room.acceptable_motion_level

    def __str__(self):
        return f'{self.room.title} {self.motion} at {self.date}'
