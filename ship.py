# -*- coding: utf-8 -*-
# Authors: TurBoss
# Models: TurBoss

# Ship
import os

from pid import PID

from panda3d.core import Vec3,Vec4,BitMask32, VBase4
from panda3d.core import TransformState
from panda3d.core import Point3, TransparencyAttrib,TextNode

from direct.actor.Actor import Actor

class Ship:
    def __init__(self):

        self.model = Actor("data/ship.egg")
        self.model.setPos(0, 0, 0)
        self.model.setHpr(0, 0, 0)


    def draw(self):
        self.model.reparentTo(render)
