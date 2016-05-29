# -*- coding: utf-8 -*-
# Authors: TurBoss
# Models: TurBoss

# Ship

from pid import PID
from bullet import Bullet

from direct.actor.Actor import Actor

class Ship:
    def __init__(self, game):

        self.game = game

        self.x_pid = PID(3.0, 5.0, 1.0)
        self.z_pid = PID(3.0, 5.0, 1.0)

        self.model = Actor("data/ship.egg")

        self.model.setPos(0, 30, 0)
        self.model.setHpr(0, 0, 0)

        self.cool_down = 0.1
        self.last_shoot = 0

        self.keyMap = {
            "attack": 0,
        }

        # This list will stored fired bullets.
        self.bullets = []

        self.game.accept("mouse1", self.setKey, ["attack", 1])
        self.game.accept("mouse1-up", self.setKey, ["attack", 0])

        self.game.accept("shift-mouse1", self.setKey, ["attack", 1])
        self.game.accept("shift-mouse1-up", self.setKey, ["attack", 0])

    def setKey(self, key, value):
        self.keyMap[key] = value

    def draw(self):
        self.model.reparentTo(render)

    def update(self, task):
        dt = globalClock.getDt()

        # Movement
        if self.game.mouseWatcherNode.hasMouse():
            mpos = self.game.mouseWatcherNode.getMouse()

            x = mpos.getX() * 20
            z = mpos.getY() * 20

            self.x_pid.setPoint(x)
            self.z_pid.setPoint(z)

            pid_x = self.x_pid.update(self.model.getX())
            pid_z = self.z_pid.update(self.model.getZ())

            self.vx = pid_x
            self.vz = pid_z

            self.vx = min(10, self.vx)
            self.vx = max(-10, self.vx)

            self.vz = min(10, self.vz)
            self.vz = max(-10, self.vz)

            self.model.setX(self.model, self.vx * dt)
            self.model.setZ(self.model, self.vz * dt)

            #self.model.setH(self.vx * dt)

            print(self.vx * dt)


        # Shoot

        if self.keyMap["attack"]:
            current_shoot_time = task.time
            if current_shoot_time - self.last_shoot >= self.cool_down:

                self.last_shoot = current_shoot_time

                self.bullet = Bullet(self)

        return task.cont
