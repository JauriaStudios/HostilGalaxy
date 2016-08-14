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

    p_pos_x = 0
    p_pos_z = 0
    max_particles = 5
    life = 0
    p_life = 0
    particle_count = 0
    p = 0

    def __init__(self, game, start_posX, start_posY):

        self.game = game

        self.model = Actor(os.path.join("data", "rock"))
        self.model.setPos(start_posX, 0, start_posY)
        self.model.setScale(1)

        self.life = 5
        self.p_life = 30

        self.rock_collision = EntityCollision(self)

        self.model.reparentTo(render)

        self.game.taskMgr.add(self.update, "update_rock")

    def spawn_particles(self, pos_x, pos_z):

        if self.particle_count < self.max_particles:
            self.particle_count += 1
            self.p_pos_x = pos_x
            self.p_pos_z = pos_z

            self.p_life = 30

            self.p = ParticleEffect()
            self.p.loadConfig(Filename('data/particles/dust.ptf'))

            self.p.start(self.model)

            self.p.setPos(self.p_pos_x, 0.000, self.p_pos_z)

    def update(self, task):

        dt = globalClock.getDt()

        if self.model:

            if self.p:
                if self.p_life:

                    self.p_life -= 1

                    if self.p_life <= 0:
                        self.p.cleanup()

            self.model.setR(self.model, 10 * dt)
            self.model.setZ(self.model.getZ() - dt)

            if self.life <= 0:
                self.model.remove_node()

        return task.cont
