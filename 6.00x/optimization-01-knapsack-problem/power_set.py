# python 3.6.6

# 0 0 0 ------> no elements selected (0)
# 0 0 1 ------> only "c" element has been selected (1)
# 0 1 0 ------> only "b" element has been selected (2)
# 0 1 1 ------> only "b" and "c" element has been selected (3)
# 1 0 0 ------> similarly (4)
# 1 0 1 ------> (5)
# 1 1 0 ------> (6)
# 1 1 1 ------> (7)

def power_set(items):
    N = len(items) # 3 items
    combo = []
    for i in range(2**N):  # create all combinations count => 8
        temp_combo = []

        # 2 1 0 - index j
        # 0 0 0 - binary representation
        for j in range(N):

            # iterate by index over binary number, from right-> left. ex: 001 - take 1, then 0, then 0.
            # to understand if it's 1 or 0 used modulo operator %.
            # 0 % 2 = 0
            # 1 % 2 = 1
            if(i >> j) % 2 == 1:
                temp_combo.append(items[j])
        if temp_combo:
            combo.append(temp_combo)
    return combo
# Output:
# 0:['a']
# 1:['b']
# 2:['a', 'b']
# 3:['c']
# 4:['a', 'c']
# 5:['b', 'c']
# 6:['a', 'b', 'c']

if __name__ == '__main__':
    items = ['a','b','c']
    power_set = power_set(items)







    
