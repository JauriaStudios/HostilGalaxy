# -*- coding: utf-8 -*-
# Authors: TurBoss
# Models: TurBoss

# Background
import os

from panda3d.core import TextureStage

class Background:
    def __init__(self, game):

        self.game = game

        self.texture = loader.loadTexture(os.path.join("data", "bg.png"))
        self.model = loader.loadModel(os.path.join("data", "bg.egg"))

        self.model.setHpr(0, 0, 0)
        self.model.setPos(0, 0, 0)
        self.model.setScale(1)

    def draw(self):
        self.model.reparentTo(self.game.camera)
        self.ts = TextureStage('ts')
        #self.model.setTexture(self.texture, 0)
        self.model.setTexture(self.ts, self.texture)

