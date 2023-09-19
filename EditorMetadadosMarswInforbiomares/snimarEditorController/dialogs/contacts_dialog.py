# -*- coding: utf-8 -*-
##############################################################################
#
#  Title:   snimarEditorController/dialogs/contacts_dialog.py
#  Authors: Pedro Dias, Eduardo Castanho, Joana Teixeira
#  Date:    2015-08-11T16:14:20
#
# ---------------------------------------------------------------------------
#
#  XML metadata editor plugin for QGIS developed for the SNIMar Project.
#  Copyright (C) 2015  Eduardo Castanho, Pedro Dias, Joana Teixeira
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from builtins import str
from builtins import range
from qgis.PyQt import QtCore as qcore
from qgis.PyQt import QtGui as qgui
from qgis.PyQt import QtWidgets as qwidgets
from qgis.PyQt.QtCore import QMetaObject, Qt
from qgis.PyQt.QtWidgets import QWidget, QToolTip, QDateTimeEdit, QDialog
from qgis.PyQt.QtGui import QCursor, QFont

from EditorMetadadosMarswInforbiomares.snimarQtInterfaceView.pyuic4GeneratedSourceFiles.dialogs import contactListManagerWindow
from EditorMetadadosMarswInforbiomares.snimarEditorController.models import table_list_aux as tla
from EditorMetadadosMarswInforbiomares.snimarEditorController.models import customComboBoxModel as cus

import platform

import os
import json
import qgis
import uuid
import secrets

CONTACTFILE = os.path.join(os.path.join(os.path.abspath(os.path.expanduser('~')), '.snimar'), 'contact_list.json')
OUTRA = "Outra - Especificar Abaixo"


