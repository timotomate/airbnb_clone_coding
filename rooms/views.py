from django.shortcuts import render
from math import ceil #최소 정수 출력 함수
from . import models


# Create your views here.
def all_rooms(request):
    page = int(request.GET.get("page",  1))
    page = int(page or 1)
    print(request.GET)# 터미널 창에서 확인용
    print(request.GET.get("page"))# 터미널 창에서 확인용
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit]
    page_count = ceil(models.Room.objects.count() / page_size)
    return render(
        request,
        "rooms/home.html",
        {
            "potato": all_rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count),
        },
    )