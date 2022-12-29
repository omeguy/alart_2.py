from binance.client import Client
import pandas as pd
import pandas_ta as ta
from datetime import datetime
import requests

WEBHOOK_URL = "https://discordapp.com/api/webhooks/1057814315475947571/X1Nv65Jo6o-VlIov7LYymif__Z5dF60sAe7AnLeKtgPjUJ9LaKF7f8Xk6AraOcaCNsLg"
webhook_url = "https://discordapp.com/api/webhooks/1057818187946795159/NdjTK9xfSx9_yNKqAnrWi47vgacROikJa5yiOZdLqsYdA91nPhdNIFCJbN3uOsdd5wko"

api_key = 'EcCJnX3k9X6eZaBLLIwDAcj1OugeqjXa0QOHl1nMTfvEcO77om7WcxycDnfvrCEo'
api_secret = 'ee8kKo6y9Ai9YofZMzZ3e36HziGQX916QpOVBurC3HUWnE2Z3fa4s5vSJYF6tbSN'  
symbol = 'BTCUSDT'
symbol2 = 'ETHUSDT'
client = Client(api_key, api_secret)

client = Client(api_key, api_secret)

def getdata(symbol):
    candles = client.get_klines(symbol=symbol, interval=Client.KLINE_INTERVAL_15MINUTE)
    df = pd.DataFrame(candles)
    df = df.rename(columns={0:'time', 1: 'open', 2: 'high', 3: 'low', 4: 'close', 5: 'volume'}).astype(float)
    df = df.drop(columns=[6,7,8,9,10,11])
    df['time'] = pd.to_datetime(df['time'])
    
    fma = df.ta.sma(21)
    sma = df.ta.sma(50)
    tma = df.ta.sma(200)
    adx = df.ta.adx()
    
    df = pd.concat([df, fma, sma, tma, adx], axis=1)

    return df

df = getdata(symbol)
df1 = getdata(symbol2)

last_row2 = df.iloc[-1]
last_row3= df2.iloc[-1]

def istrend(df):
    if last_row2['SMA_200'] > last_row2['SMA_50'] and last_row2['SMA_50'] > last_row2['SMA_21'] and last_row2['ADX_14'] >=20:
         message = f"**BTCUSDT**:DOWNTREND:The trend:**MAY_GO_SHORT**"
         print(message)
         payload = {
             "username": "Trend_alartBot",
             "content": message
             
         }
         requests.post(WEBHOOK_URL, json=payload)
        
    elif last_row2['SMA_200'] < last_row2['SMA_50'] and last_row2['SMA_50'] < last_row2['SMA_21'] and last_row2['ADX_14'] >=20:
         message = f"**BTCUSDT**:UPTREND:The trend:**MAY_GO_LONG**"
         print(message)
         payload = {
             "username": "Trend_alartBot",
             "content": message
             
         }
         requests.post(WEBHOOK_URL, json=payload)
    
    else:
         message = f"**BTCUSDT**:NO_CLEAR_TREND:**N**"
         print(message)
         payload = {
             "username": "Trend_alartBot",
             "content": message
             
         }
         requests.post(WEBHOOK_URL, json=payload)



def istrend(df1):
    if last_row3['SMA_200'] > last_row3['SMA_50'] and last_row3['SMA_50'] > last_row3['SMA_21'] and last_row3['ADX_14'] >=20:
         message = f"**ETHUSDT**:DOWNTREND:The trend:**MAY_GO_SHORT**"
         print(message)
         payload = {
             "username": "Trend_alartBot",
             "content": message
             
         }
         requests.post(WEBHOOK_URL, json=payload)
        
    elif last_row3['SMA_200'] < last_row3['SMA_50'] and last_row3['SMA_50'] < last_row3['SMA_21'] and last_row3['ADX_14'] >=20:
         message = f"**ETHUSDT**:UPTREND:The trend:**MAY_GO_LONG**"
         print(message)
         payload = {
             "username": "Trend_alartBot",
             "content": message
             
         }
         requests.post(WEBHOOK_URL, json=payload)
    
    else:
         message = f"**ETHUSDT**:NO_CLEAR_TREND:**N**"
         print(message)
         payload = {
             "username": "Trend_alartBot",
             "content": message
             
         }
         requests.post(WEBHOOK_URL, json=payload)
    

istrend(df)
istrend(df1)