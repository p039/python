import subprocess
import sys
import time
import random

class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_weight(self):
        return self.weight

    def __str__(self):
        return "%s, %s, %s" % (self.name, str(self.value), str(self.weight))


if __name__ == "__main__":
    clock = Item("clock", 10, 2)
    print(clock)
