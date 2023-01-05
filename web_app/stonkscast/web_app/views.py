from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Inference
from yahoo_fin import stock_info as si



# Create your views here.
def index(request):
    template = loader.get_template('web_app/index.html')
    stocks = Inference()
    top_stocks = stocks.top_stocks()
    for stock in top_stocks:
        stock['price'] = round(si.get_live_price(stock['stock_name']), 1)
    context = {
        'top_stocks': top_stocks,  
    }
    return HttpResponse(template.render(context, request))