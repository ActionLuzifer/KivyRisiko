#!/usr/bin/python3
# coding=utf-8
"""
Created on 2016-12-27

@author: actionluzifer
"""


from kivy.app import App                   # Application
from kivy.uix.gridlayout import GridLayout # Layout
from kivy.uix.label import Label           # Labels (Buttons == Labels?)
from kivy.uix.button import Button         # Buttons

# Fix OpenGL 2.0 Bug
from kivy import Config
Config.set("graphics", "multisamples", '0')



class KivyRisikoScreen(GridLayout):

    def __init__(self, **kwargs):
        super(KivyRisikoScreen, self).__init__(**kwargs)
        self.cols = 1
        self.rows = 2
        risikoScreenMap = KivyRisikoScreenMap()
        risikoScreenButtons = KivyRisikoScreenButtons()
        self.add_widget(risikoScreenMap)
        self.add_widget(risikoScreenButtons)



class KivyRisikoScreenMap(GridLayout):

    def __init__(self, **kwargs):
        super(KivyRisikoScreenMap, self).__init__(**kwargs)
        self.cols = 16
        self.rows = 16
        for i in range(0, 256):
            self.add_widget(Button(text="{0:>3}".format(i)))


class KivyRisikoScreenButtons(GridLayout):

    def __init__(self, **kwargs):
        super(KivyRisikoScreenButtons, self).__init__(**kwargs)
        self.cols = 4
        self.rows = 3
        self.add_widget(Button(text="Bauen"))
        self.add_widget(Button(text="Reparieren"))
        self.add_widget(Button(text=""))
        self.add_widget(Button(text=""))

        self.add_widget(Button(text="Bewegen"))
        self.add_widget(Button(text="Rekrutieren"))
        self.add_widget(Button(text=""))
        self.add_widget(Button(text=""))

        self.add_widget(Button(text=""))
        self.add_widget(Button(text=""))
        self.add_widget(Button(text=""))
        self.add_widget(Button(text="Runde beenden"))



class KivyRisikoApp (App):

    def build(self):
        return KivyRisikoScreen()


if __name__ == "__main__":
    KivyRisikoApp().run()