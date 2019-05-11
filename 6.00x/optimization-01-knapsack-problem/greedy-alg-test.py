# python 3.6.6

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


def build_items():
    return [Item(n,v,w) for n,v,w in (('clock', 175, 10),
                                      ('painting', 90, 9),
                                      ('radio', 20, 4),
                                      ('vase', 50, 2),
                                      ('book', 10, 1),
                                      ('computer', 200, 20))]

# property
def metric_value(item):
    return item.get_value()

# property
def metric_weight(item):
    return 1.0/item.get_weight()

# property
# 100/10=10
# 50/5=10
# 100/5=20
def metric_worth(item):
    return item.get_value()/item.get_weight()

def greedy(items, max_weight, metric):
    knapsack = []
    total_weight = 0
    sorted_list = sorted(items, key=metric, reverse=True) #reverse=True == descending order

    for item in sorted_list:
        item_weight = item.get_weight()
        if total_weight + item_weight <= max_weight:
            knapsack.append(item)
            total_weight += item_weight
    return knapsack

def test_greedy(items, max_weight, metric):
    result = greedy(items, max_weight, metric)
    total_value = sum(map(Item.get_value, result))
    print("Total value: %s" % (str(total_value)))

    for i in result:
        print(i)


def test_all_metrics(items, max_weight):
    print("--- Metric = value, weight=%s" % (max_weight))
    test_greedy(items, max_weight, metric_value)
    print("--- Metric = weight, weight=%s" % (max_weight))
    test_greedy(items, max_weight, metric_weight)
    print("--- Metric = worth, weight=%s" % (max_weight))
    test_greedy(items, max_weight, metric_worth)

if __name__ == "__main__":
    #clock = Item("clock", 10, 2)
    #print(clock)

    items = build_items()
    test_all_metrics(items, 25)
    #sorted_list = sorted(items, key=metric_value, reverse=True)
    #sorted_list = sorted(items, key=metric_weight, reverse=True)
    #sorted_list = sorted(items, key=metric_worth, reverse=True)
    dbg = 1
