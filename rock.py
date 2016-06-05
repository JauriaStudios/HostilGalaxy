# -*- coding: utf-8 -*-
# Authors: TurBoss
# Models: TurBoss

# Rock
import os

from direct.actor.Actor import Actor

from panda3d.core import Filename

from panda3d.physics import BaseParticleEmitter, BaseParticleRenderer
from panda3d.physics import PointParticleFactory, SpriteParticleRenderer
from panda3d.physics import LinearNoiseForce, DiscEmitter
from direct.particles.Particles import Particles
from direct.particles.ParticleEffect import ParticleEffect
from direct.particles.ForceGroup import ForceGroup

from collision import EntityCollision


class Rock:
    def __init__(self, game, start_posX, start_posY):

        self.game = game

        self.model = Actor(os.path.join("data", "rock"))
        self.model.setPos(start_posX, 0, start_posY)
        self.model.setScale(1)

        self.life = 5

        self.p_pos = 0
        self.p_life = 0

        self.rock_collision = EntityCollision(self)

        self.model.reparentTo(render)

        self.game.taskMgr.add(self.update, "update_rock")

    def spawn_particles(self, pos):

        self.p_pos = pos

        self.p_life = 30

        self.p = ParticleEffect()
        self.p.loadConfig(Filename('data/particles/fireish.ptf'))

        self.p.start(self.model)

        self.p.setPos(1.000, 0.000, 1.000)

    def update(self, task):

        dt = globalClock.getDt()

        if self.model:

            if self.p_life:

                self.p_life -= 1

                if self.p_life <= 0:
                    self.p.cleanup()


            self.model.setR(self.model, 10 * dt)
            self.model.setZ(self.model.getZ() - dt*2)

            if self.life <= 0:
                self.model.remove_node()

        return task.cont
