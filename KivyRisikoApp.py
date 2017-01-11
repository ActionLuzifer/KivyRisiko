#!/usr/bin/python3
# coding=utf-8
"""
Created on 2017-01-11

@author: ActionLuzifer
"""
from kivy.app import App                   # Application

from KivyRisiko import KivyRisiko
from KivyRisikoScreen import KivyRisikoScreen


class KivyRisikoApp (App):

    def build(self):
        self.kivyRisikoScreen = KivyRisikoScreen(_app=self, orientation="vertical")
        self.game = KivyRisiko()
        self.resetGame()

        return self.kivyRisikoScreen

    def resetGame(self):
        self.game.resetGame()
        self.kivyRisikoScreen.updateStatusLabel(self.game.round)

    def endRound(self):
        self.game.nextRound()
        self.kivyRisikoScreen.updateStatusLabel(self.game.round)
