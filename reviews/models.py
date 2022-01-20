from django.db import models
from core import models as core_models #core폴더의 models.py파일을 import 할껀데 이름은 core_models로

# Create your models here.

class Review(core_models.TimeStampedModel):
    
    """ Reviews Model Definition """

    review = models.TextField(max_length=1000, blank=True)
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.User", related_name="reviews", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", related_name="reviews", on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.review} - {self.room}'
        #return self.room.host.username #room클래스의 변수 room -> host(user.User) -> Users클래스의 멤버변수 username에 접근
        