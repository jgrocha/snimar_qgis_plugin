# coding=utf-8
from PyQt4.QtGui import QDialog, QPixmap
import EditorMetadadosSNIMar
from EditorMetadadosSNIMar.snimarQtInterfaceView.pyuic4GeneratedSourceFiles.dialogs import about


class About(QDialog, about.Ui_About):
    def __init__(self):
        super(About, self).__init__()
        self.setupUi(self)
        self.version.setText(u"Versão:" + EditorMetadadosSNIMar.__version__)
        self.pushButton.clicked.connect(lambda: self.done(1))
