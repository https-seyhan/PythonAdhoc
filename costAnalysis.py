import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt
import  seaborn as sb
import os
sb.set(style="whitegrid")
os.chdir('/home/saul/Desktop')

pd.options.display.float_format = '{:.1f}'.format
figsize = (1500 / 50, 400 / 50)
fig, ax = plt.subplots(1, 1, figsize=figsize)

cost = pd.read_csv('spend.csv', sep=',')

#sb.boxplot(y="cost", data=cost)
#cost.set_index('date', inplace=True)
print(cost.describe())
#cost.boxplot(cost['cost'])
cost['date'] = pd.to_datetime(cost.date)
print(cost.columns)
print(cost.info())
cost.set_index('date')
cost.sort_values(by='date', inplace=True)
print(cost['date'])
print('Total Market Cost is  %0.1f in % 2d days with Daily spend is %0.1f' % (cost['cost'].sum(), (cost['date'].max() - cost['date'].min()).days,
                                                                              cost['cost'].sum() / (cost['date'].max() - cost['date'].min()).days))
#cost.plot(cost['cost'])
#sb.lineplot(x="date", y="cost", data=cost)
#sb.distplot(cost)
#ax.plot(cost['cost'])
ax = sb.barplot(x="type", y="cost", data=cost, estimator=sum)
#g = sb.catplot(x="type", y="cost", hue="market", data=cost,height=6, kind="bar", palette="muted")
#g.despine(left=True)
#g.set_ylabels("Cost")
#g.set_xlabels(("Cost Type"))

plt.show()
#cost.sort(cost.date)
#cost['newdate']