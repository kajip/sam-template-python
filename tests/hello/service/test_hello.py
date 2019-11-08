# -*- encoding:utf-8 -*-

from service.hello import *


def test_greeting():
    expected = "Hello, {}"

    name = "ほげ"
    greeting = Greeting(name)

    assert greeting.greeting() == expected.format(name)