class ContactsDialog(QDialog, contactListManagerWindow.Ui_contacts_dialog):
    def __init__(self, parent, serverContact, resp, token, url, usernameGeo, passwordGeo, edition_mode=True):
        super(ContactsDialog, self).__init__(parent)
        if platform.system() != "Linux":
            font = QFont()
            font.setFamily(u"Segoe UI Symbol")
            self.setFont(font)
        # VIEW SETUP#############################################################
        self.setupUi(self)
        self.superParent = self.parent()

        for btn in self.findChildren(qwidgets.QPushButton, qcore.QRegExp('btn_*')):
            if '_add_' in btn.objectName():
                btn.setIcon(qgui.QIcon(':/resourcesFolder/icons/plus_icon.svg'))
                btn.setText('')
            elif '_del_' in btn.objectName():
                btn.setIcon(qgui.QIcon(':/resourcesFolder/icons/delete_icon.svg'))
                btn.setText('')
            elif '_clear_' in btn.objectName():
                btn.setIcon(qgui.QIcon(':/resourcesFolder/icons/delete_field.svg'))

        lists = ['phone', 'fax', 'email']
        for item in lists:
            btn = self.findChild(qwidgets.QPushButton, 'btn_add_' + item)
            btn.clicked.connect(self.add_list_row)
            btn = self.findChild(qwidgets.QPushButton, 'btn_del_' + item)
            btn.clicked.connect(self.del_list_row)

        for info in self.findChildren(qwidgets.QPushButton, qcore.QRegExp('info_*')):
            info.setIcon(qgui.QIcon(':/resourcesFolder/icons/help_icon.svg'))
            info.setText('')
            info.pressed.connect(self.printHelp)

        # Contact list connections and variables
        self.username = usernameGeo
        self.password = passwordGeo
        self.users = serverContact
        self.session = resp
        self.contact_array = None
        self.open_contact_array()
        self.current_contact = None
        self.contact_list.clearSelection()
        self.contactPanel.setDisabled(True)
        self.server = url
        self.token = token

        # SETUP THE DIALOG MODE
        if edition_mode:  # EDITION MODE

            self.orgs = {}
            org = self.superParent.orgs
            for x in org:
                name = org[x] + " (" + x + ")"
                self.orgs[x] = cus.CodeListItem(name, name, name)

            self.combo_org.setModel(
                cus.CustomComboBoxModel(self,
                                        [cus.CodeListItem(OUTRA, OUTRA, OUTRA)] + sorted(list(self.orgs.values()),
                                                                                         key=lambda x: x.term_pt)))
            self.combo_org.currentIndexChanged.connect(self.check_org)
            self.btn_contact_add.setVisible(True)
            self.btn_contact_del.setVisible(True)
            self.cancelChanges()
            self.btn_add_contact_metadata.setVisible(False)

            # CONNECTING FIELDS THAT CAN BE CHANGED
            self.name.textChanged.connect(self.changesMade)
            self.organization.textChanged.connect(self.changesMade)
            self.city.textChanged.connect(self.changesMade)
            self.postalcode.textChanged.connect(self.changesMade)
            self.country.textChanged.connect(self.changesMade)
            self.delivery_point.textChanged.connect(self.changesMade)
            self.phone.model().rowsInserted.connect(self.changesMade)
            self.fax.model().rowsInserted.connect(self.changesMade)
            self.email.model().rowsInserted.connect(self.changesMade)
            self.online.textChanged.connect(self.changesMade)
            self.phone.model().rowsRemoved.connect(self.changesMade)
            self.fax.model().rowsRemoved.connect(self.changesMade)
            self.email.model().rowsRemoved.connect(self.changesMade)
            self.online.textChanged.connect(self.changesMade)

            # SETUP MANDATORY FIELDS VISUAL VALIDATION
            self.organization.editingFinished.connect(self.setup_mandatory_label)
            self.name.editingFinished.connect(self.setup_mandatory_label)
            self.setup_mandatory_label()

            # ACTIONS SETUP
            self.btn_contact_save.clicked.connect(self.save_contact)  # save contact
            self.btn_cancelClose.clicked.connect(self.cancelChanges)  # cancel changes and revert contact
            self.btn_contact_add.clicked.connect(
                self.new_contact)  # add new contact if changes in current contact exists ask...
            self.btn_contact_del.clicked.connect(self.delete_contact)  # delete contact with confirmation

            self.contact_list.itemClicked.connect(
                self.selection_changed)  # change current selection if changes exists ask...
        else:  # EXPORT MODE
            self.contactPanel.hide()
            self.btn_add_contact_metadata.setVisible(True)
            self.btn_contact_add.setVisible(False)
            self.btn_contact_del.setVisible(False)
            self.adjustSize()

        # ACTIONS SETUP
        self.contact_list.itemClicked.connect(self.selection_changed_export_Mode)  # change current selection
        # ACTIONS FUNCTIONS
        self.eater = tla.EatWheel()
        for x in self.findChildren(qwidgets.QComboBox):
            x.installEventFilter(self.eater)
            x.setFocusPolicy(Qt.StrongFocus)
        for x in self.findChildren(QDateTimeEdit):
            x.installEventFilter(self.eater)
            x.setFocusPolicy(Qt.StrongFocus)
        
    # Função set message
    @qcore.pyqtSlot()
    def showAlert(self, texto, title, icon):
        message = qwidgets.QMessageBox(self)
        message.setWindowTitle(title)
        message.setIcon(icon)
        message.setText(texto)
        message.show()

    @qcore.pyqtSlot()
    def mountContactGeo(self, contacto, username, password, email):
        name = contacto.get('name')

        name = name.split(' ')
        if len(name) >= 1:
            nome = name[0] 
            surname = name[len(name)-1]
        else:
            nome = name[0] 
            surname = ''
        
        organisation = contacto.get('organization')
        emailAddresses = contacto.get('email')

        addresses = [
            {
                "address":  contacto.get('delivery_point'),
                "city": contacto.get('city'),
                "country": contacto.get('country'),
                "zip": contacto.get('postalcode')
            }
        ]

        jsonUser = {
            "username": str(username),
            "password": 'P'+str(password)+'s#',
            "profile": 'RegisteredUser',
            "surname": surname,
            "emailAddresses": emailAddresses,
            "addresses": addresses,
            "organisation": organisation,
            "profile": 'RegisteredUser',
            "enabled": bool(0),
            "name":nome
        }
        json_object = json.dumps(jsonUser, indent = 4) 

        return json_object

    @qcore.pyqtSlot()
    def printHelp(self):
        QToolTip.showText(QCursor.pos(), tla.formatTooltip(
            self.superParent.helps['contactListManagerWindow'][self.sender().objectName()]),
                          None)

    @qcore.pyqtSlot()
    def save_contact(self):

        flags = self.mandatory_state()
        if all(flag == True for flag in list(flags.values())):
            # Get the data
            self.current_contact['name'] = str(self.name.text())
            self.current_contact['organization'] = str(self.organization.text())
            self.current_contact['delivery_point'] = str(self.delivery_point.text())
            self.current_contact['city'] = str(self.city.text())
            self.current_contact['postalcode'] = str(self.postalcode.text())
            self.current_contact['country'] = str(self.country.text())

            '''self.current_contact['utilizador'] = str(self.utilizador.text)
            self.current_contact['password'] = str(self.passwd.text())

            ##Check if utilizador and password is set
            if len(str(self.utilizador.text())) < 3:
                self.showAlert('Erro Utilizador inválido. \n Por favor forneça um utilizador válido.','Ocorreu um erro',qwidgets.QMessageBox.Critical)
                return
            elif len(str(self.passwd.text())) < 8:
                self.showAlert('Erro Password inválida. \n A Password deve conter pelo menos 8 caracteres.','Ocorreu um erro',qwidgets.QMessageBox.Critical)
                return
            
            '''

            items = [str(self.phone.item(index).text()) for index in range(self.phone.count())]
            self.current_contact['phone'] = items

            items = [str(self.email.item(index).text()) for index in range(self.email.count())]
            self.current_contact['email'] = items

            items = [str(self.fax.item(index).text()) for index in range(self.fax.count())]
            self.current_contact['fax'] = items

            self.current_contact['online'] = str(self.online.text())
            if self.current_contact['index'] == -1:
                print('Inserir')

                key = uuid.uuid4()
                key = str(key).split('-')
                username = 'ipma'+key[0]
                email = 'visit@test.com'

                password_length = 8
                password = secrets.token_urlsafe(password_length)
                self.current_contact['index'] = len(self.contact_array)

                ##Mount Contact Geonetwork
                contacto = self.mountContactGeo(self.current_contact, username, password, email)
                #print(contacto)

                #Update Geonetwork
                session = self.session
                xsrf_token = self.token
                if self.server:
                    url = self.server + '/srv/api/users/'
                    headers = {'Accept': 'application/json, text/plain', 'Content-Type': 'application/json;charset=UTF-8', 'X-XSRF-TOKEN': xsrf_token}

                    response = session.put(url, auth=(self.username, self.password), headers=headers, data=contacto)

                    ##Get users geonetwork
                    url = str(self.server) + '/srv/api/users'
                    headers = {'Accept': 'application/json', 'X-XSRF-TOKEN': xsrf_token}

                    response = session.get(url, auth=(self.username, self.password), headers=headers)
                    serverUsers = json.loads(response.text)

                    for user in serverUsers:
                        usernameServer = user.get('username')
                        if usernameServer == username:
                            id = user.get('id')
                            self.current_contact['id'] = id
                            #print(self.current_contact)
    
                self.contact_array.append(self.current_contact)
                item_label = self.current_contact['name'] + ' - ' + self.current_contact['organization']
                self.contact_list.addItem(item_label)
                self.contact_list.setCurrentRow(self.current_contact['index'])
            else:
                #print('Atualização')
                try:
                    contacto = self.contact_array[self.current_contact['index']]
                    if contacto.get('id'):
                        #Get Nome Sobrenome, email, Organização, Endereço, Estado, Cidade, Pais 
                        id = contacto.get('id')
                        name = contacto.get('name')

                        name = name.split(' ')
                        if len(name) >= 1:
                           nome = name[0] 
                           surname = name[len(name)-1]
                        else:
                            nome = name[0] 
                            surname = ''
                        organisation = contacto.get('organization')
                        emailAddresses = contacto.get('email')

                        addresses = [
                            {
                                "address":  contacto.get('delivery_point'),
                                "city": contacto.get('city'),
                                "country": contacto.get('country'),
                                "zip": contacto.get('postalcode')
                            }
                        ]

                        jsonUser = {
                            "surname": surname,
                            "id":id,
                            "emailAddresses": emailAddresses,
                            "addresses": addresses,
                            "organisation": organisation,
                            "profile": 'RegisteredUser',
                            "enabled": bool(0),
                            "name":nome
                        }
                        json_object = json.dumps(jsonUser, indent = 4) 
                        #print(json_object)
                        
                        #Update Geonetwork
                        session = self.session
                        xsrf_token = self.token
                        if self.server:
                            url = self.server + '/srv/api/users/'+str(id)
                            headers = {'Accept': 'application/json, text/plain', 'Content-Type': 'application/json;charset=UTF-8', 'X-XSRF-TOKEN': xsrf_token}

                            response = session.put(url, auth=(self.username, self.password), headers=headers, data=json_object)

                        #print(self.token)
                except:
                    exist = False
                    #print('Não tem id')

                self.contact_array[self.current_contact['index']] = self.current_contact
                item_label = self.current_contact['name'] + ' - ' + self.current_contact['organization']
                self.contact_list.item(self.current_contact['index']).setText(item_label)
            self.save_contact_array()
            self.present_contact()
            self.changes = False
            self.btn_cancelClose.setDisabled(True)
            self.btn_contact_save.setDisabled(True)

    @qcore.pyqtSlot()
    def changesMade(self):
        self.changes = True
        self.btn_cancelClose.setDisabled(False)
        self.btn_contact_save.setDisabled(False)

    @qcore.pyqtSlot()
    def cancelChanges(self):
        self.present_contact()
        self.changes = False
        self.btn_cancelClose.setDisabled(True)
        self.btn_contact_save.setDisabled(True)

    @qcore.pyqtSlot()
    def new_contact(self):
        self.changes = True
        self.current_contact = None
        self.present_contact()
        self.current_contact = self.generate_contact_object()
        self.contact_list.clearSelection()
        self.contactPanel.setDisabled(False)

    @qcore.pyqtSlot()
    def delete_contact(self):
        message = qwidgets.QMessageBox()
        message.setModal(True)
        message.setWindowTitle(u'Remover contacto?')
        message.setIcon(qwidgets.QMessageBox.Warning)
        message.setText(u"Tem a certeza que pretende remover contacto?\n(Operação Irreversivel!)")
        message.addButton(u'Remover', qwidgets.QMessageBox.AcceptRole)
        message.addButton(u'Cancelar', qwidgets.QMessageBox.RejectRole)
        ret = message.exec_()
        if ret == qwidgets.QMessageBox.AcceptRole:
            # get current selected index in list
            index = self.contact_list.currentRow()
            if index < 0:
                return
            self.contact_list.takeItem(index)
            self.contact_array.pop(index)
            self.save_contact_array()
            self.contact_list.clearSelection()
            self.contactPanel.setDisabled(True)
            self.current_contact = None
            self.present_contact()
            self.changes = False

    @qcore.pyqtSlot()
    def selection_changed(self):
        index = self.contact_list.currentRow()
        if self.changes and self.current_contact is not None:
            message = qwidgets.QMessageBox()
            message.setModal(True)
            message.setWindowTitle(u'Existem Alterações.')
            message.setIcon(qwidgets.QMessageBox.Warning)
            message.setText(u"Deseja guardar as alterações efectuadas?")
            message.addButton(u'Guardar', qwidgets.QMessageBox.AcceptRole)
            message.addButton(u'Cancelar', qwidgets.QMessageBox.RejectRole)
            ret = message.exec_()
            if ret == qwidgets.QMessageBox.AcceptRole:
                self.save_contact()
        self.contactPanel.setDisabled(False)
        self.changes = False
        self.current_contact = self.contact_array[index]
        self.contact_list.setCurrentRow(index)
        self.present_contact()
        self.cancelChanges()

    @qcore.pyqtSlot()
    def selection_changed_export_Mode(self):
        index = self.contact_list.currentRow()
        self.current_contact = self.contact_array[index]

    # CONTACT ARRAY OPERATIONS
    def save_contact_array(self):
        """Saves the current contact array to the contact_list.json"""
        #print(self.contact_array)
        with open(CONTACTFILE, 'w') as fp:
            json.dump(self.contact_array, fp)

    def open_contact_array(self):
        with open(CONTACTFILE, 'r') as file:
            self.contact_array = json.loads(file.read())
        
        #print(self.contact_array)
        for user in self.users:
            if user.get('profile') == 'RegisteredUser' and user.get('name') != 'nobody':
                userId = user.get('id')
                igual = 0
                for contact in self.contact_array:
                    try:
                        id = contact.get('id')
                        if id :
                            if id == userId:
                                igual = igual + 1
                    except:
                        exist = False
                
                if igual == 0:
                    name = str(user.get('name')) + ' ' + str(user.get('surname'))
                    organisation = str(user.get('organisation'))
                    emailAddresses = user.get('emailAddresses')
                    addresses = user.get('addresses')
                    city = addresses[0]['city']
                    postalcode = addresses[0]['zip']
                    country = addresses[0]['country']
                    #userId = user.get('id')

                    contact = {
                        "index": len(self.contact_array),
                        "name": name,
                        "organization": organisation,
                        "delivery_point": '',
                        "city": city,
                        "postalcode": postalcode,
                        "country": country,
                        "phone": [], 
                        "fax": [], 
                        "email": emailAddresses, 
                        "online": '',
                        "id": userId
                    }

                    self.contact_array.append(contact)
                    
        self.fix_contact_list()
        if self.contact_array is None:
            self.contact_array = []

        if len(self.contact_array) > 0:
            list_item_texts = [(x['name'], x['organization']) for x in self.contact_array]
            items_labels = [item_text[0] + ' - ' + item_text[1] for item_text in list_item_texts]
            self.contact_list.addItems(items_labels)

    @qcore.pyqtSlot()
    def add_list_row(self):
        """Add a new row to the specific list that shares the same name with the button that
        emits the signal that fires the slot."""
        sender_name = self.sender().objectName()
        target_list = self.findChild(qwidgets.QListWidget, sender_name.split('_')[2])
        target_input = self.findChild(qwidgets.QLineEdit, sender_name.split('_')[2] + '_input')

        if target_list is not None and target_input is not None:
            input_text = target_input.text()
            if len(input_text) > 0:
                item = qwidgets.QListWidgetItem(input_text)
                item.setFlags(item.flags() | qcore.Qt.ItemIsEditable)
                target_list.addItem(item)
                target_input.setText('')

    @qcore.pyqtSlot()
    def del_list_row(self):
        """Works like the add_list_row, but deletes the selected row from the list that shares
        its name with button that emits the signal."""
        sender_name = self.sender().objectName()
        target_list = self.findChild(qwidgets.QListWidget, sender_name.split('_')[2])

        index = target_list.currentRow()
        if index is not None:
            target_list.takeItem(index)
            target_list.setCurrentRow(-1)

    @qcore.pyqtSlot()
    def present_contact(self):
        self.name.clear()
        self.organization.clear()
        self.delivery_point.clear()
        self.city.clear()
        self.postalcode.clear()
        self.country.clear()
        self.phone.clear()
        self.fax.clear()
        self.email.clear()
        self.online.clear()

        if self.current_contact is not None:
            self.name.setText(self.current_contact['name'])
            self.set_org(self.current_contact['organization'])
            # self.organization.setText(self.current_contact['organization'])
            self.delivery_point.setText(self.current_contact['delivery_point'])
            self.city.setText(self.current_contact['city'])
            self.postalcode.setText(self.current_contact['postalcode'])
            self.country.setText(self.current_contact['country'])
            self.phone.addItems(self.current_contact['phone'])
            self.fax.addItems(self.current_contact['fax'])
            self.email.addItems(self.current_contact['email'])
            self.online.setText(self.current_contact['online'])

        self.setup_mandatory_label()

    # AUX FUNCTIONS ###########################################################
    def generate_contact_object(self):
        """Returns an empty contact dict"""
        d = {}
        d['index'] = -1
        d['name'] = None
        d['organization'] = None
        d['delivery_point'] = None
        d['city'] = None
        d['postalcode'] = None
        d['country'] = None
        d['phone'] = []
        d['fax'] = []
        d['email'] = []
        d['online'] = None
        return d

    def mandatory_state(self):
        """Validates that mandatory fields are written."""

        organization = len(str(self.organization.text())) > 0

        return {
            'organization': True
            }

    def setup_mandatory_label(self):
        state = self.mandatory_state()
        if not state['organization']:
            label_text = u'Nome da Organização'
            label_text += u' ' + u'\u26a0'
            self.label_organization.setText(label_text)
            self.label_organization.setToolTip(u'Elemento obrigatório em falta')
        else:
            label_text = u'Nome da Organização'
            self.label_organization.setText(label_text)
            self.label_organization.setToolTip(u'')

    def output_contact(self):
        return self.current_contact

    def fix_contact_list(self):
        ret = []
        for x in self.contact_array:
            x['fax'] = x.get('faxlist', [])
            x['online'] = x.get('online')[0] if x.get('online') is not None and type(x.get('online')) == list and len(
                x.get('online')) > 0 else  x.get('online')
            if not x['online']:
                x['online'] = None
            try:
                del x['faxlist']
                del x['address']
            except KeyError:
                continue
            ret.append(x)
        return ret

    def check_org(self):
        if self.combo_org.currentText() == OUTRA:
            #NOT IN THE LIST
            self.organization.setDisabled(False)
            self.organization.setText("")
        else:
            #IN THE LIST
            self.organization.setDisabled(True)
            self.organization.setText(self.combo_org.currentText())

    def set_org(self, org_name):

        if org_name in [x.term for x in list(self.orgs.values())]:
            self.combo_org.setCurrentIndex(self.combo_org.findText(org_name))
        else:
            self.combo_org.setCurrentIndex(0)
            self.check_org()
            self.organization.setText(org_name)
