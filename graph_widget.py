from PySide2 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os

pg.setConfigOption('foreground', 'k')

class Graph(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super(Graph, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self._layout = QtWidgets.QVBoxLayout()
        self._layout.setContentsMargins(5,5,5,5)

        self._layout.addWidget(self.graphWidget)

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]

        #Add Background colour to white
        self.graphWidget.setBackground('#f7f7f7')
        # self.graphWidget.setForground('b')
        # Add Axis Labels
        # styles = {"color": "#000", "font-size": "15px"}
        # self.graphWidget.setLabel("left", "Cases", **styles)
        # self.graphWidget.setLabel("bottom", "Days", **styles)
        #Add grid
        self.graphWidget.showGrid(x=False, y=False)
        #Set Range
        self.graphWidget.setXRange(0, 10, padding=0)
        self.graphWidget.setYRange(20, 55, padding=0)

        pen = pg.mkPen(color=(255, 0, 0), width=3)
        self.graphWidget.plot(hour, temperature, name="Sensor 1",  pen=pen, symbol='o', symbolSize=7, symbolBrush=('b'))

        self.setLayout(self._layout)

        self.setStyleSheet(u'border:none')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Graph()
    main.show()
    sys.exit(app.exec_())

