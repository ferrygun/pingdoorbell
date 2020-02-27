from pymouse import PyMouse
from time import sleep
from gi.repository import Gdk
import sys

def PixelAt(x, y):
  w = Gdk.get_default_root_window()
  pb = Gdk.pixbuf_get_from_window(w, x, y, 1, 1)
  x = int.from_bytes(pb.get_pixels(), "big")    
  return x

m = PyMouse()
while True:
    print(m.position())
    print(PixelAt(int(m.position()[0]), int(m.position()[1])))
    #print(PixelAt(429, 447))
    sleep(0.5)
