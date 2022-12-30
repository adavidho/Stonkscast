import numpy as np
import pandas as pd
import yfinance as yf
from wsb_extraction import get_wc_ts

# Ticker definition
tickers_meme = ["GME", "AMC", "BBBY", "FIZZ","BB","NOK","PLTR","SPCE","CLOV","ZOM","SNDL","TSLA","WISH", "CRSR","WKHS","UWMC","CLF","ATOM","APE","WEN","HHC","DC","DTE","KE","AA","HOOD","TLRY","UNIT","SNAP","NRDY","LL"]
tickers_no_meme = ["ALOR","SCAQ","RXST","HCAR","FACT", "EVC","TETC","GCO", "ALLK","EVBG","TSLX","GCMG","VVNT","LIVN","TENB","ITCI","RRC","USFD","RRX","PSO","VIPS","EXAS","HUBS","MOS","AEE","FMX","ENB","JNJ","SOUNW","DS","SCTL","CARV","ETW","DHT","CLIN","WWW","TPIC","GNK","BKSC","AU","RFP","ENO","FROG","COWNL","CSSEN","ODC","NBTB","IMCR","HIG","RL","VEEV","MCD","ARGX","LRCX","WTM","SBSW","CLAR","SBBA","POST","COST","MDLZ","COKE","INDO","PBT","HHGCW","EOD","DRAYU","BANX","BRP","CNCE","PACB","AMPH","OIS","TWI","FREY","AGNC","MMAT","INFY","PCTY","USM","GNE","AGI","AEFC","NPO","GOOGL","CVS","LMT","FCX","ED","PNR","PRG"] 

# NOTE: Remove after Debugging
# tickers_meme = tickers_meme[:1]
# tickers_no_meme = tickers_no_meme[:1]

final_frame = pd.DataFrame()

# List of dates to get course & WSB keyword density
date_list = ["2020-12-01", "2020-12-16", "2021-01-04", "2021-01-20"]

for t in tickers_meme+tickers_no_meme:
    # Stock price & label
    stock_price = pd.Series(yf.Ticker(t).history(start="2020-12-01")["Open"])
    stock_price.index = pd.DatetimeIndex([idx.date() for idx in stock_price.index])
    appendix = {
        "meme_stock": t in tickers_meme,
        "ticker": t,
    }

    # Get Reddit wsb keyword denisty time series
    wsb_density = get_wc_ts(t)

    for date in date_list:
        appendix[f"price_{date}"] = stock_price.get(date, np.nan)
        appendix[f"wsv_{date}"] = wsb_density.get(date, np.nan)

    appendix |= yf.Ticker(t).info

    final_frame = final_frame.append(appendix, ignore_index=True)
    print("Finished entries for ticker: ", t)

# Drop cols with (nearly) no value
cols_to_drop = ["preMarketPrice", "longBusinessSummary", "phone", "companyOfficers", "website",\
        "address1", "address2", "exchangeTimezoneName", "gmtOffSetMilliseconds", "symbol", "messageBoardId",\
        "annualHoldingsTurnover", "lastSplitDate", "lastSplitFactor", "morningStarOverallRating", "category",\
        "toCurrency", "expireDate", "algorithm", "circulatingSupply", "currency", "lastMarket", "maxSupply",\
        "fromCurrency", "coinMarketCapLink"]

for column in cols_to_drop:
    vc = final_frame[column].value_counts()
    print(f"Feature {column} has value counts: \n{vc}:")

# Drop cols
final_frame.drop(cols_to_drop, axis=1, inplace=True)

print("\n--------- Final DataFrame ---------\n")
print(final_frame.head(20))


final_frame.to_csv("stock_data.csv")


"""
normal_stocks = ["GME", "AMC", "BBBY", "FIZZ","BB","NOK","PLTR","SPCE","CLOV","ZOM","SNDL","TSLA","WISH", "CRSR","WKHS","UWMC","CLF","ATOM","APE","WEN","HHC","DC","DTE","KE","AA","HOOD","TLRY","UNIT","SNAP","NRDY","LL","ALOR","SCAQ","RXST","HCAR","FACT", "EVC","TETC","GCO", "ALLK","EVBG","TSLX","GCMG","VVNT","LIVN","TENB","ITCI","RRC","USFD","RRX","PSO","VIPS","EXAS","HUBS","MOS","AEE","FMX","ENB","JNJ","SOUNW","DS","SCTL","CARV","ETW","DHT","CLIN","WWW","TPIC","GNK","BKSC","AU","RFP","ENO","FROG","COWNL","CSSEN","ODC","NBTB","IMCR","HIG","RL","VEEV","MCD","ARGX","LRCX","WTM","SBSW","CLAR","SBBA","POST","COST","MDLZ","COKE","INDO","PBT","HHGCW","EOD","DRAYU","BANX","BRP","CNCE","PACB","AMPH","OIS","TWI","FREY","AGNC","MMAT","INFY","PCTY","USM","GNE","AGI","AEFC","NPO",
"GOOGL","CVS","LMT","FCX","ED","PNR","PRG"]
"""