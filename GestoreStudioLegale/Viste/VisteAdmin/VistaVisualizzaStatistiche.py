'''from PyQt5.QtChart import QBarCategoryAxis, QBarSet, QChart, QBarSeries, QValueAxis, QChartView
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QMainWindow, QWidget, QGridLayout
import pyqtgraph as pg'''
#from _curses import window
'''from _curses import window
from PyQt5.QtChart import QBarSet, QHorizontalBarSeries, QChart, QBarCategoryAxis, QValueAxis, QChartView, QBarSeries, QStackedBarSeries
from PyQt5.Qt import Qt
from PyQt5.QtChart import QBarSet, QHorizontalBarSeries, QChart, QBarCategoryAxis, QValueAxis, QChartView
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout
from numpy.distutils.fcompiler import pg
from GestoreStudioLegale.Utilities.Utilities import Tools

from GestoreStudioLegale.Gestione.Statistiche import Statistiche

class VistaVisualizzaStatistiche(QMainWindow):

    def __init__(self, parent=None):
        super(VistaVisualizzaStatistiche, self).__init__(parent)
        self.setWindowTitle("Statistiche")
        stats = Statistiche()
        stat= stats.mostraStatistiche()
        self.resize(1000, 800)
        set0 = QBarSet('Medie Mensili')

        set0.append([stat["Amminstrative"], stat["Civili"], stat["Minorili"], stat["Penali"], stat["Mensili"], stat["Appuntamenti"]])

        series = QStackedBarSeries()
        series.append(set0)
        series.setLabelsVisible(True)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle('STATISTICHE')

        chart.setAnimationOptions(QChart.SeriesAnimations)

        types = ('udienze amministrative', 'udienze civili', 'udienze minorili', 'udienze penali', 'udienze mensili', 'numero appuntamenti')

        axisX = QBarCategoryAxis()
        axisX.append(types)
        chart.addAxis(axisX, Qt.AlignBottom)
        series.attachAxis(axisX)

        axisY = QValueAxis()
        chart.addAxis(axisY, Qt.AlignLeft)
        series.attachAxis(axisY)

        axisY.applyNiceNumbers()

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)
        self.setCentralWidget(chartView)'''
