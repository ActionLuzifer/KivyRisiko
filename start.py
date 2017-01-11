#!/usr/bin/python3
# coding=utf-8
"""
Created on 2016-12-27

@author: actionluzifer
"""


# Fix OpenGL 2.0 Bug
from kivy import Config
Config.set("graphics", "multisamples", '0')

from KivyRisikoApp import KivyRisikoApp



if __name__ == "__main__":
    KivyRisikoApp().run()