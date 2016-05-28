# -*- coding: utf-8 -*-
# Authors: TurBoss
# Models: TurBoss

# Ship

from direct.actor.Actor import Actor

class Ship:
    def __init__(self, game):

        self.game = game

        self.model = Actor("data/ship.egg")
        self.model.setPos(0, 50, 0)
        self.model.setHpr(0, 0, 0)


    def draw(self):
        self.model.reparentTo(render)

    def update(self, task):
        dt = globalClock.getDt()

        if self.game.mouseWatcherNode.hasMouse():
            mpos = self.game.mouseWatcherNode.getMouse()

            x = mpos.getX() * 20
            y = mpos.getY() * 20

            self.model.setPos(x, self.model.getY(), y)

        return task.cont
