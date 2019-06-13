from django.db import models

# Create your models here.
class LiveRoom(models.Model):
    room_home = models.CharField(max_length=100)
    room_id = models.IntegerField()
    room_name = models.TextField()
    user_id = models.IntegerField()
    user_name = models.TextField()
    room_kind = models.TextField()
    room_url = models.TextField()
    room_kind = models.CharField(max_length=20)
    room_olnum = models.IntegerField()
    room_usertag = models.TextField()
