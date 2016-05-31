# -*- coding: utf-8 -*-
# Authors: TurBoss
# Models: TurBoss

# Collisions

from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import CollideMask


class Collision:
    def __init__(self, game):

        self.game = game

        self.cTrav = CollisionTraverser()

        self.mouseGroundRay = CollisionRay()
        self.mouseGroundRay.setOrigin(0, 5, 0)
        self.mouseGroundRay.setDirection(0, -1, 0)
        self.mouseGroundCol = CollisionNode('mouseRay')
        self.mouseGroundCol.addSolid(self.mouseGroundRay)
        self.mouseGroundCol.setFromCollideMask(CollideMask.bit(0))
        self.mouseGroundCol.setIntoCollideMask(CollideMask.allOff())
        self.mouseGroundColNp = self.game.camera.attachNewNode(self.mouseGroundCol)
        self.mouseGroundHandler = CollisionHandlerQueue()
        self.cTrav.addCollider(self.mouseGroundColNp, self.mouseGroundHandler)


        # Uncomment this line to see the collision rays
        self.mouseGroundColNp.show()

        # Uncomment this line to show a visual representation of the
        # collisions occuring
        self.cTrav.showCollisions(render)

    def update(self, task):

        if self.game.mouseWatcherNode.hasMouse():

            mpos = self.game.mouseWatcherNode.getMouse()

            self.mouseGroundRay.setFromLens(self.game.camNode, mpos.getX(), mpos.getY())

            nearPoint = render.getRelativePoint(self.game.camera, self.mouseGroundRay.getOrigin())
            nearVec = render.getRelativeVector(self.game.camera, self.mouseGroundRay.getDirection())

            self.game.ship.shipPoint.setPos(PointAtY(self.game.ship.model.getY(), nearPoint, nearVec))

        return task.cont


def PointAtY(y, point, vec):
    return point + vec * ((y - point.getY()) / vec.getY())