import pandas as pd
import os
import numpy as np
import time
import sys
import seaborn as sb
from datetime import datetime
from datetime import date
from matplotlib import pyplot as plt

# Generate Spending class
class Spending():
    def __init__(self):    
        sb.set(style="whitegrid")
        pd.options.display.float_format = '{:.1f}'.format
        os.chdir('/home/saul/Desktop')
        self.spend = pd.read_csv('spend.csv', sep=',')
        self.figsize = (1500 / 50, 400 / 50)
        self.__readFile()
  
    def __readFile(self):
        print(self.spend.describe())
        # print('Dates before modification {}'.format(cost['date']))
        self.spend['newDate'] = self.spend['date'].apply(lambda x: str(x) + '20')
        self.spend['newDate2'] = self.spend['newDate'].apply(lambda x: datetime.strptime(x, '%d/%m/%Y'))
        self.spend['date'] = pd.to_datetime(self.spend.date)
        self.spend['newDate2'] = pd.to_datetime(self.spend.newDate2)
        self.spend.set_index('newDate2')
        self.spend.sort_values(by='newDate2', inplace=True)

    def plotSubPlots(self):
        self.fig, self.ax = plt.subplots(figsize=self.figsize)
        plt.subplot(221)
        ax1 = sb.distplot(self.spend['cost'])
        plt.subplot(222)
        ax2 = sb.boxplot(x='type', y='cost', data=self.spend)
        # g = sb.catplot(x="type", y="cost", hue="market", data=cost,height=6, kind="bar", palette="muted")
        # g.despine(left=True)
        # g.set_ylabels("Cost")
        # g.set_xlabels(("Cost Type"))

        plt.subplot(212)
        sb.boxplot(x='market', y='cost', data=self.spend)
        cost_max = int(np.round(max(self.spend['cost']), 0))

        ticks = [0, int(np.round(0.1 * cost_max, 0)), int(np.round(0.2 * cost_max, 0)),
                 int(np.round(0.3 * cost_max, 0)),
                 int(np.round(0.4 * cost_max, 0)),
                 int(np.round(0.5 * cost_max, 0)), int(np.round(0.6 * cost_max, 0)), int(np.round(0.7 * cost_max, 0)),
                 int(np.round(0.8 * cost_max, 0)), int(np.round(0.9 * cost_max, 0)), int(np.round(cost_max, 0))]
        plt.yticks(ticks, ticks)

        print("Max Cost ", int(np.round(max(self.spend['cost']), 0)))
        typeCount = self.spend['type'].value_counts()
        plt.tight_layout() # make sure all graphs are tighty
        plt.show()
      
    def plotBars(self):
        plt.figure()
        sb.countplot(x="type", data=self.spend)
        plt.figure(figsize=self.figsize)
        sb.countplot(x="market", data=self.spend)
        plt.show()

    def showDataset(self):
        self.datatable = QtWidgets.QTableWidget(parent=self)
        self.datatable.setColumnCount(len(self.spend.columns))
        self.datatable.setRowCount(len(self.spend.index))
        
        for i in range(len(self.spend.index)):
            for j in range(len(spend.columns)):
                self.datatable.setItem(i, j, QtGui.QTableWidgetItem(str(df.iget_value(i, j))))

if __name__ == '__main__':
    spend = Spending()
    spend.plotSubPlots()
    spend.plotBars()
    spend.showDataset()
