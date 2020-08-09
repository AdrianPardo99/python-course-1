#!/usr/bin/env python3

class First(object):
    def __init__(self, arg1=""):
        self.arg1 = arg1

objFirst=First("Hola desde el argumento 1")
print(objFirst.arg1)
objFirst.arg1="Hey"
print(objFirst.arg1)
