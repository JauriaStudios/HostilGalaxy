# -*- coding: utf-8 -*-
# Authors: TurBoss
# Models: TurBoss

# GUI

import os, sys

from panda3d.core import AntialiasAttrib, TransparencyAttrib

from direct.showbase import DirectObject

from direct.gui.DirectGui import *


class StartMenu(DirectObject.DirectObject):

    def __init__(self, game):

        self.game = game

        self.active_button = 0

        self.frame = DirectFrame()
        self.frame['frameColor'] = (0.8, 0.8, 0.8, 0)
        self.frame['image'] = "data/startMenu.png"
        self.frame['image_scale'] = (1.0, 1.0, 1.0)
        self.frame.setPos(0, 0, 0)

        self.frame.setTransparency(TransparencyAttrib.MAlpha)

        self.maps_start = loader.loadModel("data/start_menu/buttons_start_maps")
        self.start_button = DirectButton(
            parent=self.frame,
            pos=(0, 0, 0),
            image=(
                self.maps_start.find('**/startready'),
                self.maps_start.find('**/startclicked'),
                self.maps_start.find('**/startrollover'),
                self.maps_start.find('**/startdisable')
            ),
            command=self.start_game,
            scale=0.2,
            borderWidth=(0.01, 0.01),
            frameSize=(-0.55, 0.55, -0.2, 0.2),
            frameColor=(0.8, 0.8, 0.8, 0)
        )
        # rolloverSound=self.soundManager.over,
        # clickSound=self.soundManager.click))

        self.maps_credits = loader.loadModel("data/start_menu/buttons_credits_maps.egg")
        self.credits_button = DirectButton(
            parent=self.frame,
            pos=(0, 0, -0.1),
            image=(
                self.maps_credits.find('**/creditsready'),
                self.maps_credits.find('**/creditsclicked'),
                self.maps_credits.find('**/creditsrollover'),
                self.maps_credits.find('**/creditsdisable')
            ),
            command=self.hide,
            scale=0.2,
            borderWidth=(0.01, 0.01),
            frameSize=(-0.55, 0.55, -0.2, 0.2),
            frameColor=(0.8, 0.8, 0.8, 0)
        )
        # rolloverSound=self.soundManager.over,
        # clickSound=self.soundManager.click))


        self.maps_quit = loader.loadModel("data/start_menu/buttons_quit_maps.egg")
        self.quit_button = DirectButton(
            parent=self.frame,
            pos=(0, 0, -0.2),
            image=(
                self.maps_quit.find('**/quitready'),
                self.maps_quit.find('**/quitclicked'),
                self.maps_quit.find('**/quitrollover'),
                self.maps_quit.find('**/quitdisable')
            ),
            command=self.end_game,
            scale=0.2,
            borderWidth=(0.01, 0.01),
            frameSize=(-0.55, 0.55, -0.2, 0.2),
            frameColor=(0.8, 0.8, 0.8, 0)
        )
        # rolloverSound=self.soundManager.over,
        # clickSound=self.soundManager.click))

        self.accept("escape", self.end_game)
        self.accept("arrow_up", self.up)
        self.accept("arrow_down", self.down)

    def show(self):
        self.frame.show()

    def hide(self):
        self.frame.hide()

    def start_game(self):

        self.frame.hide()
        self.game.setup()

    def end_game(self):
        sys.exit(0)

    def up(self):
        if self.active_button == 0:
            self.active_button = 2
            self.start_button['state'] = DGG.BUTTON_ROLLOVER_STATE
            self.start_button.setState()
        elif self.active_button == 1:
            self.active_button = 0
        elif self.active_button == 2:
            self.active_button = 1

        print(self.active_button)

    def down(self):
        if self.active_button == 0:
            self.active_button = 1
            self.start_button.setState()
        elif self.active_button == 1:
            self.active_button = 2
        elif self.active_button == 2:
            self.active_button = 0

        print(self.active_button)
