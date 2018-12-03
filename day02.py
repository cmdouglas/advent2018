from collections import Counter
from itertools import combinations

def checksum(ids):
    threes = 0
    twos = 0
    
    for id_ in ids:
        c = Counter(id_)
        if 2 in c.values():
            twos += 1
        if 3 in c.values():
            threes += 1
    
    return twos * threes
    
def difference(id1, id2):
    return len([(c1, c2) for (c1, c2) in zip(id1, id2) if c1 != c2])
    
def common_chars(id1, id2):
    return "".join([c1 for c1, c2 in zip(id1, id2) if c1 == c2])

def part1():
    with open('day02.txt') as f:
        ids = [id_.strip() for id_ in f.readlines()]
        print(checksum(ids))
        
def part2():
    with open('day02.txt') as f:
        ids = [id_.strip() for id_ in f.readlines()]
        for id1, id2 in combinations(ids, 2):
            if difference(id1, id2) == 1:
                print(common_chars(id1, id2))
        

if __name__ == '__main__':
    part1()
    part2()