import pandas as pd

train=pd.read_csv("./DACON_DATASET/train.csv")
train['Time']=pd.to_datetime(train['Time']).dt.strftime('%Y-%m-%d %H:%M')
train=train.set_index('Time')
train.head()
train.info()

# <class 'pandas.core.frame.DataFrame'>
# Index: 16909 entries, 2016-07-26 11:00 to 2018-06-30 23:00
# Columns: 1300 entries, X692 to X1163
# dtypes: float64(1300)
# memory usage: 167.8+ MB

train_cut=train.loc['2018-02-15 00:00':'2018-04-30 00:00', "X452"]
train_cut.head()

import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(30,10))
train_cut.plot()

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

plot_acf(train_cut)
plot_pacf(train_cut)
plt.figure(figsize=(20,4))
plt.show()

# 별 차이가 없어서 차분 진행 안 함.
# diff_1 = train_cut.diff(periods=1).iloc[1:]
# diff_1.plot()
# plt.figure(figsize=(30,10))
# plt.show()
# plot_acf(diff_1)
# plot_pacf(diff_1)

from statsmodels.tsa.arima_model import ARIMA, ARIMAResults

model = ARIMA(train_cut, order=(1,1,0))
model_fit = model.fit(trend = 'c', full_output = True, disp=1)
print(model_fit.summary())