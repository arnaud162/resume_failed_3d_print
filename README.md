If your 3D print was interupted measure the height of the unfinished part.

Use then the python script or the .exe (inside dist folder) to generate a gcode starting from the height of the unfinished part.

Python script or .exe must be placed in the same folder as the original gcode file, and executed from this folder.

Let's say for instance part printing was interupted at 20mm, a new gcode starting at altitude z=20mm will be generated. 

This program was only tested on an easythreed x1, so to be used with caution.
