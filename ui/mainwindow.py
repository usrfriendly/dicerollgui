# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from .Ui_mainwindow import Ui_MainWindow

from ui.diceroll import  Roll, PRoll


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_rollButton_released(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        
        self.d4Roll.setText(str(Roll.DoRolls(self.d4SpinBox.value(), 4)))
        self.d6Roll.setText(str(Roll.DoRolls(self.d6SpinBox.value(), 6)))
        self.d8Roll.setText(str(Roll.DoRolls(self.d8SpinBox.value(), 8)))
        self.d10Roll.setText(str(Roll.DoRolls(self.d10SpinBox.value(), 10)))
        self.d10PRoll.setText(str(PRoll.DoPRoll(1,9))+str(PRoll.DoPRoll(1, 9))+"%")
        self.d12Roll.setText(str(Roll.DoRolls(self.d12SpinBox.value(), 12)))
        self.d20Roll.setText(str(Roll.DoRolls(self.d20SpinBox.value(), 20)))
