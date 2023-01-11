from django.db import models
import pandas as pd

# Create your models here.
class Inference(models.Model):
    stock_name = models.CharField(max_length=20)
    long_name = models.CharField(max_length=30, default=None)
    # market = models.CharField(max_length=20, default=None)
    wsb_rel = models.FloatField(default=None)
    logo = models.CharField(max_length=200, default=None)
    score = models.IntegerField(default=None)
    mcap  = models.IntegerField(null=True)
    gross_margins = models.FloatField(null=True)
    kgv = models.FloatField(null=True)

    def __str__(self) -> str:
        return f"""
        Stock name: {self.stock_name} 
        Score: {self.score}
        """

    def top_stocks(self) -> dict:
        """Returns all Meeme Stocks with a positive classification, but at least 6."""

        return [vars(o) for i,o in enumerate(Inference.objects.order_by('-score')) if i<6 or vars(o)['score']>70]

    def update_model(self, data_path='D:\Documents\DHBW\Semester 3\Fallstudie\Data\AI_Data\data_ausgefüllt.csv') -> None:
        """Removes all model datapoints and loads new data from the specified path."""

        Inference.objects.all().delete()
        df = pd.read_csv(data_path, sep=";")
        for i in range(len(df)):
            Inference(
                stock_name=df.iloc[i].ticker,
                long_name = df.iloc[i].longName,
                # market=df.iloc[i].market,
                wsb_rel= round(df.iloc[i].WSB_relevance_gain_percent,2),
                logo=df.iloc[i].logoURL,
                score=int(df.iloc[i].prediction*100),
                mcap=float(df.iloc[i].MCAP.replace(",",".")),
                kgv=df.iloc[i].forwardPE,
                gross_margins=df.iloc[i].grossMargins,
            ).save()