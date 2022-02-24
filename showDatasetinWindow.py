from PyQt5 import QtCore, QtGui, QtQml
import numpy as np
import pandas as pd
import os
import sys

# show a given dataset in a window
# using python windows programming

class DataFrameModel(QtCore.QAbstractTableModel):
    DtypeRole = QtCore.Qt.UserRole + 1000
    ValueRole = QtCore.Qt.UserRole + 1001

    def __init__(self, df=pd.DataFrame(), parent=None):
        super(DataFrameModel, self).__init__(parent)
        self._dataframe = df

    def setDataFrame(self, dataframe):
        self.beginResetModel()
        self._dataframe = dataframe.copy()
        self.endResetModel()

    def dataFrame(self):
        return self._dataframe
    
    dataFrame = QtCore.pyqtProperty(pd.DataFrame, fget=dataFrame, fset=setDataFrame)
    @QtCore.pyqtSlot(int, QtCore.Qt.Orientation, result=str)
 
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self._dataframe.columns[section]
            else:
                return str(self._dataframe.index[section])
        return QtCore.QVariant()

    def rowCount(self, parent=QtCore.QModelIndex()):
        if parent.isValid():
            return 0
        return len(self._dataframe.index)

    def columnCount(self, parent=QtCore.QModelIndex()):
        if parent.isValid():
            return 0
        return self._dataframe.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < self.rowCount() \
            and 0 <= index.column() < self.columnCount()):
            return QtCore.QVariant()
        row = self._dataframe.index[index.row()]
        col = self._dataframe.columns[index.column()]
        dt = self._dataframe[col].dtype
        val = self._dataframe.iloc[row][col]
  
        if role == QtCore.Qt.DisplayRole:
            return str(val)
        elif role == DataFrameModel.ValueRole:
            return val
        if role == DataFrameModel.DtypeRole:
            return dt
        return QtCore.QVariant()

    def roleNames(self):
        roles = {
            QtCore.Qt.DisplayRole: b'display',
            DataFrameModel.DtypeRole: b'dtype',
            DataFrameModel.ValueRole: b'value'
        }
        return roles

if __name__ == "__main__":
    app = QtGui.QGuiApplication(sys.argv)
    df = pd.DataFrame(np.random.randint(0, 100, size=(6, 7)), columns=list('ABCDEFG'))    
    model = DataFrameModel(df)
    engine = QtQml.QQmlApplicationEngine()
    engine.rootContext().setContextProperty("table_model", model)
    qml_path = os.path.join(os.path.dirname(__file__), "main.qml")
    engine.load(QtCore.QUrl.fromLocalFile(qml_path))
   
    if not engine.rootObjects():
        sys.exit(-1)
    engine.quit.connect(app.quit)
    sys.exit(app.exec_())
