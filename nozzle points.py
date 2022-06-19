#!/usr/bin/env python

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'C:/Users/v-kargor/Desktop/MKWS')

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS

geompy = geomBuilder.New()

f = open("C:/Users/v-kargor/Desktop/MKWS/nozzle.txt")
n = 0
for l in f:
	x, y, z = [ float(v) for v in l.split() ]
	print (x, y, z, n)
	pt = geompy.MakeVertex(x, y, z)
	geompy.addToStudy(pt, "Vertex_%s"%(n))
	n += 1
	pass
    
if salome.sg.hasDesktop():
	salome.sg.updateObjBrowser()
    