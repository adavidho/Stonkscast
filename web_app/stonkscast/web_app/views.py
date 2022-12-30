from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Inference

# Create your views here.
def index(request):
    template = loader.get_template('web_app/index.html')
    context = {
        'name': 'David',    
    }
    return HttpResponse(template.render(context, request))