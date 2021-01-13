from PySide2 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import requests
import time
import datetime
import json

pg.setConfigOption('foreground', 'k')

class Graph(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super(Graph, self).__init__(*args, **kwargs)

        self._days, (self._cases, self._recovered, self._deaths) = self.create_data()

        self.graphWidget = pg.PlotWidget()

        self.date_axis = pg.DateAxisItem()
        self.date_axis.setGrid(True)
        self.cases_axis = pg.AxisItem(orientation='left')

        self._layout = QtWidgets.QVBoxLayout()
        self._layout.setContentsMargins(5,5,5,5)

        self._layout.addWidget(self.graphWidget)

        #Add Background colour to white
        self.graphWidget.setBackground('#f7f7f7')
        self.graphWidget.showGrid(x=True, y=False)
        #Set Range
        self.graphWidget.setYRange(min(self._cases)-6000, max(self._cases)+6000, padding=0)
        #self.graphWidget.setYXRange(20, 55, padding=0)

        pen = pg.mkPen(color=(255, 0, 0), width=4)
        self.graphWidget.setAxisItems({'bottom': self.date_axis, 'left': self.cases_axis})
        self.graphWidget.plot(self._days, self._cases, fillLevel=min(self._cases)-1000000, brush=(200,50,50,100),  pen=pen)
        self.setLayout(self._layout)

        self.setStyleSheet(u'border:none')


    @staticmethod
    def create_data():
        _x_days = []

        _y_cases = []
        _y_recovered = []
        _y_deaths = []


        i = 0
        try:
            _res = requests.get('https://disease.sh/v3/covid-19/historical/all?lastdays=60')

            _cases = _res.json()['cases']
            _recovered = _res.json()['recovered']
            _deaths = _res.json()['deaths']

            for (c_k, c_v), (r_k, r_v), (d_k, d_v) in zip(_cases.items(), _recovered.items(), _deaths.items()):
                _x_days.append(time.mktime(datetime.datetime.strptime(c_k, "%m/%d/%y").timetuple()))

                _y_cases.append(int(c_v))
                _y_recovered.append(int(r_v))
                _y_deaths.append(int(d_v))

                i += 1

            with open('./local/_historical_data.json', 'w') as f:
                f.write(json.dumps([_x_days, (_y_cases, _y_recovered, _y_deaths)]))

            return [_x_days, (_y_cases, _y_recovered, _y_deaths)]

        except:
            with open('./local/_historical_data.json') as f:
                return json.loads(f.read())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Graph()
    main.show()
    sys.exit(app.exec_())

