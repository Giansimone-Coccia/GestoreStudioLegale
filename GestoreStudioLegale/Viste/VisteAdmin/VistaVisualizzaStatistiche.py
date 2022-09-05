
'''from PyQt5.QtChart import QBarCategoryAxis, QBarSet, QChart, QBarSeries, QValueAxis, QChartView
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QMainWindow, QWidget, QGridLayout
import pyqtgraph as pg'''
#from _curses import window

from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout)
#from PyQt5.QtChart import QChart, QChartView, QHorizontalBarSeries, QBarSet, QBarCategoryAxis, QValueAxis, QBarSeries
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPainter
from numpy.distutils.fcompiler import pg

from GestoreStudioLegale.Gestione.Statistiche import Statistiche

class VistaVisualizzaStatistiche(QMainWindow):

    def __init__(self, parent=None):
        super(VistaVisualizzaStatistiche, self).__init__(parent)

        self.setWindowTitle("Statistiche")
        stats =Statistiche()

        self.resize(800, 600)

        set0 = QBarSet('X0')
        set1 = QBarSet('X1')
        set2 = QBarSet('X2')
        set3 = QBarSet('X3')
        set4 = QBarSet('X4')

        set0.append([1, 2, 3, 4, 5, 6])
        set1.append([5, 0, 0, 4, 0, 7])
        set2.append([3, 5, 8, 13, 8, 5])
        set3.append([5, 6, 7, 3, 4, 5])
        set4.append([9, 7, 5, 3, 1, 2])

        series = QHorizontalBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)
        series.append(set3)
        series.append(set4)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle('Horizontal Bar Chart Demo')

        chart.setAnimationOptions(QChart.SeriesAnimations)

        months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'June')

        axisY = QBarCategoryAxis()
        axisY.append(months)
        chart.addAxis(axisY, Qt.AlignLeft)
        series.attachAxis(axisY)

        axisX = QValueAxis()
        chart.addAxis(axisX, Qt.AlignBottom)
        series.attachAxis(axisX)

        axisX.applyNiceNumbers()

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)
        self.setCentralWidget(chartView)

        self.setGeometry(100, 100, 600, 500)

        widget = QWidget()

        stats=Statistiche()

        plot = pg.plot()

        bargraph = pg.BarGraphItem(height=stats.mostraGrafico(''), width=0.6, brush='g')

        self.set = QBarSet()
        self.set.append(stats.mostraStatistiche().values())
        self._bar_series = QBarSeries()
        self._bar_series.append(self.set)

        self.chart = QChart()

        self._axis_x = QBarCategoryAxis()
        self._axis_x.append(stats.mostraStatistiche().keys())
        self.chart.setAxisX(self._axis_x, self._bar_series)

        self._axis_y = QValueAxis()
        self.chart.setAxisY(self._axis_y, self._bar_series)
        self._axis_y.setRange(0, 20)

        self._chart_view = QChartView(self.chart)
        self._chart_view.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(self._chart_view)

        window.resize(440, 300)

        plot.addItem(bargraph)

        layout = QGridLayout()

        widget.setLayout(layout)

        layout.addWidget(plot, 0, 1, 3, 1)

        self.setCentralWidget(widget)