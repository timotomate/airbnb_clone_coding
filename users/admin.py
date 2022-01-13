from django.contrib import admin #기본제공
from django.contrib.admin.helpers import Fieldset
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
#https://docs.djangoproject.com/en/2.2/ref/contrib/admin/
#admin패널에서 user를 보고싶음. user를 컨트롤할 클래스는 CustomUserAdmin이 될것이다.
#@admin.register는 decorator이다. decorator은 클래스 바로 위에 위치해서 클래스의 위치를 알려주는 역할
#admin.site.register(models.User, CustomUserAdmin) decoator 대신에 클래스 맨 밑에다가 이거 적어도 가능
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """ Custom User Admin """
    
    fieldsets = UserAdmin.fieldsets + (("Custom Profile", 
    {"fields" : ("avatar", "gender", "bio", "birthdate", "language", "currency", "superhost")}),)

    #list_display = ('username', 'email', 'gender', 'language', 'currency', 'superhost')
    #list_filter = ('language', 'currency', 'superhost')