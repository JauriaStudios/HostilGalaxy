# -*- coding: utf-8 -*-
# Authors: TurBoss
# Models: TurBoss

# Rock
import os

from direct.actor.Actor import Actor


class Rock:
    def __init__(self, startPos):

        self.model = Actor(os.path.join("data", "rock"))
        self.model.setPos(0, 0, startPos)
        self.model.setScale(1)

    def draw(self):
        self.model.reparentTo(render)
