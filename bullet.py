# -*- coding: utf-8 -*-
# Authors: TurBoss
# Models: TurBoss

# Bullet

import os


class Bullet:

    def __init__(self, ship):

        self.ship = ship

        self.life = 30 * 5
        self.speed = 100

        # Creates a bullet and adds it to the bullet list
        pos = self.ship.model.getPos()
        self.model = loader.loadModel(os.path.join("data", "bullet.egg"))
        self.model.setPos(pos)
        self.model.setScale(0.1)
        # Velocity is in relation to the ship
        vel = (10)

        self.ship.bullets.append(self.model)

        self.model.reparentTo(render)

        self.ship.game.taskMgr.add(self.update, 'updateBullet')

    def update(self, task):
        dt = globalClock.getDt()

        self.life -= 1

        if self.life <= 0:
            self.model.removeNode()
        else:
            self.model.setZ(self.model, self.speed * dt)

        return task.cont