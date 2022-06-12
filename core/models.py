from django.db import models


class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)  # 생성될때 마다 그 시간 남김
    updated = models.DateTimeField(auto_now=True)  # 저장될때마다 그 시간 남김

    class Meta:
        abstract = True  # db에 안올라가고 코드상에서만 보임
