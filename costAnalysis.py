import pandas as pd
import time
from datetime import datetime
from datetime import date
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

#print('Dates before modification {}'.format(cost['date']))

cost['newDate'] = cost['date'].apply(lambda x: str(x) + '20')
cost['newDate2'] = cost['newDate'].apply(lambda x: datetime.strptime(x, '%d/%m/%Y'))
print('Date2!!!!!', cost['newDate2'])
#cost.boxplot(cost['cost'])
cost['date'] = pd.to_datetime(cost.date)
cost['newDate2'] = pd.to_datetime(cost.newDate2)

cost.set_index('newDate2')
cost.sort_values(by='newDate2', inplace=True)

#todays date
tday = date.today()

min_time = datetime.min.time()
current_datetime = datetime.combine(tday, min_time)

#timestamp = time.mktime(time.strptime(tday, '%Y-%m-%d'))

#print(cost['date'])
#print('From the start date of ':%Y-%m-%d' Total Market Cost is  %0.1f in % 2d days with Daily spend is %0.1f' % (cost['newDate2'].min(), cost['cost'].sum(), (cost['newDate2'].max() - cost['newDate2'].min()).days,
#                                                                              cost['cost'].sum() / (cost['newDate2'].max() - cost['newDate2'].min()).days))

print('From the start date of Total Market Cost is  %0.1f in % 2d days with Daily spend is %0.1f' % (cost['cost'].sum(), (current_datetime - cost['newDate2'].min()).days,
                                                                              cost['cost'].sum() / (current_datetime - cost['newDate2'].min()).days))

print("Food Cost Descriptive Analysis ", cost['cost'][cost['type'] == 'food'].describe())
#print("Type ", type(cost['newDate2'].max()))

#sb.lineplot(x="date", y="cost", data=cost)
#sb.distplot(cost)
#ax.plot(cost['cost'])
#ax = sb.barplot(x="type", y="cost", data=cost, estimator=sum)
ax = sb.boxplot(x='type', y='cost', data=cost)
#g = sb.catplot(x="type", y="cost", hue="market", data=cost,height=6, kind="bar", palette="muted")
#g.despine(left=True)
#g.set_ylabels("Cost")
#g.set_xlabels(("Cost Type"))

plt.show()
#cost.sort(cost.date)
#cost['newdate']