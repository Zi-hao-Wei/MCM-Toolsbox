import pandas as pd 
from fbprophet import Prophet
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv('ChinaBank.csv',parse_dates=['Date'],usecols=['Date','Close'])
df = df.rename(columns={'Date':'ds','Close':'y'})


maxNum=df['y'].max()
minNum=df['y'].min()

df['y']=df['y'].apply(lambda x: (x - maxNum) / (maxNum - minNum))


# print(df)

train = df[:300]
# test = df[:200]

# print(test)
# print(test)


m=Prophet()
m.fit(train)
future = m.make_future_dataframe(periods=50)
forecast=m.predict(future)
# print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())
m.plot(forecast)
print(future)
print(forecast)

plt.plot(df['ds'],df['y'],label='True')
plt.plot(forecast['ds'],forecast['yhat'],label='Predict')
plt.show()