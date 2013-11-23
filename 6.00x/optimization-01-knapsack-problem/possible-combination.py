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


def powerSet(items):
    N = len(items)
    for i in xrange(2**N):
        combo = []
        for j in xrange(N):
            if(i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


def testPowerSet(pset, maxWeight):
    bestSet = None
    bestVal = 0.0
    for set in pset:
        bVal = sum(map(Item.getValue, set))
        weight = sum(map(Item.getWeight, set))
        if weight <= maxWeight and bVal > bestVal:
            bestSet = set
            bestVal = bVal

    return (bestSet, bestVal)


def simPowerSet():
    items = buildItems()
    maxWeight = 25
    pset = powerSet(items)
    objSet, objVal = testPowerSet(pset, maxWeight)
    print 'Total value: ', objVal

    for item in objSet:
        print ' ', item
    

if __name__ == '__main__':
    simPowerSet()
    




















    
