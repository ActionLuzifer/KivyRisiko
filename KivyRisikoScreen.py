#!/usr/bin/python3
# coding=utf-8
"""
Created on 2017-01-11

@author: ActionLuzifer
"""

from kivy.uix.boxlayout import BoxLayout
from KivyRisikoScreenMap import KivyRisikoScreenMap
from KivyRisikoScreenButtons import KivyRisikoScreenButtons
from KivyRisikoStatusBar import KivyRisikoStatusBar


class KivyRisikoScreen(BoxLayout):

    def __init__(self, _app, **kwargs):
        super(KivyRisikoScreen, self).__init__(**kwargs)
        self.app = _app
        self.kivyRisikoScreenUp  = BoxLayout(size_hint=(1, 0.7), orientation="vertical")
        self.kivyRisikoStatusBar = KivyRisikoStatusBar(self, size_hint=(1, 0.1))
        self.kivyRisikoScreenLow = BoxLayout(size_hint=(1, 0.2), orientation="vertical")
        self.add_widget(self.kivyRisikoScreenUp)
        self.add_widget(self.kivyRisikoStatusBar)
        self.add_widget(self.kivyRisikoScreenLow)
        risikoScreenMap     = KivyRisikoScreenMap(self)
        risikoScreenButtons = KivyRisikoScreenButtons(self)

        self.kivyRisikoScreenUp.add_widget(risikoScreenMap)
        self.kivyRisikoScreenLow.add_widget(risikoScreenButtons)


    def endRound(self):
        self.app.endRound()


    def updateStatusLabel(self, _round):
        self.kivyRisikoStatusBar.updateStatusLabel(_round)