import platform
import json

from qgis.PyQt import QtCore as qcore
from qgis.PyQt import QtGui as qgui
from qgis.PyQt import QtWidgets
from qgis.PyQt import QtNetwork

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
        self.wk_model = TableModel(self, [u"Nome", u"AphiaId"], [QtWidgets.QLineEdit, QtWidgets.QLineEdit], self.results_table)
        self.results_table.setModel(self.wk_model)
        self.results_table.resizeColumnsToContents()
        self.results_table.verticalHeader().setVisible(False)
        self.results_table.resizeRowsToContents()
        self.results_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.results_table.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.results_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.results_table.selectionModel().selectionChanged.connect(self.handle_selection_change)

        # Close the dialog window
        self.btn_close_dialog.clicked.connect(lambda: self.done(0))

        # Setup search
        self.btn_search.clicked.connect(self.search_thesaurus)

        # Setup add row
        self.add_row_btn.clicked.connect(self.add_keyword)

    def search_thesaurus(self):
        """
        Send request to the WORMS API
        """
        network_manager = QtNetwork.QNetworkAccessManager(self)

        name = self.name_edit.text()
        request_name_url = 'http://www.marinespecies.org/rest/AphiaRecordsByName/{}'.format(name)
        request = QtNetwork.QNetworkRequest(qcore.QUrl(request_name_url))
        reply = network_manager.get(request)

        def process_name_search():
            data = json.loads(str(reply.readAll(), 'utf-8'))

            for item in data:
                self.wk_model.addNewRow([item['scientificname'], item['AphiaID']])

        reply.finished.connect(process_name_search)

    def handle_selection_change(self, selected, deselected):
        self.add_row_btn.setEnabled(True)
        self.current_selection = [item.data() for item in selected.indexes()]

    def add_keyword(self):
        selection = self.results_table.selectionModel()
        self.parent().wormskeywords.model().addNewRow(self.current_selection)
