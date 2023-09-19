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
from EditorMetadadosMarswInforbiomares.snimarQtInterfaceView.pyuic4GeneratedSourceFiles.dialogs import login_geonetwork
from EditorMetadadosMarswInforbiomares import resources
import xml.dom.minidom
import uuid
import datetime
import os
import json

class login_Geonetwork(QDialog, login_geonetwork.Ui_Login_Geonetwork):
    def __init__(self, serverURL):
        super(login_Geonetwork, self).__init__()
        self.setupUi(self)

        ### Funções 
        # Função set error 
        def showError(texto, title, icon):
            message = QMessageBox(self)
            message.setWindowTitle(title)
            message.setIcon(icon)
            message.setText(texto)
            message.show()

        @qcore.pyqtSlot()
        def loginGeonetwork(user, passwd):
            # Set up your username and password:
            username = user.text()
            password = passwd.text()

            # Set up your server and the authentication URL:
            authenticate_url = serverURL + '/srv/eng/info?type=me'

            # To generate the XRSF token, send a post request to the following URL: http://localhost:8080/geonetwork/srv/eng/info?type=me
            session = requests.Session() 
            response = session.post(authenticate_url)

            # Extract XRSF token
            xsrf_token = response.cookies.get("XSRF-TOKEN")
            
            # Set header for connection
            headers = {'Accept': 'application/json', 'X-XSRF-TOKEN': xsrf_token}

            url = serverURL+"/signin"

            response = session.post(url,
                auth=(username, password),
                headers=headers,
            )   

            if response.status_code == 200:
                EditorMetadadosMarswInforbiomares.editorMetadadosMarswInforbiomares.saveGeonet(xsrf_token, session, username, password)
                self.done(1)
            else:
                showError('Dados inválidos!!! \n Utilizador ou password errados.', 'Ocorreu um erro',QMessageBox.Critical)

        ##Acções botões    
        self.carregar.clicked.connect(lambda: loginGeonetwork(self.user, self.password))
        self.voltar.clicked.connect(lambda: self.done(1))