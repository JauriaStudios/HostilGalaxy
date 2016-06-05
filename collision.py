# -*- coding: utf-8 -*-
# Authors: TurBoss
# Models: TurBoss

# Collisions


from panda3d.core import CollisionNode, CollisionSphere, CollisionRay
from panda3d.core import CollisionHandlerQueue, CollisionTraverser
from panda3d.core import CollideMask, BitMask32

ENEMIES = BitMask32(0b1)
ALLIES = BitMask32(0b10)


class MouseCollision:
    def __init__(self, game):

        self.game = game

        self.c_trav = CollisionTraverser()

        self.mouse_groundHandler = CollisionHandlerQueue()
        self.mouse_ground_ray = CollisionRay()
        self.mouse_ground_col = CollisionNode('mouseRay')

        self.mouse_ground_ray.setOrigin(0, 0, 0)
        self.mouse_ground_ray.setDirection(0, -1, 0)

        self.mouse_ground_col.addSolid(self.mouse_ground_ray)
        self.mouse_ground_col.setFromCollideMask(CollideMask.bit(0))
        self.mouse_ground_col.setIntoCollideMask(CollideMask.allOff())

        self.mouse_ground_col_np = self.game.camera.attachNewNode(self.mouse_ground_col)

        self.c_trav.addCollider(self.mouse_ground_col_np, self.mouse_groundHandler)

        self.game.taskMgr.add(self.update, 'updateMouse')

    def update(self, task):

        if self.game.mouseWatcherNode.hasMouse():
            if self.game.ship.model:

                mouse_pos = self.game.mouseWatcherNode.getMouse()

                self.mouse_ground_ray.setFromLens(self.game.camNode, mouse_pos.getX(), mouse_pos.getY())

                near_point = render.getRelativePoint(self.game.camera, self.mouse_ground_ray.getOrigin())
                near_vec = render.getRelativeVector(self.game.camera, self.mouse_ground_ray.getDirection())

                self.game.ship.shipPoint.setPos(self.PointAtY(self.game.ship.model.getY(), near_point, near_vec))

        return task.cont

    def PointAtY(self, y, point, vec):
        return point + vec * ((y - point.getY()) / vec.getY())


class EntityCollision:
    def __init__(self, entity):

        self.entity = entity

        self.setup_collision()
        self.queue = CollisionHandlerQueue()
        self.traverser = CollisionTraverser('Collision Traverser')
        self.traverser.showCollisions(render)
        self.traverser.add_collider(self.target_nodepath, self.queue)
        base.taskMgr.add(self.collide, "Collision Task")

    def setup_collision(self):
        self.target = CollisionSphere(0, 0, 0, 1)
        self.target_node = CollisionNode('collision_entity')
        self.target_node.setFromCollideMask(ALLIES)  # unused
        self.target_node.setIntoCollideMask(ENEMIES)
        self.target_nodepath = self.entity.model.attach_new_node(self.target_node)
        self.target_nodepath.node().addSolid(self.target)
        self.target_nodepath.show()

    def collide(self, task):

        self.traverser.traverse(render)

        for entry in self.queue.get_entries():
            print("Entity:")
            print(entry)
            self.entity.spawn_particles(1)
            self.entity.life -= 1

        return task.cont


class ShipCollision:
    def __init__(self, ship):

        self.ship = ship

        self.setup_collision()
        self.queue = CollisionHandlerQueue()
        self.traverser = CollisionTraverser('Collision Traverser')
        self.traverser.showCollisions(render)
        self.traverser.add_collider(self.target_nodepath, self.queue)
        base.taskMgr.add(self.collide, "Collision Task")

    def setup_collision(self):

        self.target = CollisionSphere(0, 0, 0, 0.5)
        self.target_node = CollisionNode('collision_ship')
        self.target_node.setFromCollideMask(ENEMIES)
        self.target_node.setIntoCollideMask(ALLIES)
        self.target_nodepath = self.ship.model.attach_new_node(self.target_node)
        self.target_nodepath.node().addSolid(self.target)
        #self.target_nodepath.show()

    def collide(self, task):

        self.traverser.traverse(render)

        for entry in self.queue.get_entries():
            #print("Ship:")
            #print(entry)
            self.ship.model.cleanup()
            self.ship.model.removeNode()

        return task.cont


class BulletCollision:
    def __init__(self, bullet):

        self.bullet = bullet

        self.setup_collision()
        self.queue = CollisionHandlerQueue()
        self.traverser = CollisionTraverser('Collision Traverser')
        self.traverser.showCollisions(render)
        self.traverser.add_collider(self.target_nodepath, self.queue)
        base.taskMgr.add(self.collide, "Collision Task")

    def setup_collision(self):

        self.target = CollisionSphere(0, 0, 0, 0.1)
        self.target_node = CollisionNode('collision_bullet')
        self.target_node.setFromCollideMask(ENEMIES)
        self.target_node.setIntoCollideMask(ALLIES)

        self.target_nodepath = self.bullet.model.attach_new_node(self.target_node)
        self.target_nodepath.node().addSolid(self.target)
        self.target_nodepath.show()

    def collide(self, task):

        self.traverser.traverse(render)

        for entry in self.queue.get_entries():

            #print("Bullet:")
            #print(entry)
            self.bullet.model.removeNode()

        return task.cont
