from django.template import loader
from django.http import HttpResponse
import json


# Create your views here.
def index(request):
    template = loader.get_template("ryza.html")
    context = {'ryza_data': json.dumps(json.load(open('jsons/ryza.json')))}
    context = {'ryza_data': open('jsons/ryza.json').read()}
    return HttpResponse(template.render(context, request))
