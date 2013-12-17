
class Person(object):

    def __init__(self, name, paid):
        self.name = str(name)
        self.paid = float(paid)
        self.debt = 0.0
        self.perperson = 0.0


def getAverage(obj_persons):
    total = sum(p.paid for p in obj_persons)
    return total/len(obj_persons)


def setDebt(obj_persons):
    avg = getAverage(obj_persons)    
    for p in obj_persons:
        p.debt = round(avg - p.paid, 2)


def setPerPerson(obj_persons):
    for p in obj_persons:
        if p.paid > 0.0:
            per_person = round(p.paid / len(obj_persons), 2)
            p.perperson = per_person
            

def balance(obj_persons):
    for p in obj_persons:
        print
        for i in obj_persons:
            if p.name != i.name:
                val = p.perperson - i.perperson
                if val > 0.0:
                    print i.name + ' -> ' + p.name + ': ' + str(val)

    print 'One person pays: ' + str(round(getAverage(obj_persons), 2)) + 'EUR'

    
def build_persons():
    return [Person(name,paid) for name,paid in (('Pv', 224.1),
                                                 ('St', 175.25),
                                                 ('Fl', 30.2),
                                                 ('Mo', 0.0),
                                                 ('Pn', 20.31))]


if __name__ == '__main__':

    persons = build_persons()
    setDebt(persons)
    setPerPerson(persons)
    balance(persons) 





