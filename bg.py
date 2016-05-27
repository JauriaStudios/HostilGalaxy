# -*- coding: utf-8 -*-
# Authors: TurBoss
# Models: TurBoss

# Background
import os


class Background:
    def __init__(self):

        self.model = loader.loadModel(os.path.join("data", "bg"))
        size = self.get_size()

        self.model.setHpr(0, 0, 0)
        self.model.setPos(0, 5, size[2]/2)
        self.model.setScale(1)

    def draw(self):
        self.model.reparentTo(render)

    def get_size(self):
        min, max = self.model.getTightBounds()
        size = max - min
        return size
