# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditorMetadadosMarswInforbiomares/snimarQtInterfaceView/templates/dialogs//urlGeonetwork.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_url_geonetwork(object):
    def setupUi(self, url_geonetwork):
        url_geonetwork.setObjectName("url_geonetwork")
        url_geonetwork.setEnabled(True)
        url_geonetwork.resize(706, 295)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(url_geonetwork.sizePolicy().hasHeightForWidth())
        url_geonetwork.setSizePolicy(sizePolicy)
        url_geonetwork.setMinimumSize(QtCore.QSize(0, 0))
        url_geonetwork.setMaximumSize(QtCore.QSize(16777215, 295))
        url_geonetwork.setModal(False)
        self.gridLayout_9 = QtWidgets.QGridLayout(url_geonetwork)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.pushButton = QtWidgets.QPushButton(url_geonetwork)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_9.addWidget(self.pushButton, 8, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(url_geonetwork)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_9.addWidget(self.pushButton_2, 7, 0, 1, 1)
        self.label = QtWidgets.QLabel(url_geonetwork)
        self.label.setObjectName("label")
        self.gridLayout_9.addWidget(self.label, 0, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(url_geonetwork)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_9.addWidget(self.textEdit, 1, 0, 1, 1)

        self.retranslateUi(url_geonetwork)
        QtCore.QMetaObject.connectSlotsByName(url_geonetwork)

    def retranslateUi(self, url_geonetwork):
        _translate = QtCore.QCoreApplication.translate
        url_geonetwork.setWindowTitle(_translate("url_geonetwork", "Lista de Contactos"))
        self.pushButton.setText(_translate("url_geonetwork", "Limpar"))
        self.pushButton_2.setText(_translate("url_geonetwork", "Gravar"))
        self.label.setText(_translate("url_geonetwork", "Url Geonetwork:"))