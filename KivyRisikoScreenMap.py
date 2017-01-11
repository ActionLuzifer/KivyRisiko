#!/usr/bin/python3
# coding=utf-8
"""
Created on 2017-01-11

@author: ActionLuzifer
"""

from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class KivyRisikoScreenMap(GridLayout):

    def __init__(self, _kivyRisikoScreen, **kwargs):
        super(KivyRisikoScreenMap, self).__init__(**kwargs)
        self.kivyRisikoScreen = _kivyRisikoScreen
        self.cols = 16
        self.rows = 16
        for i in range(0, 256):
            self.add_widget(Button(text="{0:>3}".format(i)))
