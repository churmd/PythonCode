#!/usr/bin/env python3

import pi3d
from rotatingCamera import RotatingCamera

"""Practice using the pi3d library, following demo
    https://www.youtube.com/watch?v=_jdYhRDygAM."""

#create display
DISPLAY = pi3d.Display.create()

#create mouse obj
mymouse = pi3d.Mouse(restrict = False)
mymouse.start()

#create camera
CAM = RotatingCamera(5, mymouse)

#create keyboard obj
mykeys = pi3d.Keyboard()

#create cubes
cubeList = []
for i in range(10) :
    cube = pi3d.Cuboid(x = i)
    cube.set_material((0.0, 1.0, 0.0))
    cubeList.append(cube)

#display loop
while DISPLAY.loop_running() :
    #listen for keystrokes
    k = mykeys.read()
    if k == 27 : #ESC key
        mykeys.close()
        DISPLAY.destory()
        break

    CAM.update(mymouse, mykeys)

    for cube in cubeList:
        cube.draw()
