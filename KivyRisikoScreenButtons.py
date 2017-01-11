#!/usr/bin/python3
# coding=utf-8
"""
Created on 2017-01-11

@author: ActionLuzifer
"""

from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class KivyRisikoScreenButtons(GridLayout):

    def __init__(self, _kivyRisikoScreen, **kwargs):
        super(KivyRisikoScreenButtons, self).__init__(**kwargs)
        self.kivyRisikoScreen = _kivyRisikoScreen

        self.cols = 4
        self.rows = 3
        btnBauen        = Button(text="Bauen")
        btnReparieren   = Button(text="Reparieren")
        btnBewegen      = Button(text="Bewegen")
        btnRekrutieren  = Button(text="Rekrutieren")
        btnRundeBeenden = Button(text="Runde beenden")
        btnRundeBeenden.bind(on_press=self.endRound)

        self.add_widget(btnBauen)
        self.add_widget(btnReparieren)
        self.add_widget(Button(text=""))
        self.add_widget(Button(text=""))

        self.add_widget(btnBewegen)
        self.add_widget(btnRekrutieren)
        self.add_widget(Button(text=""))
        self.add_widget(Button(text=""))

        self.add_widget(Button(text=""))
        self.add_widget(Button(text=""))
        self.add_widget(Button(text=""))
        self.add_widget(btnRundeBeenden)


    def endRound(self, _btn):
        self.kivyRisikoScreen.endRound()



