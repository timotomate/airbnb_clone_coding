from django.contrib.auth.models import AbstractUser
from django.db import models # 기본제공

# Create your models here.
# https://docs.djangoproject.com/en/4.0/ref/models/fields/

class User(AbstractUser): #여기다가 코드 작성하면 장고가 아래 항목에 따라서 자동으로 Form 생성해줌
    """ Custon User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other")
    )

    LANGUAGE_ENGLISH = "english"
    LANGUAGE_KOREAN = "korean"

    LANGUAGE_CHOICES =(
        (LANGUAGE_ENGLISH, "en"),
        (LANGUAGE_KOREAN, "kr")
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCH_CHOICES = (
        (CURRENCY_USD, "usd"),
        (CURRENCY_KRW, "krw")
    )

    avatar = models.ImageField(blank=True)
    gender = models.CharField(choices = GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank = True, null=True)
    language = models.CharField(choices = LANGUAGE_CHOICES, max_length = 6, blank = True)
    currency = models.CharField(choices=CURRENCH_CHOICES, max_length = 3, blank = True)
    superhost = models.BooleanField(default=False)

    # def __str__(self):
    #     return "SEXY"