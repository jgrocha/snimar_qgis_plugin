# coding=utf-8
from qgis.PyQt.QtWidgets import QDialog
from EditorMetadadosMarswInforbiomares.CONSTANTS import Scopes as SCOPES
from EditorMetadadosMarswInforbiomares.snimarEditorController import filemanager
import requests
from qgis.PyQt.QtGui import QPixmap, QIcon
from qgis.PyQt import QtCore
from qgis.PyQt import QtCore as qcore
from EditorMetadadosMarswInforbiomares.snimarProfileModel import snimarProfileModel, validation
from EditorMetadadosMarswInforbiomares.snimarEditorController.metadadoSNIMar import MetadadoSNIMar, vality_msg
from qgis.PyQt.QtWidgets import QPushButton, QHeaderView, QMenu, QAction, QProgressDialog, QProgressBar, QMessageBox, QAbstractItemView, QMainWindow, QWidget, QLineEdit, QTabBar
import EditorMetadadosMarswInforbiomares
from EditorMetadadosMarswInforbiomares.snimarQtInterfaceView.pyuic4GeneratedSourceFiles.dialogs import read_geonetwork
from EditorMetadadosMarswInforbiomares import resources
import xml.dom.minidom
import uuid
import datetime
import os
import json

class read_Geonetwork(QDialog, read_geonetwork.Ui_About):
    def __init__(self):
        super(read_Geonetwork, self).__init__()
        self.setupUi(self)
        #self.version.setText(u"Versão:" + EditorMetadadosMarswInforbiomares.__version__)
        
        def load_codelists(self):
            with open('/home/utilizador/.local/share/QGIS/QGIS3/profiles/default/python/plugins/EditorMetadadosMarswInforbiomares/resourcesFolder/CodeLists/SNIMar_GMXCODELISTS.json') as json_data:
                self.codelists = json.load(json_data)
            with open('/home/utilizador/.local/share/QGIS/QGIS3/profiles/default/python/plugins/EditorMetadadosMarswInforbiomares/resourcesFolder/CodeLists/SNIMar_HELPS.json') as json_help:
                self.helps = json.load(json_help)
            with open('/home/utilizador/.local/share/QGIS/QGIS3/profiles/default/python/plugins/EditorMetadadosMarswInforbiomares/resourcesFolder/CodeLists/SNIMar_ReferenceSystems.json') as json_ref:
                self.reference_systems = json.load(json_ref)
            with open('/home/utilizador/.local/share/QGIS/QGIS3/profiles/default/python/plugins/EditorMetadadosMarswInforbiomares/resourcesFolder/CodeLists/SNIMar_ORGS.json') as json_ref:
                self.orgs = json.load(json_ref)

        def editor_dirname(self):
            """
            Returns the name of the directory for the editor contact and working
            metadata lists.
            """
            return os.path.join(os.path.abspath(os.path.expanduser('~')), '.snimar')

        def setup_editor_dir(self):
            if not os.path.exists(self.editor_dirname()):
                os.mkdir(self.editor_dirname())

        #self.codelists = None
        #self.helps = None
        #self.orgs = None
        #self.reference_systems = None
        #load_codelists(self)

        #self.tracked_list = filemanager.FileManager(to_save=True, editordir=editor_dirname(self))
        #self.tmp_list = filemanager.FileManager(to_save=False, editordir=editor_dirname(self))
        #self.open_list = filemanager.FileManager(to_save=False, editordir=editor_dirname(self))
        #self.last_open_dir = os.path.expanduser('~')

        # Função set error 
        def showError(texto):
            message = QMessageBox(self)
            message.setWindowTitle(u'Erro ao abrir o endereço')
            message.setIcon(QMessageBox.Critical)
            message.setText(texto)
            message.show()

        def check_validity_xml(xmlFile):
            try:
                xmlCheck = xml.dom.minidom.parseString(xmlFile)
                return True
            except:
                showError('Ocorreu um erro ao ler o XML fornecido. \n Por favor forneça um endereço XML válido.')
                return False

        def readFile(fileName):
            try:
                open(fileName, "r")
                md = validation.validate(fileName)

                if md is None:
                    showError('Ocorreu um erro ao ler o XML fornecido. \n Por favor forneça um endereço XML válido.')
                    return
                else:
                    meta = MetadadoSNIMar(self, xml_doc=fileName, md=md)
                    meta.setObjectName(fileName)

                    if SCOPES.get_code_representation(md.hierarchy) != SCOPES.SERVICES:
                        common = md.identification
                    else:
                        common = md.serviceidentification

                    if common is None:
                        showError('Ocorreu um erro ao ler o XML fornecido. \n O metadado está corrupto. Por favor verifique o conteúdo do XML.')
                        return

                    filelist = {
                        'path': fileName, 'name': fileName, 'object': meta, 'title': common.title,
                        'doc_type': SCOPES.get_rich_text_translation(md.hierarchy),
                        'id': md.identifier
                    }

                    #self.open_list.track_new_file(**filelist)
                    #print(EditorMetadadosMarswInforbiomares)
                    #self.tabWidget.setCurrentIndex(self.tabWidget.addTab(meta, os.path.basename(doc)))
                    #print('open_metadata_xml_file')
            except IOError as e:
                showError('Ocorreu um erro ao ler o XML fornecido. \n Por favor forneça um endereço XML válido.')
                return

        ### Função Carregar
        @qcore.pyqtSlot()
        def checkUrl(url):
            #Guarda url na variavel link
            link = str(url.text())
            try:
                f = requests.get(link)
                xmlFile = f.text
                xmlValid = check_validity_xml(xmlFile)

                if xmlValid:
                    #geração de randon uuid para salvar XML
                    randonUuid = uuid.uuid4()
                    randonUuid = str(randonUuid)
                    randonUuid = randonUuid.replace("-","")
                    now = datetime.datetime.now()
                    fileName = str(now.strftime("%d%m%y")) + str(randonUuid)

                    ##Save File
                    checkPath = os.path.isdir('snimar_qgis_plugin')
                    if checkPath:
                        f = open("snimar_qgis_plugin/" +fileName + '.xml', "w")
                        f.write(xmlFile)
                        f.close()
                    else:
                        path = 'snimar_qgis_plugin'
                        os.mkdir(path)
                        f = open("snimar_qgis_plugin/" +fileName + '.xml', "w")
                        f.write(xmlFile)
                        f.close()
                    #readFile("snimar_qgis_plugin/" +fileName + ".xml")
                    #editorMetadadosMarswInforbiomares.sayHellow()
                    #std = EditorMetadadosMarswInforbiomares(QMainWindow, snimarEditorMainWindow.Ui_mainwindow)
                    fileName = "snimar_qgis_plugin/" +fileName + ".xml"
                    
                    EditorMetadadosMarswInforbiomares.editorMetadadosMarswInforbiomares.connectFile(fileName)
                    self.done(1)
            except requests.exceptions.RequestException as e:
                showError('Endereço XML inválido. Forneça um endereço XML válido.')

        ##Acções botões    
        self.carregar.clicked.connect(lambda: checkUrl(self.url))
        self.voltar.clicked.connect(lambda: self.done(1))