from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from PySide2 import QtWebEngineWidgets



class Map(QWidget):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)

        self.map_view = QtWebEngineWidgets.QWebEngineView()
        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0,0,0,0)


        with open('./public/map.html', 'r') as f:
            self.map_view.setHtml(f.read())

        self._layout.addWidget(self.map_view)

        self.setLayout(self._layout)

if __name__ == '__main__':
    import sys
    app = QApplication([])
    win = Map()
    win.show()
    sys.exit(app.exec_())


