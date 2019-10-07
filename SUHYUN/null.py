### 패키지 설치 
import pandas as pd #Analysis 
import matplotlib.pyplot as plt #Visulization
import seaborn as sns #Visulization
import numpy as np #Analysis 
from scipy.stats import norm #Analysis
from sklearn.preprocessing import StandardScaler #Analysis 
from scipy import stats #Analysis 
import warnings 
warnings.filterwarnings('ignore')

import gc

import os
import string
color = sns.color_palette()

from plotly import tools
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go

from sklearn import model_selection, preprocessing, metrics, ensemble, naive_bayes, linear_model
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import TruncatedSVD

pd.options.mode.chained_assignment = None
pd.options.display.max_columns = 999

import plotly.graph_objs as go

import time
import random

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

from lightgbm import LGBMRegressor

import eli5
from eli5.sklearn import PermutationImportance

import shap
train=pd.read_csv("./DACON_DATASET/train.csv")
train['Time']=pd.to_datetime(train['Time']).dt.strftime('%Y-%m-%d %H:%M')
train.head()
train.info()

# dateparse = lambda x : pd.datetime.strptime(x, '%Y-%m-%d %H:%M')
# train = pd.read_csv("./DACON_DATASET/train.csv", parse_dates={'datetime': ['date', 'time']}, date_parser=dateparse)
# train.shape

def mis_value_graph(data):  
    data = [
    go.Bar(
        x = data.columns,
        y = data.isnull().sum(),
        name = 'Counts of Missing value',
        textfont=dict(size=20),
        marker=dict(
        line=dict(
            color= generate_color(),
            #width= 2,
        ), opacity = 0.45
    )
    ),
    ]
    layout= go.Layout(
        title= '"Total Missing Value By Column"',
        xaxis= dict(title='Columns', ticklen=5, zeroline=False, gridwidth=2),
        yaxis= dict(title='Value Count', ticklen=5, gridwidth=2),
        showlegend=True
    )
    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig, filename='skin')
    
def generate_color():
    color = '#{:02x}{:02x}{:02x}'.format(*map(lambda x: random.randint(0, 255), range(3)))
    return color

mis_value_graph(train)

train.isnull().sum().sort_values().head(50)
series=train.notnull().sum().sort_values().head(50)
series.plot(kind='barh', axis=1)
pp.show


test=pd.read_csv("./DACON_DATASET/test.csv")
test['Time']=pd.to_datetime(test['Time']).dt.strftime('%Y-%m-%d %H:%M')
test.head()
test.notnull().sum().sort_values().head(50)

