# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AutoSectDialog
                                 A QGIS plugin
 AutoSect a pour tâche de générer des points le long de lignes à une distance spécifique
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-06-21
        git sha              : $Format:%H$
        copyright            : (C) 2020 by Hocine ABBAS
        email                : hocine.abbas@ent.univ-orleans.fr
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import os

from qgis.PyQt import uic

from qgis.PyQt.QtCore import QSettings
from qgis.PyQt.QtWidgets import QDialog, QDialogButtonBox

from qgis.core import (
    QgsMapLayer,
    QgsWkbTypes,
    QgsUnitTypes,
    QgsDistanceArea,
    QgsProject
)


from .traitementautosect import traitement_le_long_du_cours_eau

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'Autosect_dialog_base.ui'))

class AutosectDialog(QDialog, FORM_CLASS):
    """Constructor."""
    def __init__(self, iface):
        self.iface = iface
        QDialog.__init__(self)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.setWindowTitle('Autosect')
        self.qgisSettings = QSettings()
        self.okbutton = self.buttonBox.button(QDialogButtonBox.Ok)
        self.okbutton.setEnabled(True)
        self.da = QgsDistanceArea()


        for layer in self.iface.mapCanvas().layers():
            if layer.type() == QgsMapLayer.VectorLayer and \
                 layer.geometryType() == QgsWkbTypes.LineGeometry:
                self.selectLayerComboBox.addItem(layer.name(), layer)

    def chargement_de_la_couche(self):
        index = self.selectLayerComboBox.currentIndex()
        return self.selectLayerComboBox.itemData(index)


    def accept(self):
        layer = self.chargement_de_la_couche()
        layerout = self.layerNameLine.text()
        distance = self.distanceSpinBox.value()
        startpoint = 0

        projection_setting_key = "Projections/defaultBehaviour"
        old_projection_setting = self.qgisSettings.value(projection_setting_key)
        self.qgisSettings.setValue(projection_setting_key, "useGlobal")
        self.qgisSettings.sync()

        traitement_le_long_du_cours_eau(layerout, startpoint, distance, layer)
        self.qgisSettings.setValue(projection_setting_key, old_projection_setting)
        QDialog.accept(self)
