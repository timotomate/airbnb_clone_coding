from django.views.generic import ListView, DetailView
from django.http import Http404
from django.urls import reverse
from django.shortcuts import render, redirect
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
    city = request.GET.get("city")
    city = str.capitalize(city)
    return render(request, "rooms/search.html", {"city" : city})
    # {"city" : city}는 context를 의미함. context는 현재파일인 views.py에서 변수로 사용한 city 변수를 html 변수로 넘기는 것을 의미함
    # render 함수 = template인 html파일을 화면에 띄워줌
    # 파리미터 = request, template, 