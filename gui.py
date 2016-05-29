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

        self.frame = DirectFrame()
        self.frame['frameColor'] = (0.8, 0.8, 0.8, 0)
        self.frame['image'] = os.path.join("data", "startMenu.png")
        self.frame['image_scale'] = (1.0, 1.0, 1.0)
        self.frame.setPos(0, 0, 0)

        self.frame.setTransparency(TransparencyAttrib.MAlpha)

        self.accept("escape", sys.exit)

    def show(self):
        self.frame.show()

    def hide(self):
        self.frame.hide()

    def doStartGame(self):

        self.frame.hide()
        self.game.setup()

    def endGame(self):
        sys.exit()