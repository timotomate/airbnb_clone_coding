from django.views.generic import ListView, DetailView
from django.http import Http404
from django.urls import reverse
from django.shortcuts import render, redirect
from django_countries import countries
from . import models


class HomeView(ListView):
    """ HomeView Definition """
    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/detail.html", {'room' : room})
#     except models.Room.DoesNotExist:
#         #return redirect(reverse("core:home"))
#         raise Http404()

class RoomDetail(DetailView):
    """ 
    RoomDetail Definition 
    - HomeView 위에서 보듯이 반드시 view가 볼 model에 대해서 먼저 지정해주어야 함.
    """
    model = models.Room


def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))
    s_amenities = request.GET.get("amenities")
    s_facilities = request.GET.get("facilities")
    
    
    form = {
        "city": city,
        "s_room_type": room_type,
        "s_country": country,
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
    }

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
    }

    return render(request, "rooms/search.html", {**form, **choices})
    # {"city" : city}는 context를 의미함. context는 현재파일인 views.py에서 변수로 사용한 city 변수를 html 변수로 넘기는 것을 의미함
    # render 함수 = template인 html파일을 화면에 띄워줌
    # 파리미터 = request, template, 
    # countries변수는 django.countries 라이브러리에서 가져왔음