# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from collections import OrderedDict
import rospy
from kinematic_pkg.msg import WEP_msg

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 750)
        MainWindow.setMinimumSize(QtCore.QSize(800, 750))
        MainWindow.setMaximumSize(QtCore.QSize(800, 750))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 791, 631))
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.comTab = QtWidgets.QWidget()
        self.comTab.setEnabled(True)
        self.comTab.setAccessibleName("")
        self.comTab.setObjectName("comTab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.comTab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 100, 771, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.comXlabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.comXlabel.setObjectName("comXlabel")
        self.horizontalLayout_7.addWidget(self.comXlabel)
        self.comXSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.comXSpin.setDecimals(3)
        self.comXSpin.setMinimum(-1000.0)
        self.comXSpin.setMaximum(1000.0)
        self.comXSpin.setObjectName("comXSpin")
        self.horizontalLayout_7.addWidget(self.comXSpin)
        self.verticalLayout_11.addLayout(self.horizontalLayout_7)
        self.verticalLayout.addLayout(self.verticalLayout_11)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.comYlabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.comYlabel.setObjectName("comYlabel")
        self.horizontalLayout_6.addWidget(self.comYlabel)
        self.comYSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.comYSpin.setDecimals(3)
        self.comYSpin.setMinimum(-1000.0)
        self.comYSpin.setMaximum(1000.0)
        self.comYSpin.setObjectName("comYSpin")
        self.horizontalLayout_6.addWidget(self.comYSpin)
        self.verticalLayout_10.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.verticalLayout_10)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.comZlabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.comZlabel.setObjectName("comZlabel")
        self.horizontalLayout_5.addWidget(self.comZlabel)
        self.comZSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.comZSpin.setDecimals(3)
        self.comZSpin.setMinimum(-1000.0)
        self.comZSpin.setMaximum(1000.0)
        self.comZSpin.setObjectName("comZSpin")
        self.horizontalLayout_5.addWidget(self.comZSpin)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.verticalLayout_9)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comRolllabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.comRolllabel.setObjectName("comRolllabel")
        self.horizontalLayout_3.addWidget(self.comRolllabel)
        self.comRollSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.comRollSpin.setDecimals(3)
        self.comRollSpin.setMinimum(-1000.0)
        self.comRollSpin.setMaximum(1000.0)
        self.comRollSpin.setObjectName("comRollSpin")
        self.horizontalLayout_3.addWidget(self.comRollSpin)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comPitchlabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.comPitchlabel.setObjectName("comPitchlabel")
        self.horizontalLayout_2.addWidget(self.comPitchlabel)
        self.comPitchSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.comPitchSpin.setDecimals(3)
        self.comPitchSpin.setMinimum(-1000.0)
        self.comPitchSpin.setMaximum(1000.0)
        self.comPitchSpin.setObjectName("comPitchSpin")
        self.horizontalLayout_2.addWidget(self.comPitchSpin)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comYawlabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.comYawlabel.setObjectName("comYawlabel")
        self.horizontalLayout.addWidget(self.comYawlabel)
        self.comYawSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.comYawSpin.setDecimals(3)
        self.comYawSpin.setMinimum(-1000.0)
        self.comYawSpin.setMaximum(1000.0)
        self.comYawSpin.setObjectName("comYawSpin")
        self.horizontalLayout.addWidget(self.comYawSpin)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.comLabel = QtWidgets.QLabel(self.comTab)
        self.comLabel.setGeometry(QtCore.QRect(260, 20, 231, 61))
        self.comLabel.setStyleSheet("font: 63 36pt \"Ubuntu\";")
        self.comLabel.setObjectName("comLabel")
        self.tabWidget.addTab(self.comTab, "")
        self.jointTab = QtWidgets.QWidget()
        self.jointTab.setObjectName("jointTab")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.jointTab)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(10, 90, 781, 491))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.lHipYawLabel = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.lHipYawLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lHipYawLabel.setObjectName("lHipYawLabel")
        self.horizontalLayout_14.addWidget(self.lHipYawLabel)
        self.lHipYawSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_6)
        self.lHipYawSpin.setDecimals(3)
        self.lHipYawSpin.setMinimum(-1000.0)
        self.lHipYawSpin.setMaximum(1000.0)
        self.lHipYawSpin.setObjectName("lHipYawSpin")
        self.horizontalLayout_14.addWidget(self.lHipYawSpin)
        self.rHipYawLabel = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.rHipYawLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rHipYawLabel.setObjectName("rHipYawLabel")
        self.horizontalLayout_14.addWidget(self.rHipYawLabel)
        self.rHipYawSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_6)
        self.rHipYawSpin.setDecimals(3)
        self.rHipYawSpin.setMinimum(-1000.0)
        self.rHipYawSpin.setMaximum(1000.0)
        self.rHipYawSpin.setObjectName("rHipYawSpin")
        self.horizontalLayout_14.addWidget(self.rHipYawSpin)
        self.verticalLayout_21.addLayout(self.horizontalLayout_14)
        self.verticalLayout_6.addLayout(self.verticalLayout_21)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.lHipRollLabel = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.lHipRollLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lHipRollLabel.setObjectName("lHipRollLabel")
        self.horizontalLayout_13.addWidget(self.lHipRollLabel)
        self.lHipRollSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_6)
        self.lHipRollSpin.setDecimals(3)
        self.lHipRollSpin.setMinimum(-1000.0)
        self.lHipRollSpin.setMaximum(1000.0)
        self.lHipRollSpin.setObjectName("lHipRollSpin")
        self.horizontalLayout_13.addWidget(self.lHipRollSpin)
        self.rHipRollLabel = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.rHipRollLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rHipRollLabel.setObjectName("rHipRollLabel")
        self.horizontalLayout_13.addWidget(self.rHipRollLabel)
        self.rHipRollSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_6)
        self.rHipRollSpin.setDecimals(3)
        self.rHipRollSpin.setMinimum(-1000.0)
        self.rHipRollSpin.setMaximum(1000.0)
        self.rHipRollSpin.setObjectName("rHipRollSpin")
        self.horizontalLayout_13.addWidget(self.rHipRollSpin)
        self.verticalLayout_20.addLayout(self.horizontalLayout_13)
        self.verticalLayout_6.addLayout(self.verticalLayout_20)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lHipPitchLabel = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.lHipPitchLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lHipPitchLabel.setObjectName("lHipPitchLabel")
        self.horizontalLayout_12.addWidget(self.lHipPitchLabel)
        self.lHipPitchSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_6)
        self.lHipPitchSpin.setDecimals(3)
        self.lHipPitchSpin.setMinimum(-1000.0)
        self.lHipPitchSpin.setMaximum(1000.0)
        self.lHipPitchSpin.setObjectName("lHipPitchSpin")
        self.horizontalLayout_12.addWidget(self.lHipPitchSpin)
        self.rHipPitchLabel = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.rHipPitchLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rHipPitchLabel.setObjectName("rHipPitchLabel")
        self.horizontalLayout_12.addWidget(self.rHipPitchLabel)
        self.rHipPitchSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_6)
        self.rHipPitchSpin.setDecimals(3)
        self.rHipPitchSpin.setMinimum(-1000.0)
        self.rHipPitchSpin.setMaximum(1000.0)
        self.rHipPitchSpin.setObjectName("rHipPitchSpin")
        self.horizontalLayout_12.addWidget(self.rHipPitchSpin)
        self.verticalLayout_19.addLayout(self.horizontalLayout_12)
        self.verticalLayout_6.addLayout(self.verticalLayout_19)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lKneeLabel = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.lKneeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lKneeLabel.setObjectName("lKneeLabel")
        self.horizontalLayout_11.addWidget(self.lKneeLabel)
        self.lKneeSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_6)
        self.lKneeSpin.setDecimals(3)
        self.lKneeSpin.setMinimum(-1000.0)
        self.lKneeSpin.setMaximum(1000.0)
        self.lKneeSpin.setObjectName("lKneeSpin")
        self.horizontalLayout_11.addWidget(self.lKneeSpin)
        self.rKneeLabel = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.rKneeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rKneeLabel.setObjectName("rKneeLabel")
        self.horizontalLayout_11.addWidget(self.rKneeLabel)
        self.rKneeSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_6)
        self.rKneeSpin.setDecimals(3)
        self.rKneeSpin.setMinimum(-1000.0)
        self.rKneeSpin.setMaximum(1000.0)
        self.rKneeSpin.setObjectName("rKneeSpin")
        self.horizontalLayout_11.addWidget(self.rKneeSpin)
        self.verticalLayout_18.addLayout(self.horizontalLayout_11)
        self.verticalLayout_6.addLayout(self.verticalLayout_18)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lFootPitchLabel = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.lFootPitchLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lFootPitchLabel.setObjectName("lFootPitchLabel")
        self.horizontalLayout_9.addWidget(self.lFootPitchLabel)
        self.lFootPitchSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_6)
        self.lFootPitchSpin.setDecimals(3)
        self.lFootPitchSpin.setMinimum(-1000.0)
        self.lFootPitchSpin.setMaximum(1000.0)
        self.lFootPitchSpin.setObjectName("lFootPitchSpin")
        self.horizontalLayout_9.addWidget(self.lFootPitchSpin)
        self.rFootPitchLabel = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.rFootPitchLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rFootPitchLabel.setObjectName("rFootPitchLabel")
        self.horizontalLayout_9.addWidget(self.rFootPitchLabel)
        self.rFootPitchSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_6)
        self.rFootPitchSpin.setDecimals(3)
        self.rFootPitchSpin.setMinimum(-1000.0)
        self.rFootPitchSpin.setMaximum(1000.0)
        self.rFootPitchSpin.setObjectName("rFootPitchSpin")
        self.horizontalLayout_9.addWidget(self.rFootPitchSpin)
        self.verticalLayout_16.addLayout(self.horizontalLayout_9)
        self.verticalLayout_6.addLayout(self.verticalLayout_16)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lFootRollLabel = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.lFootRollLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lFootRollLabel.setObjectName("lFootRollLabel")
        self.horizontalLayout_8.addWidget(self.lFootRollLabel)
        self.lFootRollSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_6)
        self.lFootRollSpin.setDecimals(3)
        self.lFootRollSpin.setMinimum(-1000.0)
        self.lFootRollSpin.setMaximum(1000.0)
        self.lFootRollSpin.setObjectName("lFootRollSpin")
        self.horizontalLayout_8.addWidget(self.lFootRollSpin)
        self.rFootRollLabel = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.rFootRollLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rFootRollLabel.setObjectName("rFootRollLabel")
        self.horizontalLayout_8.addWidget(self.rFootRollLabel)
        self.rFootRollSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_6)
        self.rFootRollSpin.setDecimals(3)
        self.rFootRollSpin.setMinimum(-1000.0)
        self.rFootRollSpin.setMaximum(1000.0)
        self.rFootRollSpin.setObjectName("rFootRollSpin")
        self.horizontalLayout_8.addWidget(self.rFootRollSpin)
        self.verticalLayout_17.addLayout(self.horizontalLayout_8)
        self.verticalLayout_6.addLayout(self.verticalLayout_17)
        self.label_13 = QtWidgets.QLabel(self.jointTab)
        self.label_13.setGeometry(QtCore.QRect(250, 20, 271, 51))
        self.label_13.setStyleSheet("font: 63 36pt \"Ubuntu\";")
        self.label_13.setObjectName("label_13")
        self.tabWidget.addTab(self.jointTab, "")
        self.inKinTab = QtWidgets.QWidget()
        self.inKinTab.setObjectName("inKinTab")
        self.verticalLayoutWidget_15 = QtWidgets.QWidget(self.inKinTab)
        self.verticalLayoutWidget_15.setGeometry(QtCore.QRect(10, 90, 781, 501))
        self.verticalLayoutWidget_15.setObjectName("verticalLayoutWidget_15")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_15)
        self.verticalLayout_22.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout()
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.lXLabel = QtWidgets.QLabel(self.verticalLayoutWidget_15)
        self.lXLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lXLabel.setObjectName("lXLabel")
        self.horizontalLayout_16.addWidget(self.lXLabel)
        self.lXSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_15)
        self.lXSpin.setDecimals(3)
        self.lXSpin.setMinimum(-1000.0)
        self.lXSpin.setMaximum(1000.0)
        self.lXSpin.setObjectName("lXSpin")
        self.horizontalLayout_16.addWidget(self.lXSpin)
        self.rXLabel = QtWidgets.QLabel(self.verticalLayoutWidget_15)
        self.rXLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rXLabel.setObjectName("rXLabel")
        self.horizontalLayout_16.addWidget(self.rXLabel)
        self.rXSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_15)
        self.rXSpin.setDecimals(3)
        self.rXSpin.setMinimum(-1000.0)
        self.rXSpin.setMaximum(1000.0)
        self.rXSpin.setObjectName("rXSpin")
        self.horizontalLayout_16.addWidget(self.rXSpin)
        self.verticalLayout_31.addLayout(self.horizontalLayout_16)
        self.verticalLayout_22.addLayout(self.verticalLayout_31)
        self.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.lYLabel = QtWidgets.QLabel(self.verticalLayoutWidget_15)
        self.lYLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lYLabel.setObjectName("lYLabel")
        self.horizontalLayout_17.addWidget(self.lYLabel)
        self.lYSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_15)
        self.lYSpin.setDecimals(3)
        self.lYSpin.setMinimum(-1000.0)
        self.lYSpin.setMaximum(1000.0)
        self.lYSpin.setObjectName("lYSpin")
        self.horizontalLayout_17.addWidget(self.lYSpin)
        self.rYLabel = QtWidgets.QLabel(self.verticalLayoutWidget_15)
        self.rYLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rYLabel.setObjectName("rYLabel")
        self.horizontalLayout_17.addWidget(self.rYLabel)
        self.rYSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_15)
        self.rYSpin.setDecimals(3)
        self.rYSpin.setMinimum(-1000.0)
        self.rYSpin.setMaximum(1000.0)
        self.rYSpin.setObjectName("rYSpin")
        self.horizontalLayout_17.addWidget(self.rYSpin)
        self.verticalLayout_30.addLayout(self.horizontalLayout_17)
        self.verticalLayout_22.addLayout(self.verticalLayout_30)
        self.verticalLayout_29 = QtWidgets.QVBoxLayout()
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.lZLabel = QtWidgets.QLabel(self.verticalLayoutWidget_15)
        self.lZLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lZLabel.setObjectName("lZLabel")
        self.horizontalLayout_18.addWidget(self.lZLabel)
        self.lZSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_15)
        self.lZSpin.setDecimals(3)
        self.lZSpin.setMinimum(-1000.0)
        self.lZSpin.setMaximum(1000.0)
        self.lZSpin.setObjectName("lZSpin")
        self.horizontalLayout_18.addWidget(self.lZSpin)
        self.rZLabel = QtWidgets.QLabel(self.verticalLayoutWidget_15)
        self.rZLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rZLabel.setObjectName("rZLabel")
        self.horizontalLayout_18.addWidget(self.rZLabel)
        self.rZSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_15)
        self.rZSpin.setDecimals(3)
        self.rZSpin.setMinimum(-1000.0)
        self.rZSpin.setMaximum(1000.0)
        self.rZSpin.setObjectName("rZSpin")
        self.horizontalLayout_18.addWidget(self.rZSpin)
        self.verticalLayout_29.addLayout(self.horizontalLayout_18)
        self.verticalLayout_22.addLayout(self.verticalLayout_29)
        self.verticalLayout_28 = QtWidgets.QVBoxLayout()
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.lRollLabel = QtWidgets.QLabel(self.verticalLayoutWidget_15)
        self.lRollLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lRollLabel.setObjectName("lRollLabel")
        self.horizontalLayout_19.addWidget(self.lRollLabel)
        self.lRollSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_15)
        self.lRollSpin.setDecimals(3)
        self.lRollSpin.setMinimum(-1000.0)
        self.lRollSpin.setMaximum(1000.0)
        self.lRollSpin.setObjectName("lRollSpin")
        self.horizontalLayout_19.addWidget(self.lRollSpin)
        self.rRollLabel = QtWidgets.QLabel(self.verticalLayoutWidget_15)
        self.rRollLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rRollLabel.setObjectName("rRollLabel")
        self.horizontalLayout_19.addWidget(self.rRollLabel)
        self.rRollSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_15)
        self.rRollSpin.setDecimals(3)
        self.rRollSpin.setMinimum(-1000.0)
        self.rRollSpin.setMaximum(1000.0)
        self.rRollSpin.setObjectName("rRollSpin")
        self.horizontalLayout_19.addWidget(self.rRollSpin)
        self.verticalLayout_28.addLayout(self.horizontalLayout_19)
        self.verticalLayout_22.addLayout(self.verticalLayout_28)
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_20.setSpacing(10)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.lPitchLabel = QtWidgets.QLabel(self.verticalLayoutWidget_15)
        self.lPitchLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lPitchLabel.setObjectName("lPitchLabel")
        self.horizontalLayout_20.addWidget(self.lPitchLabel)
        self.lPitchSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_15)
        self.lPitchSpin.setDecimals(3)
        self.lPitchSpin.setMinimum(-1000.0)
        self.lPitchSpin.setMaximum(1000.0)
        self.lPitchSpin.setObjectName("lPitchSpin")
        self.horizontalLayout_20.addWidget(self.lPitchSpin)
        self.rPitchLabel = QtWidgets.QLabel(self.verticalLayoutWidget_15)
        self.rPitchLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rPitchLabel.setObjectName("rPitchLabel")
        self.horizontalLayout_20.addWidget(self.rPitchLabel)
        self.rPitchSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_15)
        self.rPitchSpin.setDecimals(3)
        self.rPitchSpin.setMinimum(-1000.0)
        self.rPitchSpin.setMaximum(1000.0)
        self.rPitchSpin.setObjectName("rPitchSpin")
        self.horizontalLayout_20.addWidget(self.rPitchSpin)
        self.verticalLayout_27.addLayout(self.horizontalLayout_20)
        self.verticalLayout_22.addLayout(self.verticalLayout_27)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.lYawLabel = QtWidgets.QLabel(self.verticalLayoutWidget_15)
        self.lYawLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lYawLabel.setObjectName("lYawLabel")
        self.horizontalLayout_21.addWidget(self.lYawLabel)
        self.lYawSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_15)
        self.lYawSpin.setDecimals(3)
        self.lYawSpin.setMinimum(-1000.0)
        self.lYawSpin.setMaximum(1000.0)
        self.lYawSpin.setObjectName("lYawSpin")
        self.horizontalLayout_21.addWidget(self.lYawSpin)
        self.rYawLabel = QtWidgets.QLabel(self.verticalLayoutWidget_15)
        self.rYawLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rYawLabel.setObjectName("rYawLabel")
        self.horizontalLayout_21.addWidget(self.rYawLabel)
        self.rYawSpin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_15)
        self.rYawSpin.setDecimals(3)
        self.rYawSpin.setMinimum(-1000.0)
        self.rYawSpin.setMaximum(1000.0)
        self.rYawSpin.setObjectName("rYawSpin")
        self.horizontalLayout_21.addWidget(self.rYawSpin)
        self.verticalLayout_24.addLayout(self.horizontalLayout_21)
        self.verticalLayout_22.addLayout(self.verticalLayout_24)
        self.label_14 = QtWidgets.QLabel(self.inKinTab)
        self.label_14.setGeometry(QtCore.QRect(140, 30, 541, 41))
        self.label_14.setStyleSheet("font: 63 36pt \"Ubuntu\";")
        self.label_14.setObjectName("label_14")
        self.tabWidget.addTab(self.inKinTab, "")
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(210, 650, 131, 41))
        self.startBtn.setStyleSheet("font: 20pt \"TakaoPGothic\";\n""color : rgb(0, 170, 0);")
        self.startBtn.setObjectName("startBtn")
        self.stopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn.setGeometry(QtCore.QRect(440, 650, 111, 41))
        self.stopBtn.setStyleSheet("font: 20pt \"TakaoPGothic\";\n""color : rgb(202, 0, 0);")
        self.stopBtn.setObjectName("stopBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)

        #My Code Start

        self.setDefines() ## set defines aparam
        self.flag = False
        self.mainValues =[]
        try:
            self.pub_WEP = rospy.Publisher('update_WEP', WEP_msg, queue_size=10)
            self.msg = WEP_msg()
            rospy.init_node('offsetTuner', anonymous=True)
            self.flag = True
        except:
            print("Port not found")
            self.flag = False

        self.actionSave.triggered.connect(self.saveFile)
        self.actionOpen.triggered.connect(self.openFile)

        self.stopBtn.clicked.connect(self.stopRobot)
        self.startBtn.clicked.connect(self.startRobot)

        #My Code Finished

        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def saveFile(self):
        dlg = QFileDialog()
        fileName = QFileDialog.getSaveFileName(None, "Save Your Record","","")
        #if fileName:
        #    print(fileName)
        values = OrderedDict()

        values["P_COM_X_offset"] = str(self.comXSpin.value())
        values["P_COM_Y_offset"] = str(self.comYSpin.value())
        values["P_COM_Z_offset"] = str(self.comZSpin.value())
        values["P_COM_Roll_offset"] = str(self.comRollSpin.value())
        values["P_COM_Pitch_offset"] = str(self.comPitchSpin.value())
        values["P_COM_Yaw_offset"] = str(self.comYawSpin.value())

        values["P_Left_Leg_Hip_Yaw_Offset"] = str(self.lHipYawSpin.value())
        values["P_Left_Leg_Hip_Roll_Offset"] = str(self.lHipRollSpin.value())
        values["P_Left_Leg_Hip_Pitch_Offset"] = str(self.lHipPitchSpin.value())
        values["P_Left_Leg_Knee_Offset"] = str(self.lKneeSpin.value())
        values["P_Left_Leg_Foot_Pitch_Offset"] = str(self.lFootPitchSpin.value())
        values["P_Left_Leg_Foot_Roll_Offset"] = str(self.lFootRollSpin.value())

        values["P_Right_Leg_Hip_Yaw_Offset"] = str(self.rHipYawSpin.value())
        values["P_Right_Leg_Hip_Roll_Offset"] = str(self.rHipRollSpin.value())
        values["P_Right_Leg_Hip_Pitch_Offset"] = str(self.rHipPitchSpin.value())
        values["P_Right_Leg_Knee_Offset"] = str(self.rKneeSpin.value())
        values["P_Right_Leg_Foot_Pitch_Offset"] = str(self.rFootPitchSpin.value())
        values["P_Right_Leg_Foot_Roll_Offset"] = str(self.rFootRollSpin.value())

        values["P_Left_Leg_X_Offset"] = str(self.lXSpin.value())
        values["P_Left_Leg_Y_Offset"] = str(self.lYSpin.value())
        values["P_Left_Leg_Z_Offset"] = str(self.lZSpin.value())
        values["P_Left_Leg_Roll_Offset"] = str(self.lRollSpin.value())
        values["P_Left_Leg_Pitch_Offset"] = str(self.lPitchSpin.value())
        values["P_Left_Leg_Yaw_Offset"] = str(self.lYawSpin.value())

        values["P_Right_Leg_X_Offset"] = str(self.rXSpin.value())
        values["P_Right_Leg_Y_Offset"] = str(self.rYSpin.value())
        values["P_Right_Leg_Z_Offset"] = str(self.rZSpin.value())
        values["P_Right_Leg_Roll_Offset"] = str(self.rRollSpin.value())
        values["P_Right_Leg_Pitch_Offset"] = str(self.rPitchSpin.value())
        values["P_Right_Leg_Yaw_Offset"] = str(self.rYawSpin.value())

        myFile = open(fileName[0] + '.txt', 'w')
        cnt = 0
        for value in values:
            if(cnt == 6) :
                myFile.write('\n')
                cnt = 0
            myFile.write("WEP[" + value + "] = " + values[value] + ';' + '\n')
            cnt += 1
        myFile.close()

    def openFile(self):

        seq = []

        seq.append(self.comXSpin)
        seq.append(self.comYSpin)
        seq.append(self.comZSpin)
        seq.append(self.comRollSpin)
        seq.append(self.comPitchSpin)
        seq.append(self.comYawSpin)

        seq.append(self.lHipYawSpin)
        seq.append(self.lHipRollSpin)
        seq.append(self.lHipPitchSpin)
        seq.append(self.lKneeSpin)
        seq.append(self.lFootPitchSpin)
        seq.append(self.lFootRollSpin)

        seq.append(self.rHipYawSpin)
        seq.append(self.rHipRollSpin)
        seq.append(self.rHipPitchSpin)
        seq.append(self.rKneeSpin)
        seq.append(self.rFootPitchSpin)
        seq.append(self.rFootRollSpin)

        seq.append(self.lXSpin)
        seq.append(self.lYSpin)
        seq.append(self.lZSpin)
        seq.append(self.lRollSpin)
        seq.append(self.lPitchSpin)
        seq.append(self.lYawSpin)

        seq.append(self.rXSpin)
        seq.append(self.rYSpin)
        seq.append(self.rZSpin)
        seq.append(self.rRollSpin)
        seq.append(self.rPitchSpin)
        seq.append(self.rYawSpin)

        fileName = QFileDialog.getOpenFileName(None, "Open your Record","","Text Files (*.txt)")
        myFile = open(fileName[0], 'r')
        #lenght = len(myFile.readlines())
        cnt = 0
        for line in myFile:
            #line.replace('\n', '')
            if(line != '\n') :
                line = line.split(' = ')
                line[1] = (line[1].split(';'))[0]
                #print(line)
                seq[cnt].setValue(float(line[1]))
                cnt += 1
        myFile.close()

    def generateFormule(self, value):
            # return int((value * 100) + 100)
            return value

    def stopRobot(self):
        #Not used.
        if(self.flag):
            pass
        else:
            print("Not Connected to Robot")

    def startRobot(self):
        if(self.flag):
            self.msg = self.generateStart()
            self.pub_WEP.publish(self.msg)
        else:

            print ("Not connected to Robot")

    def generateStart(self):
        self.msg.WEP = [0 for i in range(self.WEP_NUM)]
        self.msg.index =  [0 for i in range(self.WEP_NUM)]
        values = []
        index = []

        # values.append(int(math.fabs(int(self.comXSpin.value()))))
        index.append(self.P_COM_X_offset)
        values.append(self.comXSpin.value())
        # if(int(self.comXSpin.value()) >= 0):
        #     values.append(0)
        # else:
        #     values.append(1)
        index.append(self.P_COM_Y_offset)
        values.append(self.comYSpin.value())

        index.append(self.P_COM_Z_offset)
        values.append(self.comZSpin.value())

        index.append(self.P_COM_Roll_offset)
        values.append(self.generateFormule(self.comRollSpin.value()))
        index.append(self.P_COM_Pitch_offset)
        values.append(self.generateFormule(self.comPitchSpin.value()))
        index.append(self.P_COM_Yaw_offset)
        values.append(self.generateFormule(self.comYawSpin.value()))
        
        index.append(self.P_Left_Leg_Hip_Yaw_Offset)
        values.append(self.generateFormule(self.lHipYawSpin.value()))
        index.append(self.P_Left_Leg_Hip_Roll_Offset)
        values.append(self.generateFormule(self.lHipRollSpin.value()))
        index.append(self.P_Left_Leg_Hip_Pitch_Offset)
        values.append(self.generateFormule(self.lHipPitchSpin.value()))
        index.append(self.P_Left_Leg_Knee_Offset)
        values.append(self.generateFormule(self.lKneeSpin.value()))
        index.append(self.P_Left_Leg_Foot_Pitch_Offset)
        values.append(self.generateFormule(self.lFootPitchSpin.value()))
        index.append(self.P_Left_Leg_Foot_Roll_Offset)
        values.append(self.generateFormule(self.lFootRollSpin.value()))


        index.append(self.P_Right_Leg_Hip_Yaw_Offset)
        values.append(self.generateFormule(self.rHipYawSpin.value()))
        index.append(self.P_Right_Leg_Hip_Roll_Offset)
        values.append(self.generateFormule(self.rHipRollSpin.value()))
        index.append(self.P_Right_Leg_Hip_Pitch_Offset)
        values.append(self.generateFormule(self.rHipPitchSpin.value()))
        index.append(self.P_Right_Leg_Knee_Offset)
        values.append(self.generateFormule(self.rKneeSpin.value()))
        index.append(self.P_Right_Leg_Foot_Pitch_Offset)
        values.append(self.generateFormule(self.rFootPitchSpin.value()))
        index.append(self.P_Right_Leg_Foot_Roll_Offset)
        values.append(self.generateFormule(self.rFootRollSpin.value()))

        index.append(self.P_Left_Leg_X_Offset)
        values.append(self.lXSpin.value())

        index.append(self.P_Left_Leg_Y_Offset)
        values.append(self.lYSpin.value())

        index.append(self.P_Left_Leg_Z_Offset)
        values.append(self.lZSpin.value())
        
        index.append(self.P_Left_Leg_Roll_Offset)
        values.append(self.generateFormule(self.lRollSpin.value()))
        index.append(self.P_Left_Leg_Pitch_Offset)
        values.append(self.generateFormule(self.lPitchSpin.value()))
        index.append(self.P_Left_Leg_Yaw_Offset)
        values.append(self.generateFormule(self.lYawSpin.value()))

        index.append(self.P_Right_Leg_X_Offset)
        values.append(self.rXSpin.value())

        index.append(self.P_Right_Leg_Y_Offset)
        values.append(self.rYSpin.value())

        index.append(self.P_Right_Leg_Z_Offset)
        values.append(self.rZSpin.value())

        index.append(self.P_Right_Leg_Roll_Offset)
        values.append(self.generateFormule(self.rRollSpin.value()))
        index.append(self.P_Right_Leg_Pitch_Offset)
        values.append(self.generateFormule(self.rPitchSpin.value()))
        index.append(self.P_Right_Leg_Yaw_Offset)
        values.append(self.generateFormule(self.rYawSpin.value()))

        sizeOfArr = len(values)
        self.msg.sizeOfArr = sizeOfArr
        self.msg.WEP[0 : sizeOfArr] = values
        self.msg.index[0 : sizeOfArr] = index
        print(values)
        return self.msg

    def generateStop(self):
        values = []
        values.append(254)
        values.append(0)
        values.append(0)
        values.append(0)
        values.append(112)
        values.append(int(self.comXSpin.value()))
        values.append(int(self.comYSpin.value()))
        values.append(int(self.comZSpin.value()))
        values.append(self.generateFormule(self.comRollSpin.value()))
        values.append(self.generateFormule(self.comPitchSpin.value()))
        values.append(self.generateFormule(self.comYawSpin.value()))

        values.append(self.generateFormule(self.lHipYawSpin.value()))
        values.append(self.generateFormule(self.lHipRollSpin.value()))
        values.append(self.generateFormule(self.lHipPitchSpin.value()))
        values.append(self.generateFormule(self.lKneeSpin.value()))
        values.append(self.generateFormule(self.lFootPitchSpin.value()))
        values.append(self.generateFormule(self.lFootRollSpin.value()))

        values.append(self.generateFormule(self.rHipYawSpin.value()))
        values.append(self.generateFormule(self.rHipRollSpin.value()))
        values.append(self.generateFormule(self.rHipPitchSpin.value()))
        values.append(self.generateFormule(self.rKneeSpin.value()))
        values.append(self.generateFormule(self.rFootPitchSpin.value()))
        values.append(self.generateFormule(self.rFootRollSpin.value()))

        values.append(int(self.lXSpin.value()))
        values.append(int(self.lYSpin.value()))
        values.append(int(self.lZSpin.value()))
        values.append(self.generateFormule(self.lRollSpin.value()))
        values.append(self.generateFormule(self.lPitchSpin.value()))
        values.append(self.generateFormule(self.lYawSpin.value()))

        values.append(int(self.rXSpin.value()))
        values.append(int(self.rYSpin.value()))
        values.append(int(self.rZSpin.value()))
        values.append(self.generateFormule(self.rRollSpin.value()))
        values.append(self.generateFormule(self.rPitchSpin.value()))
        values.append(self.generateFormule(self.rYawSpin.value()))

        return values


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AUTMan OffsetTuner"))
        self.comXlabel.setText(_translate("MainWindow", "COM X offset"))
        self.comYlabel.setText(_translate("MainWindow", "COM Y offset"))
        self.comZlabel.setText(_translate("MainWindow", "COM Z offset"))
        self.comRolllabel.setText(_translate("MainWindow", "COM Roll offset"))
        self.comPitchlabel.setText(_translate("MainWindow", "COM Pitch offset"))
        self.comYawlabel.setText(_translate("MainWindow", "COM Yaw offset"))
        self.comLabel.setText(_translate("MainWindow", "Body COM"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.comTab), _translate("MainWindow", "COM"))
        self.lHipYawLabel.setText(_translate("MainWindow", "Left Leg Hip Yaw Offset"))
        self.rHipYawLabel.setText(_translate("MainWindow", "Right Leg Hip Yaw Offset"))
        self.lHipRollLabel.setText(_translate("MainWindow", "Left Leg Hip Roll Offset"))
        self.rHipRollLabel.setText(_translate("MainWindow", "Right Leg Hip Roll Offset"))
        self.lHipPitchLabel.setText(_translate("MainWindow", "Left Leg Hip Pitch Offset"))
        self.rHipPitchLabel.setText(_translate("MainWindow", "Right Leg Hip Pitch Offset"))
        self.lKneeLabel.setText(_translate("MainWindow", "Left Leg Knee Offset"))
        self.rKneeLabel.setText(_translate("MainWindow", "Right Leg Knee Offset"))
        self.lFootPitchLabel.setText(_translate("MainWindow", "Left Leg Foot Pitch Offset"))
        self.rFootPitchLabel.setText(_translate("MainWindow", "Right Leg Foot Pitch Offset"))
        self.lFootRollLabel.setText(_translate("MainWindow", "Left Leg Foot Roll Offset"))
        self.rFootRollLabel.setText(_translate("MainWindow", "Right Leg Foot Roll Offset"))
        self.label_13.setText(_translate("MainWindow", "Joint Offset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.jointTab), _translate("MainWindow", "JOINT"))
        self.lXLabel.setText(_translate("MainWindow", "Left Leg X Offset"))
        self.rXLabel.setText(_translate("MainWindow", "Right Leg X Offset"))
        self.lYLabel.setText(_translate("MainWindow", "Left Leg Y Offset"))
        self.rYLabel.setText(_translate("MainWindow", "Right Leg Y Offset"))
        self.lZLabel.setText(_translate("MainWindow", "Left Leg Z Offset"))
        self.rZLabel.setText(_translate("MainWindow", "Right Leg Z Offset"))
        self.lRollLabel.setText(_translate("MainWindow", "Left Leg Roll Offset"))
        self.rRollLabel.setText(_translate("MainWindow", "Right Leg Roll Offset"))
        self.lPitchLabel.setText(_translate("MainWindow", "Left Leg Pitch Offset"))
        self.rPitchLabel.setText(_translate("MainWindow", "Right Leg Pitch Offset"))
        self.lYawLabel.setText(_translate("MainWindow", "Left Leg Yaw Offset"))
        self.rYawLabel.setText(_translate("MainWindow", "Right Leg Yaw Offset"))
        self.label_14.setText(_translate("MainWindow", "Inverse Kinematic Offset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.inKinTab), _translate("MainWindow", "Inverse Kinematic"))
        self.startBtn.setText(_translate("MainWindow", "START"))
        self.stopBtn.setText(_translate("MainWindow", "STOP"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))


    def setDefines(self):
        ##Walk Engine Parameters
        self.P_Motion_Resolution =  1  ##motion resoulotion (min=0.001  max=0.1)  
        self.P_Gait_Frequency =  2  ##gait frequency (min=0.001  max=1.0) 
        self.P_Double_Support_Sleep =  3  ##double support sleep (min=0.001  max=1.0)  
        self.P_Single_Support_Sleep =  4  ##single support sleep (min=0.001  max=1.0)  
        self.P_Fly_Roll_Gain =   5  ##fly leg roll gain  
        self.P_Fly_Pitch_Gain =  6  ##fly leg pitch gain 
        self.P_Fly_Yaw_Gain = 7  ##fly leg yaw gain
        self.P_Fly_X_Swing_Gain =   8
        self.P_Fly_Y_Swing_Gain =   9
        self.P_Fly_Z_Swing_Gain =   10  ##fly leg step height gain (min=0.001  max=1.0)  
        self.P_Support_Roll_Gain =  11  ##support leg roll gain  
        self.P_Support_Pitch_Gain = 12  ##support leg pitch gain
        self.P_Support_Yaw_Gain =   13  ##support leg yaw gain  
        self.P_Support_X_Swing_Gain =  14  
        self.P_Support_Y_Swing_Gain =  15  ##support leg Y gain (sideward) 
        self.P_Support_Z_Swing_Gain =  16  ##support leg Z gain (topdown) this parameter also can use for push  
        self.P_Body_X_Swing_Gain =  17
        self.P_Body_Y_Swing_Gain =  18  ##body sideward swing gain (for swing both of legs in y axis during walk)  
        self.P_Body_Z_Swing_Gain =  19  ##body topdown swing gain (for swing both of legs in Z axis during walk)

        ##stablization parameters
        self.P_Stablizer_Arm_Pitch_Gain = 20 ##add
        self.P_Stablizer_Arm_Roll_Gain =  21 ##add
        self.P_Stablizer_Arm_Elbow_Gain = 22
        self.P_Stablizer_Hip_Roll_Gain =  23 ##add
        self.P_Stablizer_Hip_Pitch_Gain = 24 ##add
        self.P_Stablizer_Knee_Gain =   25 ##add
        self.P_Stablizer_Foot_Pitch_Gain =   26 ##add
        self.P_Stablizer_Foot_Roll_Gain = 27 ##add
        self.P_Stablizer_COM_X_Shift_Gain =  28 ##add
        self.P_Stablizer_COM_Y_Shift_Gain =  29 ##add

        self.P_Gyro_Stablizer_Arm_Pitch_Gain =  30 ##add
        self.P_Gyro_Stablizer_Arm_Roll_Gain =   31
        self.P_Gyro_Stablizer_Arm_Elbow_Gain =  32
        self.P_Gyro_Stablizer_Hip_Roll_Gain =   33 ##add
        self.P_Gyro_Stablizer_Hip_Pitch_Gain =  34 ##add
        self.P_Gyro_Stablizer_Knee_Gain = 35 ##add
        self.P_Gyro_Stablizer_Foot_Pitch_Gain = 36 ##add
        self.P_Gyro_Stablizer_Foot_Roll_Gain =  37 ##add
        self.P_Gyro_Stablizer_COM_X_Shift_Gain=  38 ##add
        self.P_Gyro_Stablizer_COM_Y_Shift_Gain=  39 ##add

        ##hopping gait gain
        self.P_Stablizer_Hopping_Gait_X_Gain =  40
        self.P_Stablizer_Hopping_Gait_Y_Gain =  41

        ##both leg offset in inverse kinematic (body COM)
        self.P_COM_X_offset = 42 ##add
        self.P_COM_Y_offset = 43 ##add
        self.P_COM_Z_offset = 44 ##add
        self.P_COM_Roll_offset = 45 ##add
        self.P_COM_Pitch_offset =   46 ##add
        self.P_COM_Yaw_offset =  47 ##add
        
        ##legs joints offset 
        self.P_Left_Leg_Hip_Yaw_Offset =  48 ##add
        self.P_Left_Leg_Hip_Roll_Offset = 49 ##add
        self.P_Left_Leg_Hip_Pitch_Offset =   50 ##add
        self.P_Left_Leg_Knee_Offset =  51 ##add
        self.P_Left_Leg_Foot_Pitch_Offset =  52 ##add
        self.P_Left_Leg_Foot_Roll_Offset =   53 ##add

        self.P_Right_Leg_Hip_Yaw_Offset = 54 ##add
        self.P_Right_Leg_Hip_Roll_Offset =   55 ##add
        self.P_Right_Leg_Hip_Pitch_Offset =  56 ##add
        self.P_Right_Leg_Knee_Offset = 57 ##add
        self.P_Right_Leg_Foot_Pitch_Offset = 58 ##add
        self.P_Right_Leg_Foot_Roll_Offset =  59 ##add

        ##Left leg inverse kinematic offset 
        self.P_Left_Leg_X_Offset =  60 ##add
        self.P_Left_Leg_Y_Offset =  61 ##add
        self.P_Left_Leg_Z_Offset =  62 ##add
        self.P_Left_Leg_Roll_Offset =  63 ##add
        self.P_Left_Leg_Pitch_Offset = 64 ##add
        self.P_Left_Leg_Yaw_Offset =   65 ##add

        self.P_Right_Leg_X_Offset = 66 ##add
        self.P_Right_Leg_Y_Offset = 67 ##add
        self.P_Right_Leg_Z_Offset = 68 ##add
        self.P_Right_Leg_Roll_Offset = 69 ##add
        self.P_Right_Leg_Pitch_Offset =   70 ##add
        self.P_Right_Leg_Yaw_Offset =  71 ##add

        self.P_R_Arm_Pitch_offset = 72 ##add
        self.P_R_Arm_Roll_offset =  73 ##add
        self.P_R_Arm_Elbow_offset = 74 ##add

        self.P_L_Arm_Pitch_offset = 75 ##add
        self.P_L_Arm_Roll_offset =  76 ##add
        self.P_L_Arm_Elbow_offset = 77 ##add

        ##fall thershold
        self.P_Fall_Roll_Thershold =   78
        self.P_Fall_Pitch_Thershold =  79

        ##imu offset
        self.P_IMU_X_Angle_Offset = 80 ##add
        self.P_IMU_Y_Angle_Offset = 81 ##add

        ##MPU filtering parametrs 
        self.P_Gyro_X_LowPass_Gain =   82 ##add
        self.P_Gyro_Y_LowPass_Gain =   83 ##add

        ##kalman filter r mesurement value
        self.P_Kalman_Roll_RM_Rate =   84
        self.P_Kalman_Pitch_RM_Rate =  85
        self.P_Kalman_Yaw_RM_Rate = 86

        ##smoothing ratio
        self.P_Vx_Smoothing_Ratio = 87 
        self.P_Vy_Smoothing_Ratio = 88 
        self.P_Vt_Smoothing_Ratio = 89 

        self.P_Leg_Length =   90 ##add

        self.P_Head_Pan_Speed =  91
        self.P_Head_Tilt_Speed = 92

        self.P_Min_Voltage_Limit =  93

        self.Vx_Offset =   94
        self.Vy_Offset =   95
        self.Vt_Offset =   96

        self.P_Left_Leg_Hip_Pitch_Offset_Original = 97 ##add
        self.P_Right_Leg_Hip_Pitch_Offset_Original=  98 ##add
        self.P_Left_Leg_Hip_Pitch_Offset_Backwards=  99 ##add
        self.P_Right_Leg_Hip_Pitch_Offset_Backwards= 100 ##add

        self.WEP_NUM = 101

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

