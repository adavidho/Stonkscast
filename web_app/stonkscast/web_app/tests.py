from django.test import TestCase
from .models import Inference

#Automate testing for web_app functioalities

def create_stock(stock_name, score):
    """
    Create a Samlpe stock with a given 'score' (number between 0 and 100 
    and 'stock_name' which is the ticker of the sample stock.
    """
    return Inference.objects.create(stock_name=stock_name, score=score)

class InferenceModelTests(TestCase):

    def test_all_positive_top_stocks(self):
        """
        Test if top_stocks() returns a all positive Meemestocks 
        (score higher than 70).
        """
        stock_names = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHI']
        stocks_list = [create_stock(stock_name=stock_names[i],score=i+71,) for i in range(7)]
        stocks = Inference()
        self.assertIs(
            len(stocks.top_stocks()), 
            7
        )

    def test_all_negative_top_stocks(self):
        """
        Test if top_stocks() returns at least 6 stocks, 
        even if they are not positive (score higher than 70).
        """
        stock_names = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHI']
        stocks_list = [create_stock(stock_name=stock_names[i],score=i,) for i in range(7)]
        stocks = Inference()
        self.assertIs(
            len(stocks.top_stocks()), 
            6
        )

