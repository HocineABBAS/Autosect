# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class interfaceautosect(object):
    def setupUi(self, Autosect_dialog):
        Autosect_dialog.setObjectName("Autosect_dialog")
        Autosect_dialog.resize(336, 256)
        self.selectLayerComboBox = QtWidgets.QComboBox(Autosect_dialog)
        self.selectLayerComboBox.setGeometry(QtCore.QRect(50, 40, 241, 21))
        self.selectLayerComboBox.setObjectName("selectLayerComboBox")
        self.label = QtWidgets.QLabel(Autosect_dialog)
        self.label.setGeometry(QtCore.QRect(50, 20, 101, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Autosect_dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 101, 21))
        self.label_2.setObjectName("label_2")
        self.distanceSpinBox = QtWidgets.QDoubleSpinBox(Autosect_dialog)
        self.distanceSpinBox.setGeometry(QtCore.QRect(50, 100, 241, 21))
        self.distanceSpinBox.setDecimals(9)
        self.distanceSpinBox.setMaximum(999999999.999999)
        self.distanceSpinBox.setProperty("value", 1.0)
        self.distanceSpinBox.setObjectName("distanceSpinBox")
        self.layerNameLine = QtWidgets.QLineEdit(Autosect_dialog)
        self.layerNameLine.setGeometry(QtCore.QRect(50, 160, 241, 20))
        self.layerNameLine.setObjectName("layerNameLine")
        self.labelLayerName = QtWidgets.QLabel(Autosect_dialog)
        self.labelLayerName.setGeometry(QtCore.QRect(50, 140, 81, 21))
        self.labelLayerName.setObjectName("labelLayerName")
        self.buttonBox = QtWidgets.QDialogButtonBox(Autosect_dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-80, 210, 371, 20))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Autosect_dialog)
        self.buttonBox.accepted.connect(Autosect_dialog.accept)
        self.buttonBox.rejected.connect(Autosect_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Autosect_dialog)

    def retranslateUi(self, Autosect_dialog):
        _translate = QtCore.QCoreApplication.translate
        Autosect_dialog.setWindowTitle(_translate("Autosect_dialog", "autonet"))
        self.label.setText(_translate("Autosect_dialog", "Sélection de la rivière "))
        self.label_2.setText(_translate("Autosect_dialog", "Taille du trançon "))
        self.labelLayerName.setText(_translate("Autosect_dialog", "Fichier en sortie"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Autosect_dialog = QtWidgets.QDialog()
    ui = Ui_Autosect_dialog()
    ui.setupUi(Autosect_dialog)
    Autosect_dialog.show()
    sys.exit(app.exec_())
