# -*- coding: utf-8 -*-
# Authors: TurBoss
# Models: TurBoss

# Collisions

from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import CollideMask
from panda3d.core import CollisionSphere


class Collision:
    def __init__(self, game):

        self.game = game

        self.cTrav = CollisionTraverser()

        self.init_mouse()

    def init_mouse(self):

        self.mouseGroundHandler = CollisionHandlerQueue()
        self.mouseGroundRay = CollisionRay()
        self.mouseGroundCol = CollisionNode('mouseRay')

        self.mouseGroundRay.setOrigin(0, 0, 0)
        self.mouseGroundRay.setDirection(0, -1, 0)

        self.mouseGroundCol.addSolid(self.mouseGroundRay)
        self.mouseGroundCol.setFromCollideMask(CollideMask.bit(0))
        self.mouseGroundCol.setIntoCollideMask(CollideMask.allOff())

        self.mouseGroundColNp = self.game.camera.attachNewNode(self.mouseGroundCol)

        self.cTrav.addCollider(self.mouseGroundColNp, self.mouseGroundHandler)

    def update(self, task):

        if self.game.mouseWatcherNode.hasMouse():

            mouse_pos = self.game.mouseWatcherNode.getMouse()

            self.mouseGroundRay.setFromLens(self.game.camNode, mouse_pos.getX(), mouse_pos.getY())

            near_point = render.getRelativePoint(self.game.camera, self.mouseGroundRay.getOrigin())
            near_vec = render.getRelativeVector(self.game.camera, self.mouseGroundRay.getDirection())

            self.game.ship.shipPoint.setPos(PointAtY(self.game.ship.model.getY(), near_point, near_vec))

        return task.cont

def PointAtY(y, point, vec):
    return point + vec * ((y - point.getY()) / vec.getY())