# -*- encoding:utf-8 -*-


class Greeting:
    def __init__(self, name):
        self._name = name

    def greeting(self):
        return "Hello, " + self._name
