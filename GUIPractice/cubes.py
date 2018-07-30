#!/usr/bin/env python3

import pi3d

"""Practice using the pi3d library, following demo
    https://www.youtube.com/watch?v=_jdYhRDygAM."""

#create display
DISPLAY = pi3d.Display.create()

#create camera
CAM = pi3d.Camera(eye = (0.0,0.0,-5.0))

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

    for cube in cubeList:
        cube.draw()
