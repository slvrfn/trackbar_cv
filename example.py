import numpy as np
 
from trackbar import *

 
img = np.zeros((480,640,3))
midpoint = tuple(np.roll(np.array(img.shape[0:2])/2,1).astype(dtype=np.int))

def draw_image(point):
    new_image = np.copy(img)
    (x,y) = point
    cv2.line(new_image,(midpoint[0]+x,midpoint[1]+y),midpoint,[255,255,255])
    return new_image

def compute_values(rho,theta):
    x = int(np.cos(theta)*rho)
    y = int(np.sin(theta)*rho)
    return (x, y)

result = display_trackbar_window(
    'test',
    draw_image,
    compute_values,
    rho   = param(40,10,scale(10)),
    theta = param(90,0,lambda x: (x/90.*360.)*np.pi/180.))
