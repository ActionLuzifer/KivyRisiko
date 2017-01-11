#!/usr/bin/python3
# coding=utf-8
"""
Created on 2017-01-11

@author: ActionLuzifer
"""

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class KivyRisikoStatusBar(BoxLayout):

    def __init__(self, _kivyRisikoScreen, **kwargs):
        super(KivyRisikoStatusBar, self).__init__(**kwargs)
        self.kivyRisikoScreen = _kivyRisikoScreen
        self.btnRound = Button(text="Runde NaN")
        self.add_widget(self.btnRound)


    def updateStatusLabel(self, _round):
        self.btnRound.text = "Runde {}".format(_round)


