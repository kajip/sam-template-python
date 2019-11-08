# -*- encoding:utf-8 -*-

import os
import sys

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
ROOT_DIRECTORY = CURRENT_DIRECTORY + "/../"

# Lambda Functionのルートディレクトリ名を記述
functions = [
    "hello",
]

# モジュールを走査するrootディレクトリにLambda Functionのルートディレクトリを追加
for function in functions:
    sys.path.append(ROOT_DIRECTORY + function)
