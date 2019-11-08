# -*- encoding:utf-8 -*-

import json
from service.hello import Greeting


def handler(event, context):
    """HelloFunction"""
    greeting = Greeting(event["name"])
    print(greeting.greeting())
