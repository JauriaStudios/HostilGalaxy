# -*- coding: utf-8 -*-
# Authors: TurBoss
# Models: TurBoss

# Ship

from pid import PID

from direct.actor.Actor import Actor

class Ship:
    def __init__(self, game):

        self.game = game

        self.x_pid = PID(3.0, 0.5, 1.0)
        self.y_pid = PID(3.0, 0.5, 1.0)

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

            print(x, y)

            self.x_pid.setPoint(x)

            pid_x = self.x_pid.update(self.model.getX())

            pid_x = min(1, pid_x)
            pid_x = max(-1, pid_x)

            self.y_pid.setPoint(y)

            pid_y = self.y_pid.update(self.model.getY())

            pid_y = min(1, pid_y)
            pid_y = max(-1, pid_y)

            self.model.setPos(pid_x, 0, pid_y)

        return task.cont
