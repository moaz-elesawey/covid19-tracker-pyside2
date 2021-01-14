from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from ui_main import Ui_MainWindow
from api import get_countries_data

from map_widget import Map
from graph_widget import Graph

import locale
locale.setlocale(locale.LC_NUMERIC, '')


_COUNTRIES_DATA = get_countries_data()
# print(_COUNTRIES_DATA[1])

class MainWindow(QMainWindow):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)

        self.setWindowIcon(QIcon('./icons/window_icon.png'))

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.__map = Map()
        self.__graph = Graph()

        #Row count 
        self.ui.countries_cases_table.setRowCount(len(_COUNTRIES_DATA))
        #Column count 
        self.ui.countries_cases_table.setColumnCount(2)
        self.ui.countries_cases_table.setHorizontalHeaderLabels(['Country', 'Total Cases'])

        #Table will fit the screen horizontally 
        self.ui.countries_cases_table.horizontalHeader().setStretchLastSection(True)
        self.ui.countries_cases_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        self.ui.countries_select.currentIndexChanged.connect(self.on_select_country)
        self.ui.header_title.clicked.connect(self.refresh_data)

        self.init_components()

        self._populate_table()

        # creating the schedualer
        self .__timer = QTimer()
        self.__timer.timeout.connect(self.refresh_data)
        self.__timer.start(1000*60*1)

        self.show()

    def init_components(self):

        self.ui.covid_cases_inc.setText("+"+self.format_number(_COUNTRIES_DATA[0]['today_cases']))
        self.ui.recovered_cases_inc.setText("+"+self.format_number(_COUNTRIES_DATA[0]['today_recovered']))
        self.ui.death_cases_inc.setText("+"+self.format_number(_COUNTRIES_DATA[0]['today_deaths']))

        self.ui.covid_cases_tot.setText("+"+self.format_number(_COUNTRIES_DATA[0]['cases'])+' Total')
        self.ui.recovered_cases_tot.setText("+"+self.format_number(_COUNTRIES_DATA[0]['recovered'])+' Total')
        self.ui.death_cases_tot.setText("+"+self.format_number(_COUNTRIES_DATA[0]['deaths'])+' Total')

        ## adding the map to the it place
        self.ui.verticalLayout_5.removeWidget(self.__map)
        self.ui.verticalLayout_8.removeWidget(self.__graph)

        self.ui.verticalLayout_5.addWidget(self.__map)
        self.ui.verticalLayout_8.addWidget(self.__graph)


    def _populate_table(self):
        self.ui.countries_select.clear()

        for i in range(len(_COUNTRIES_DATA)):
            self.ui.countries_select.addItem(_COUNTRIES_DATA[i]['country_name'])
            for j in range(2):
                self.ui.countries_cases_table.setItem(i, 0, QTableWidgetItem(_COUNTRIES_DATA[i]['country_name']))
                self.ui.countries_cases_table.setItem(i, 1, QTableWidgetItem(self.format_number(_COUNTRIES_DATA[i]['cases'])))


    # events
    def on_select_country(self, e):
        self.ui.covid_cases_inc.setText("+"+self.format_number(_COUNTRIES_DATA[e]['today_cases']))
        self.ui.recovered_cases_inc.setText("+"+self.format_number(_COUNTRIES_DATA[e]['today_recovered']))
        self.ui.death_cases_inc.setText("+"+self.format_number(_COUNTRIES_DATA[e]['today_deaths']))

        self.ui.covid_cases_tot.setText("+"+self.format_number(_COUNTRIES_DATA[e]['cases'])+' Total')
        self.ui.recovered_cases_tot.setText("+"+self.format_number(_COUNTRIES_DATA[e]['recovered'])+' Total')
        self.ui.death_cases_tot.setText("+"+self.format_number(_COUNTRIES_DATA[e]['deaths'])+' Total')

    def refresh_data(self):
        global _COUNTRIES_DATA
        _current_index = self.ui.countries_select.currentIndex()
        _COUNTRIES_DATA = get_countries_data()

        self.init_components()
        self._populate_table()

        self.ui.countries_select.setCurrentIndex(_current_index)
        print('refresh_data')

    @staticmethod
    def format_number(number):
        _num = locale.format_string('%d', number, grouping=True)

        return _num


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())

