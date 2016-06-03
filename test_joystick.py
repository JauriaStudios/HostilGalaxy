# TODO:
# * Deal with hot plugging / unplugging of sticks
# * Can I get a unique ID for a model / instance of a stick?

import pyglet

from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from panda3d.core import Filename


class World(ShowBase):

    def __init__(self):

        ShowBase.__init__(self)

        self.j = Joypad()

        self.taskMgr.add(self.update, 'updateJoypad')

    def update(self, task):
        dt = globalClock.getDt()

        self.j.update()

        return task.cont


class Joypad:
    def __init__(self):
        pyglet.app.platform_event_loop.start()
        controller = Controller()
        joysticks = pyglet.input.get_joysticks()
        print("Found %s joysticks" % (len(joysticks), ))
        for joystick in joysticks:
            joystick.push_handlers(controller)
            joystick.open()

    def clean(self):
        for joystick in pyglet.input.get_joysticks():
            joystick.close()

    def update(self):
        pyglet.app.platform_event_loop.step(0.003)


class Controller:
    def on_joybutton_press(self, joystick, button):
        print(joystick, button)

    def on_joybutton_release(self, joystick, button):
        print(joystick, button)

    def on_joyaxis_motion(self, joystick, axis, value):
        print(joystick, axis, value)

    def on_joyhat_motion(self, joystick, hat_x, hat_y):
        print(joystick, hat_x, hat_y)


def main():

    props = WindowProperties( )

    props.setTitle('Hostil Galaxy')
    props.setCursorFilename(Filename.binaryFilename('cursor.ico'))
    props.setCursorHidden(False)
    props.setFullscreen(False)
    props.setSize(800, 600)

    game = World()

    game.win.setClearColor((1, 1, 1, 1))
    game.win.requestProperties(props)
    game.setFrameRateMeter(True)

    game.run()

if __name__ == "__main__": main()
