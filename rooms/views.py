from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def all_rooms(request):
    now = datetime.now()
    #return HttpResponse(content=f"{now}<h1>Hello Sucker</h1>")
    return render(request, "all_rooms")