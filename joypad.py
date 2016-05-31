# -*- coding: utf-8 -*-
# Authors: TurBoss
# Models: TurBoss

# Joystick

import pyglet


class Joypad:
    def __init__(self):

        print("-- init Joystick")
        pyglet.app.platform_event_loop.start()

        self.controller = Controller()

        self.joysticks = pyglet.input.get_joysticks()
        if self.joysticks:

            for i in range(0,len(self.joysticks)):

                print("--- found joystick nº%s" % i)

                self.joystick = self.joysticks[i]

                self.joystick.push_handlers(self.controller)
                self.joystick.open()
        else:

            print("--- no joystick(s) found")

    def clean(self):

        if self.joysticks:

            for i in range(0, len(self.joysticks)):

                print("--- close joystick nº %s" % i)

                self.joystick = self.joysticks[i]
                self.joystick.close()

    def update(self, task):

        pyglet.app.platform_event_loop.step(0.003)

        return task.cont


class Controller:

    def on_joybutton_press(self, joystick, button):
        print(joystick, button)

    def on_joybutton_release(self, joystick, button):
        print(joystick, button)

    def on_joyaxis_motion(self, joystick, axis, value):
        print(joystick, axis, value)

    def on_joyhat_motion(self, joystick, hat_x, hat_y):
        print(joystick, hat_x, hat_y)