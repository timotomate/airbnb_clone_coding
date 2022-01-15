from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):

    """ Time Stamped Model """
    
    created = models.DateTimeField(auto_now_add=True) #객체가 처음 생성될 때 자동으로 현재 시각이 필드값
    updated = models.DateTimeField(auto_now_add=True) 
    
    class Meta:
        abstract = True