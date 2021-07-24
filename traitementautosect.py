# -*- coding: utf-8 -*-

from qgis.PyQt.QtCore import (
    QVariant,
    QCoreApplication
)
from qgis.core import (
    QgsVectorLayer,
    QgsMarkerSymbol,
    QgsGeometry,
    QgsProject,
    QgsField,
    QgsFields,
    QgsFeature,
    QgsMessageLog,
    QgsPoint,
    Qgis,
    QgsSingleSymbolRenderer,
    QgsVectorFileWriter,
    QgsUnitTypes
)


def creation_point(startpoint, distance, geom):

    if distance <= 0:
        distance = geom.length()
    La_longueur = geom.length()
    La_distance = distance
    feats = []
    point = geom.interpolate(startpoint)
    point = QgsGeometry.fromPointXY(point.asPoint())
    field_id = QgsField(name="id", type=QVariant.Int)
    field = QgsField(name="dist", type=QVariant.Double)
    fields = QgsFields()
    fields.append(field_id)
    fields.append(field)
    feature = QgsFeature(fields)
    feature['dist'] = startpoint
    feature.setGeometry(point)
    feats.append(feature)
    while startpoint + La_distance <= La_longueur:
        point = geom.interpolate(startpoint + La_distance)
        feature = QgsFeature(fields)
        feature['dist'] = (startpoint + La_distance)
        feature.setGeometry(point)
        feats.append(feature)
        La_distance = La_distance + distance
    return feats


def traitement_le_long_du_cours_eau(layerout, startpoint, distance, layer):

    crs = layer.crs().authid()
    shape = False
    if shape:
        # define fields for feature attributes. A list of QgsField objects is needed
        fields = [QgsField("first", QVariant.Int),
                  QgsField("second", QVariant.String)]
        writer = QgsVectorFileWriter("my_shapes.shp",
                                     "CP1250",
                                     fields,
                                     Qgis.WKBPoint,
                                     crs,
                                     "ESRI Shapefile")
        fet = QgsFeature()
        fet.setGeometry(QgsGeometry.fromPoint(QgsPoint(10, 5)))
        fet.setAttributes([1, "text"])
        writer.addFeature(fet)
        del writer
        layer_type = "Shapefile"
    else:
        layer_type = "memory"
    virt_layer = QgsVectorLayer("Point?crs=%s" % crs,
                                layerout,
                                layer_type)
    provider = virt_layer.dataProvider()
    virt_layer.startEditing()
    provider.addAttributes([QgsField("tronçon", QVariant.Int)])
    layerft=layer.getFeatures()
    for feature in layerft:
        geom = feature.geometry()
        features = creation_point(startpoint,
                                    distance,
                                    geom)
        provider.addFeatures(features)
        virt_layer.updateExtents()

    proj = QgsProject.instance()
    proj.addMapLayers([virt_layer])
    virt_layer.commitChanges()
    virt_layer.reload()
    virt_layer.triggerRepaint()
    return
