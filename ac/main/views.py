import json

from django.db.models import Q
from django.shortcuts import render, HttpResponse

from .models import Test


# Create your views here.
def index(request):
    return render(request, 'main.html')


def get_places(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        places = Test.objects.filter(Q(country__icontains=q) | Q(name__icontains=q))
        results = []
        for pl in places:
            place_json = pl.country + ", " + pl.name
            results.append(place_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
