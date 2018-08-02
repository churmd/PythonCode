import pi3d
from numpy import sin, cos, radians

class RotatingCamera:
    def __init__(self, CAMRAD, mouse):
        self.CAMERA = pi3d.Camera()
        #radius of camera position
        self.CAMRAD = CAMRAD
        #rotation of camera
        self.mouseRot = 0.0
        #tilt of camera
        self.tilt = 15.0
        self.frame = 0
        #"old" mouse positions
        self.omx, self.omy = mouse.position()

    def update(self, mouse):
        #"new" mouse position
        mx, my = mouse.position()
        self.mouseRot -= (mx - self.omx) * 0.2
        self.tilt -= (my - self.omy) * 0.1
        #"new" mouse position becomes the "old" one
        self.omx = mx
        self.omy = my
        #need to reset camera first
        self.CAMERA.reset()
        self.CAMERA.rotate(-self.tilt, self.mouseRot, 0)
        #self.CAMERA.position((self.CAMRAD * sin(radians(self.mouseRot)) * cos(radians(self.tilt))), (self.CAMRAD * sin(radians(self.tilt))), (self.CAMRAD * cos(radians(self.mouseRot)) * cos(radians(self.tilt))))
