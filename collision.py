# -*- coding: utf-8 -*-
# Authors: TurBoss
# Models: TurBoss

# Collisions


from panda3d.core import CollisionNode, CollisionSphere, CollisionRay
from panda3d.core import CollisionHandlerQueue, CollisionTraverser
from panda3d.core import CollideMask

class MouseCollision:
    def __init__(self, game):

        self.game = game

        self.cTrav = CollisionTraverser()

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

        self.game.taskMgr.add(self.update, 'updateMouse')

    def update(self, task):

        if self.game.mouseWatcherNode.hasMouse():

            mouse_pos = self.game.mouseWatcherNode.getMouse()

            self.mouseGroundRay.setFromLens(self.game.camNode, mouse_pos.getX(), mouse_pos.getY())

            near_point = render.getRelativePoint(self.game.camera, self.mouseGroundRay.getOrigin())
            near_vec = render.getRelativeVector(self.game.camera, self.mouseGroundRay.getDirection())

            self.game.ship.shipPoint.setPos(self.PointAtY(self.game.ship.model.getY(), near_point, near_vec))

        return task.cont

    def PointAtY(self, y, point, vec):
        return point + vec * ((y - point.getY()) / vec.getY())


class EntityCollision:
    def __init__(self, entity):

        # Target; a sphere. You should attach it to your actual model,
        # not .show() it directly. Also, the sphere you see is a low-
        # poly model, but the collisions will be calculated against a
        # mathematically perfect sphere.
        self.target = CollisionSphere(0, 0, 0, 1)
        self.target_nodepath = entity.model.attach_new_node(CollisionNode('collision_target'))
        self.target_nodepath.node().addSolid(self.target)
        #self.target_nodepath.show()


class ShipCollision:
    def __init__(self, game):

        self.game = game

        self.setup_collision() #  Now we have self.hitter_nodepath
        self.queue = CollisionHandlerQueue()
        self.traverser = CollisionTraverser('Collision Traverser')
        self.traverser.showCollisions(render)
        self.traverser.add_collider(self.target_nodepath, self.queue)
        self.game.taskMgr.add(self.collide, "Collision Task")

    def setup_collision(self):
        # Hitter. Do note that not every combination of object works,
        # there is a table for that in the manual.

        self.target = CollisionSphere(0, 0, 0, 1)
        self.target_nodepath = self.game.ship.model.attach_new_node(CollisionNode('collision_target'))
        self.target_nodepath.node().addSolid(self.target)
        self.target_nodepath.show()

    def collide(self, task):
        self.traverser.traverse(render)
        for entry in self.queue.get_entries():
            print(entry)
        return task.cont