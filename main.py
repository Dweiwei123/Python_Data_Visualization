# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot

from uiWindow import Ui_MainWindow
from PyQt5 import QtWidgets
import os
import webbrowser as web


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # 当前文件夹目录
        dir = os.path.dirname(__file__)
        url = dir + '\聚类.svg'
        #print(url)
        web.open_new_tab(url)

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # 当前文件夹目录
        dir = os.path.dirname(__file__)
        url = dir + r'\聚类2.svg'
        web.open_new_tab(url)


    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        # 当前文件夹目录
        dir = os.path.dirname(__file__)
        url = dir + r'\平均评分地图.svg'
        web.open_new_tab(url)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
