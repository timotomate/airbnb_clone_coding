from django.db import models
from core import models as core_models

# https://www.airbnb.co.kr/wishlists/ 이거 참고

class List(core_models.TimeStampedModel):

    """ LIst Model Definition """

    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.User", related_name="lists",on_delete=models.CASCADE)
    rooms = models.ManyToManyField("rooms.Room", related_name="lists",blank=True)#list 하나에 여러 room이 있을 수 있음.

    def __str__(self):
        return self.name