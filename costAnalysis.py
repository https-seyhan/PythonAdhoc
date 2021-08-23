import pandas as pd
import numpy as np
import time
import os
import seaborn as sb
from datetime import datetime
from datetime import date
from matplotlib import pyplot as plt

def setEnvironment():
    #sb.set(style="whitegrid")
    plt.style.use('seaborn-whitegrid')
    os.chdir('/home/saul/Desktop')
    pd.options.display.float_format = '{:.1f}'.format
    #figsize = (1500 / 50, 400 / 50)
    #fig, (ax1, ax2) = plt.subplots(ncols=1,nrows=2, figsize=figsize)

def importData():
    cost = pd.read_csv('spend.csv', sep=',')
    #cost.set_index('date', inplace=True)
    print(cost.describe())
    return cost

def shapeData(cost):
    cost['newDate'] = cost['date'].apply(lambda x: str(x) + '20')
    cost['newDate2'] = cost['newDate'].apply(lambda x: datetime.strptime(x, '%d/%m/%Y'))
    #print('Date2!!!!!', cost['newDate2'])
    cost['date'] = pd.to_datetime(cost.date)
    cost['newDate2'] = pd.to_datetime(cost.newDate2)
    cost.set_index('newDate2')
    cost.sort_values(by='newDate2', inplace=True) #Sort by Date
    #todays date
    tday = date.today()
    min_time = datetime.min.time()
    current_datetime = datetime.combine(tday, min_time)
    #timestamp = time.mktime(time.strptime(tday, '%Y-%m-%d'))
    #print(cost['date'])
    #print('From the start date of ':%Y-%m-%d' Total Market Cost is  %0.1f in % 2d days with Daily spend is %0.1f' % (cost['newDate2'].min(), cost['cost'].sum(), (cost['newDate2'].max() - cost['newDate2'].min()).days,
    #                                                                              cost['cost'].sum() / (cost['newDate2'].max() - cost['newDate2'].min()).days))
    print('Between ', cost["newDate2"].min().strftime("%d/%m/%Y"), ' and ', date.today().strftime("%d/%m/%Y"),  'Total Market Cost is  %0.1f in % 2d days (%2d months) with Daily spend is %0.1f' % ( cost['cost'].sum(), (current_datetime - cost['newDate2'].min()).days, (current_datetime - cost['newDate2'].min()).days/30,
                                                                             cost['cost'].sum() / (current_datetime - cost['newDate2'].min()).days))
    print('Between ', cost["newDate2"].min().strftime("%d/%m/%Y"), ' and ', date.today().strftime("%d/%m/%Y"),  ' Food Cost is  %0.1f in % 2d days (%2d months) with Daily spend is %0.1f' % (cost['cost'][cost['type'] == 'food'].sum(), (current_datetime - cost['newDate2'].min()).days, (current_datetime - cost['newDate2'].min()).days/30,
                                                                              cost['cost'][cost['type'] == 'food'].sum() / (current_datetime - cost['newDate2'].min()).days))
    print('Between ', cost["newDate2"].min().strftime("%d/%m/%Y"), ' and ', date.today().strftime("%d/%m/%Y"),  ' Alcohol Cost is  %0.1f in % 2d days (%2d months) with Daily spend is %0.1f' % (cost['cost'][cost['type'] == 'alcohol'].sum(), (current_datetime - cost['newDate2'].min()).days, (current_datetime - cost['newDate2'].min()).days/30,
                                                                              cost['cost'][cost['type'] == 'alcohol'].sum() / (current_datetime - cost['newDate2'].min()).days))
    print("Food Cost Descriptive Analysis ", cost['cost'][cost['type'] == 'food'].describe())
    #print("Type ", type(cost['newDate2'].max()))
    print("Start Date !!!!!!!!! ", cost['newDate2'].min())
    #sb.lineplot(x="date", y="cost", data=cost)
    #sb.distplot(cost)
    #ax.plot(cost['cost'])
    #ax = sb.barplot(x="type", y="cost", data=cost, estimator=sum)

def plotSubPlots(cost):
    #figsize = (1500 / 50, 400 / 50)
    median = cost['cost'].median()
    mean = cost['cost'].mean()
    mode=cost['cost'].mode().to_numpy()[0]
    
    plt.subplot(221)
    sb.distplot(cost['cost'])
    plt.axvline(median, color='g', linestyle='--')
    plt.axvline(mean, color='r', linestyle = '--')
    plt.axvline(mode, color='b', linestyle = '--')
    plt.legend({'Mean':mean,'Median':median, 'Mode':mode})
    plt.subplot(222)
    sb.boxplot(x='type', y='cost', data=cost)
    # g = sb.catplot(x="type", y="cost", hue="market", data=cost,height=6, kind="bar", palette="muted")
    # g.despine(left=True)
    # g.set_ylabels("Cost")
    # g.set_xlabels(("Cost Type"))
    plt.subplot(212)
    sb.boxplot(x='market', y='cost', data=cost)
    cost_max = int(np.round(max(cost['cost']), 0))
  
    ticks = [0, int(np.round(0.1 * cost_max, 0)), int(np.round(0.2 * cost_max, 0)), int(np.round(0.3 * cost_max, 0)),
             int(np.round(0.4 * cost_max, 0)),
             int(np.round(0.5 * cost_max, 0)), int(np.round(0.6 * cost_max, 0)), int(np.round(0.7 * cost_max, 0)),
             int(np.round(0.8 * cost_max, 0)), int(np.round(0.9 * cost_max, 0)), int(np.round(cost_max, 0))]
    plt.yticks(ticks, ticks)
    print("Max Cost ", int(np.round(max(cost['cost']), 0)))
    typeCount = cost['type'].value_counts()
    plt.show()

def plotBars(cost):
    plt.figure()
    sb.countplot(x="type", data=cost)
    plt.figure()
    sb.countplot(x="market", data=cost)
    plt.show()

def plotDists(cost):
    #plt.figure(figsize=figsize)
    fig, ax = plt.subplots(figsize=figsize)
    wolli = cost[cost['market']=='wolli']
    #print(wolli.describe())
    coles = cost[cost['market']=='coles']
    #print(coles.describe())
    #wolli['cost'].plot.hist(histtype='step', bins=4)
    wolli['cost'].plot.density()
    #plt.legend(cost['market'])
    coles['cost'].plot.density()
    plt.xlabel('Coles and Wolli Costs')
    markets = cost['market'][(cost['market']=='wolli') | (cost['market']=='coles')].unique()
    print(markets)
    print("Series ", pd.Series(cost['market'][(cost['market']=='wolli') | (cost['market']=='coles')].get_values()))
    #legends = pd.DataFrame({coles:'coles', wolli:'wolli'})
    plt.legend(markets)
    plt.show()

def plotBox(cost):
    wolli = cost['cost'][cost['market'] == 'wolli']
    print(wolli.describe())
    coles = cost['cost'][cost['market'] == 'coles']
    print(coles.describe())
    markets = pd.DataFrame({'coles': coles, 'wolli': wolli})
    #markets.boxplot()
setEnvironment()
#cost = importData()
shapeData(importData())
plotSubPlots(importData())
#plotDists(cost)
#plotDists(cost)
#plotBox(cost)
