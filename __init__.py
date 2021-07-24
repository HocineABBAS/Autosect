# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AutoSect
                                 A QGIS plugin
 AutoSect a pour tâche de générer des points le long de lignes à une distance spécifique
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-06-21
        copyright            : (C) 2020 by Hocine ABBAS
        email                : hocine.abbas@ent.univ-orleans.fr
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

# noinspection PyPep8Naming
def classFactory(iface):# pylint: disable=invalid-name
    """Load AutoSect class from file AutoSect.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    
    from .Autosect import Autosect
    return Autosect(iface)
