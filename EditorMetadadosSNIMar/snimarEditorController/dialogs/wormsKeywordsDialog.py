import platform
from qgis.PyQt import QtCore as qcore
from qgis.PyQt import QtGui as qgui
from qgis.PyQt import QtWidgets

from qgis.PyQt.QtWidgets import QAbstractItemView, QSizePolicy, QLabel, QDialog

from EditorMetadadosSNIMar.snimarQtInterfaceView.pyuic4GeneratedSourceFiles.dialogs import wormsDialog


class WormsKeywordsDialog(QtWidgets.QDialog, wormsDialog.Ui_worms_dialog):
    def __init__(self, parent):
        super(WormsKeywordsDialog, self).__init__(parent)
        if platform.system() != "Linux":
            font = QFont()
            font.setFamily(u"Segoe UI Symbol")
            self.setFont(font)
        self.setupUi(self)
        self.setModal(True)
