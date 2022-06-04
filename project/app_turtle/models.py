from django.db import models
from datetime import datetime


# Create your models here.
class Posecheck(models.Model):
    time = datetime.now()
    pose_check = models.CharField(max_length=30)
    # 예를들어: 하루에 측정한 횟수 중 몇 번이나 거북목을 했는지 확인
    todays_score = models.IntegerField()

    #  User는 Account 추가 후 보충
