import rhinoscriptsyntax as rs
"""Activates current layer by selecting an object"""

id = rs.GetObject("Select object to make current layer out of")
layerId = rs.ObjectLayer(id)
layer = rs.LayerName(layerId)
rs.CurrentLayer(layer)

print ("The current layer has been changed to "  + layer)
