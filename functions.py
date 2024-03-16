import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from statsmodels.tsa.stattools import adfuller



def plot_outliers(outliers, data, method = 'LOF', halignment = 'right',
                  valignment = 'bottom', labels = False):
  plt.figure(figsize=(16,8))
  ax = data.plot(alpha = 0.6)
  if labels:
    for i in outliers['value'].items():
      plt.plot(i[0],i[1],'rx')
      plt.text(i[0],i[1],f'{i[0].date()}',
               horizontalalignment=halignment,
               verticalalignment= valignment)
  else:
    data.loc[outliers.index].plot(ax = ax,style ='rx')
  plt.title(f'Stock return - {method}')
  plt.xlabel('date')
  plt.ylabel('# of passengers')
  plt.legend(['Stock return','outliers'])
  plt.show()

def is_stationary(ts):
  pvalue = adfuller(ts)[1]
  if pvalue < 0.05:
    return f'the time series is stationary'
  else: 
    return f'the time series is not stationary'

def run_ts_plot(y, title, xlabel="time", ylabel = None,figsize=(16,8)):
      plt.figure(figsize=(16,6))
      plt.plot(y)
      plt.title(title)
      plt.xlabel(xlabel)
      plt.ylabel(ylabel)


