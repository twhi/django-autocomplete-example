import json

from django.db.models import Q
from django.shortcuts import render, HttpResponse

from .forms import MainForm
from .models import Test


def receive_form(request):

    if request.POST.get('action') == 'post':
        players = request.POST.get('title')
        selected_players = json.loads(request.POST.get('selected'))
        print(selected_players)
        # test for error
        error = False
        if error:
            response = HttpResponse({"error": "there was an error"})
            response.status_code = 500
            return response

    return HttpResponse('yes')

def index(request):
    m = MainForm()
    context = {
        'main_form': m
    }
    return render(request, 'main.html', context)


def get_places(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        places = Test.objects.filter(Q(country__icontains=q) | Q(name__icontains=q))
        results = []
        for pl in places:
            label = pl.country + ", " + pl.name
            country = pl.country 
            name = pl.name
            results.append({
                'label': label,
                'country': country,
                'name': name
            })
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
