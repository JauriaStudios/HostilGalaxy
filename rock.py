# -*- coding: utf-8 -*-
# Authors: TurBoss
# Models: TurBoss

# Rock
import os

from direct.actor.Actor import Actor


class Rock:
    def __init__(self, game, startPos):

        self.game = game

        self.model = Actor(os.path.join("data", "rock"))
        self.model.setPos(0, 0, startPos)
        self.model.setScale(1)

        self.game.taskMgr.add(self.update, "update_rock")

    def update(self, task):

        dt = globalClock.getDt()

        self.model.setR(self.model, task.time * dt)

        return task.cont


    def draw(self):

        self.model.reparentTo(render)
