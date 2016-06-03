# -*- coding: utf-8 -*-
# Authors: TurBoss
# Models: TurBoss

# Rock
import os

from direct.actor.Actor import Actor

from collision import EntityCollision


class Rock:
    def __init__(self, game, start_posX, start_posY):

        self.game = game

        self.model = Actor(os.path.join("data", "rock"))
        self.model.setPos(start_posX, 0, start_posY)
        self.model.setScale(1)



        self.rock_collision = EntityCollision(self)

        self.model.reparentTo(render)

        self.game.taskMgr.add(self.update, "update_rock")


    def update(self, task):

        dt = globalClock.getDt()

        self.model.setR(self.model, 10 * dt)
        self.model.setZ(self.model.getZ() - dt*2)

        return task.cont
