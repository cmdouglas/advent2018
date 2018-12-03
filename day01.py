def part1():
    with open('day01.txt') as f:
        total = 0
        for line in f:
            total += int(line.strip())
        
        print(total)
        
def part2():
    found = set()
    with open('day01.txt') as f:
        changes = [int(change.strip()) for change in f.readlines()]
        current = 0
        found.add(current)
        while True:
            for change in changes:
                current += change
                if current in found:
                    print(current)
                    return;
                found.add(current)


if __name__ == '__main__':
    part1()
    part2()