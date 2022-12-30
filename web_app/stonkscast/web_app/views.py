from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Inference

# Create your views here.
def index(request):
    template = loader.get_template('web_app/index.html')
    stocks = Inference()
    context = {
        'top_stocks': stocks.top_stocks()[:6],    
    }
    return HttpResponse(template.render(context, request))