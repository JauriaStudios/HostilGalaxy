# -*- coding: utf-8 -*-
# Authors: TurBoss
# Models: TurBoss

# Ship

from pid import PID
from bullet import Bullet

from direct.actor.Actor import Actor

from panda3d.core import PandaNode, NodePath

class Ship:

    def __init__(self, game):

        self.game = game

        self.shipPoint = NodePath(PandaNode("shipFloaterPoint"))
        self.shipPoint.reparentTo(render)

        self.x_pos = 0
        self.z_pos = 0

        self.x_pid = PID(3.0, 5.0, 1.0)
        self.z_pid = PID(3.0, 5.0, 1.0)

        self.model = Actor("data/ship.egg")

        self.model.setPos(0, 0, 0)
        self.model.setHpr(0, 0, 0)

        self.normal_speed = 3.5
        self.low_speed = 2

        self.speed = self.normal_speed

        self.cool_down = 0.1
        self.last_shoot = 0

        self.keyMap = {

            "up": 0,
            "down": 0,
            "left": 0,
            "right": 0,

            "brake": 0,

            "attack": 0,
        }

        # This list will stored fired bullets.
        self.bullets = []

        self.game.accept("mouse1", self.setKey, ["attack", 1])
        self.game.accept("mouse1-up", self.setKey, ["attack", 0])

        self.game.accept("shift-mouse1", self.setKey, ["attack", 1])
        self.game.accept("shift-mouse1-up", self.setKey, ["attack", 0])

        self.game.accept("x", self.setKey, ["attack", 1])
        self.game.accept("x-up", self.setKey, ["attack", 0])

        self.game.accept("c", self.setKey, ["brake", 1])
        self.game.accept("c-up", self.setKey, ["brake", 0])

        self.game.accept("arrow_up", self.setKey, ["up", 1])
        self.game.accept("arrow_up-up", self.setKey, ["up", 0])

        self.game.accept("arrow_down", self.setKey, ["down", 1])
        self.game.accept("arrow_down-up", self.setKey, ["down", 0])

        self.game.accept("arrow_left", self.setKey, ["left", 1])
        self.game.accept("arrow_left-up", self.setKey, ["left", 0])

        self.game.accept("arrow_right", self.setKey, ["right", 1])
        self.game.accept("arrow_right-up", self.setKey, ["right", 0])

    def setKey(self, key, value):
        self.keyMap[key] = value

    def draw(self):
        self.model.reparentTo(render)

    def update(self, task):
        dt = globalClock.getDt()

        # Movement


        if self.game.ship_control_type == 0:
            if self.keyMap["brake"]:
                self.speed = self.low_speed
            else:
                self.speed = self.normal_speed


            if self.keyMap["up"]:
                self.model.setZ(self.model, self.speed * dt)

            elif self.keyMap["down"]:
                self.model.setZ(self.model, -self.speed * dt)

            if self.keyMap["left"]:
                self.model.setX(self.model, -self.speed * dt)

            elif self.keyMap["right"]:
                self.model.setX(self.model, self.speed * dt)

        elif self.game.ship_control_type == 1:

            self.x_pos = self.shipPoint.getX()
            self.z_pos = self.shipPoint.getZ()

            self.x_pid.setPoint(self.x_pos)
            self.z_pid.setPoint(self.z_pos)

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

        # Shoot

        if self.keyMap["attack"]:
            current_shoot_time = task.time
            if current_shoot_time - self.last_shoot >= self.cool_down:

                self.last_shoot = current_shoot_time

                self.bullet = Bullet(self)

        return task.cont
