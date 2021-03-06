from django.db import models
from django.urls import reverse
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
    class Meta:
        verbose_name_plural = 'Amenities'


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
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE) #방을 지우면 사진도 같이 삭제되도록

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
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default = False)
    host = models.ForeignKey("users.User", related_name = "rooms", on_delete=models.CASCADE)#users 폴더의 user
    room_type = models.ForeignKey("RoomType", related_name = "rooms", blank=True, on_delete=models.SET_NULL, null = True)
    #1 User, Many Rooms
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)


    def __str__(self):
        return self.name

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews))
        return 0

    #admin 패널에서 바로 프론트엔드 부분으로
    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs = {'pk':self.pk})