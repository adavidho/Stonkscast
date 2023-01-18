from django.db import models
import pandas as pd

# Model Definitions
class Inference(models.Model):

    stock_name = models.CharField(max_length=20, null=True)
    long_name = models.CharField(max_length=30, null=True)
    # market = models.CharField(max_length=20, default=None)
    wsb_rel = models.FloatField(null=True)
    logo = models.CharField(max_length=200, null=True)
    score = models.IntegerField(null=True)
    mcap  = models.IntegerField(null=True)
    gross_margins = models.FloatField(null=True)
    kgv = models.FloatField(null=True)

    def __str__(self) -> str:
        """
        Returns the string representation of a stock.
        Stock name and stock score.
        """
        return f"Stock name: {self.stock_name} \nScore: {self.score}"

    def top_stocks(self) -> dict:
        """
        Returns at least 6 stock Meeme Stocks from the database. 
        The stocks are in sorted be descending score. All positive classifications
        (a score between 70 and 100) are returned, if less then 6 stock have a 
        score higher than 70, also negativly classified stocks are returned.
        """
        return [vars(o) for i,o in enumerate(Inference.objects.order_by('-score')) if i<6 or vars(o)['score']>70]

    def update_model(self, data_path:str) -> None:
        """
        Removes all model datapoints from the database and loads 
        new data from a ';' seperated csv in the specified path.
        """
        # Remove all datapoints from the database
        Inference.objects.all().delete()
        # Read new data from csv file in 'data_path
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
        
        return None