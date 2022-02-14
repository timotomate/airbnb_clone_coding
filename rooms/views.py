from django.shortcuts import render, redirect
from math import ceil #최소 정수 출력 함수
from . import models
from django.core.paginator import Paginator,EmptyPage

# Create your views here.
def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=3)
    #rooms = paginator.get_page(page)
    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", {"page" : rooms})
    except Exception:
        return redirect("/")