# -*- coding: utf-8 -*-
# Authors: TurBoss
# Models: TurBoss

# Ship
import os

from pid import PID

from direct.actor.Actor import Actor

class Ship:
    def __init__(self, game):

        self.game = game

        self.x_pid = PID(3.0, 0.4, 1.2)
        self.y_pid = PID(3.0, 0.4, 1.2)

        self.model = Actor("data/ship.egg")
        self.model.setPos(0, 0, 0)
        self.model.setHpr(0, 0, 0)


    def draw(self):
        self.model.reparentTo(render)

    def update(self, task):
        dt = globalClock.getDt()

        if self.game.mouseWatcherNode.hasMouse():
            mpos = self.game.mouseWatcherNode.getMouse()

            x = mpos.getX()
            y = mpos.getY()

            self.x_pid.setPoint(x)
            self.y_pid.setPoint(y)

            pid_x = self.x_pid.update(self.model.getX())
            pid_y = self.y_pid.update(self.model.getY())

            pid_x = min(6, pid_x)
            pid_x = max(-6, pid_x)

            pid_y = min(6, pid_y)
            pid_y = max(-6, pid_y)

            self.model.setPos(pid_x, 0, pid_y)

        return task.cont
