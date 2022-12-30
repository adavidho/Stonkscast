from django.db import models

# Create your models here.
class Inference(models.Model):
    stock_name = models.CharField(max_length=20)
    market = models.CharField(max_length=20)
    logo = models.CharField(max_length=200, default=None)
    score = models.IntegerField()

    def __str__(self) -> str:
        return f"""
        Stock name: {self.stock_name} 
        Market: {self.market}
        Score: {self.score}
        Logo: {self.logo}
        """

    def top_stocks(self) -> dict:
        return [vars(o) for o in Inference.objects.order_by('-score')]


# Import CSV to model
# df = pd.read_csv("stock_data.csv")[['market', 'logo_url', 'ticker']].dropna()
# for i in range(10):
#     Inference(
#         stock_name=df.iloc[i].ticker,
#         market=df.iloc[i].market,
#         logo=df.iloc[i].logo_url,
#         score=df.iloc[i].score,
#     ).save()