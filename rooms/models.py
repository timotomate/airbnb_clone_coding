from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models #users의 앱(패키지) 사용
#def __str__ 사용하는 이유 https://neung0.tistory.com/51 참고


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """
    name = models.CharField(max_length=80)
    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class RoomType(AbstractItem):

    """ RoomType Object Definition"""
    
    class Meta:
        verbose_name = "Room Type"
        ordering = ['name']
    

class Amenity(AbstractItem):

    """ RoomType Object Definition """
     
    pass


class Facility(AbstractItem):

    """ Facility Model Definition """
    class Meta:
        verbose_name_plural = 'Facilities'
    

class HouseRule(AbstractItem):

    """ HouseRule MOdel Definition"""

    class Meta:
        verbose_name = "House Rule"

class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length = 80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE) #방을 지우면 사진도 같이 삭제되도록

    def __str__(self):
        return self.caption



# Create your models here.
class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    name = models.CharField(max_length=150)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=90)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    checkin = models.TimeField()
    checkout = models.TimeField()
    instant_book = models.BooleanField(default = False)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE) #users앱 사용(1:1 관계), CASCADE = USER삭제되면 ROOM도삭제
    room_type = models.ForeignKey("RoomType", blank=True, on_delete=models.SET_NULL, null = True) #다대다관계
    amenities = models.ManyToManyField("Amenity", blank=True)
    facilities = models.ManyToManyField("Facility", blank=True)
    house_rules = models.ManyToManyField("HouseRule", blank=True)


    def __str__(self):
        return self.name
