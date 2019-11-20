import platform
from qgis.PyQt import QtCore as qcore
from qgis.PyQt import QtGui as qgui
from qgis.PyQt import QtWidgets

from qgis.PyQt.QtWidgets import QAbstractItemView, QSizePolicy, QLabel, QDialog

from EditorMetadadosSNIMar.snimarEditorController.models import TableModel
from EditorMetadadosSNIMar.snimarEditorController.models import customComboBoxModel as customCombo
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

        # Table setup
        wk_model = TableModel(self, [u"Nome", u"AphiaId"], [QtWidgets.QLineEdit, QtWidgets.QLineEdit], self.results_table)
        self.results_table.setModel(wk_model)
        self.results_table.resizeColumnsToContents()
        self.results_table.verticalHeader().setVisible(False)
        self.results_table.resizeRowsToContents()
        self.results_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.results_table.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.results_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # Close the dialog window
        self.btn_close_dialog.clicked.connect(lambda: self.done(0))

        # Setup search
        self.btn_search.clicked.connect(self.search_thesaurus)

    def search_thesaurus(self):
        """
        Send request to the WORMS API
        """
        name = self.name_edit.text()
        identifier = self.identifier_edit.text()
