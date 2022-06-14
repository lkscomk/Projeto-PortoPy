# !/usr/bin/python3
from tkinter import *
import json
from tkinter import Toplevel, Text
from tkinter import *
from idlelib.idle_test.test_colorizer import source
from idlelib.percolator import Percolator
from colorizer import *

parent = Tk()

text = Text(parent, background="white")
text.pack(expand=1, fill="both")
text.focus_set()

color_config(text)
p = Percolator(text)
d = ColorDelegator()
p.insertfilter(d)

parent.mainloop()
