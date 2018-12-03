import re
from collections import Counter, defaultdict

def parse_line(line):
    pattern = re.compile(r'#([\d]+) @ ([\d]+),([\d]+): ([\d]+)x([\d]+)')
    m = re.match(pattern, line)
    return tuple([int(g) for g in m.groups()])
    

def points(x, y, width, height):
    for x_ in range(x, x+width):
        for y_ in range(y, y+height):
            yield (x_, y_)
            
def part1():
    point_counter = Counter()
    with open('day03.txt') as f:
        for line in f:
            id_, x, y, width, height = parse_line(line.strip())
            point_counter.update(list(points(x, y, width, height)))
        
        print(len([v for v in point_counter.values() if v > 1]))

def part2():
    point_annotator = defaultdict(list)
    ids = set()
    with open('day03.txt') as f:
        for line in f:
            id_, x, y, width, height = parse_line(line.strip())
            ids.add(id_)
            for point in points(x, y, width, height):
                point_annotator[point].append(id_)
        
        eliminated = set()
        for v in point_annotator.values():
            if len(v) > 1:
                eliminated.update(v)
        print((list(ids - eliminated))[0])

if __name__ == '__main__':
    part1()
    part2()