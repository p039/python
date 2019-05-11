# python 3.6.6

class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.weight = float(w)
        self.value = float(v)

    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight

    def getValue(self):
        return self.value

    def __str__(self):
        return '<' + self.name + ', ' + str(self.value) + ', '\
                     + str(self.weight) + '>'


def buildItems():
    return [Item(n,v,w) for n,v,w in (('clock', 175, 10),
                                      ('painting', 90, 9),
                                      ('radio', 20, 4),
                                      ('vase', 50, 2),
                                      ('book', 10, 1),
                                      ('computer', 200, 20))]

def value(item):
    return item.getValue()

def weight(item):
    return 1.0/item.getWeight()

def density(item):
    return item.getValue()/item.getWeight()

def greedy(items, maxWeight, metric):
    knapsack = []
    totalWeight = 0
    for item in sorted(items, key=metric, reverse=True): #reverse=True == descending order
        w = item.getWeight()
        if w + totalWeight <= maxWeight:
            knapsack.append(item)
            totalWeight += w 
    return knapsack

def testGreedy(items, maxWeight, metric):
    g = greedy(items, maxWeight, metric)
    value = sum(map(Item.getValue, g))
    print("Total: %s" % (str(value)))
    for i in g:
        print(i)

def testGreedys(items, maxWeight = 20):
    #print 'Metric - value, weight - ', maxWeight
    testGreedy(items, maxWeight, value)
    #print 'Metric - weight, weight - ', maxWeight
    testGreedy(items, maxWeight, weight)
    #print 'Metric - density, weight - ', maxWeight
    testGreedy(items, maxWeight, density)


if __name__ == '__main__':
    items = buildItems()
    #testGreedy(items, 20, value)
    testGreedys(items)
    




















    
