#!/usr/bin/env python
# coding: utf-8

import arcgis
from arcgis.gis import GIS
gis = GIS()

map1 = gis.map('Concord, NH')
map1

# Item Added From Toolbar
# Title: New Hampshire Crime 2018 | Type: Feature Service | Owner: map_n_hike
item = gis.content.get("097d2171fc36413c9cf3501592d2ae51")
item

map1.add_layer(item)
map1

