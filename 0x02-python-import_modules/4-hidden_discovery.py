#!/usr/bin/python3
import imp
import sys

module_name = 'hidden_4'
module = imp.load_compiled(module_name, module_name + '.pyc')

names = dir(module)

names = [name for name in names if not name.startswith('__')]

names.sort()

for name in names:
    print(name)
