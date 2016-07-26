import rhinoscriptsyntax as rs
"""Turn all layers on in a document"""

layers = rs.LayerNames()
layersOn = []
if layers:
    for layer in layers:
        if rs.LayerVisible(layer)==False:
           rs.LayerVisible(layer,True)
           layersOn.append[layer]
