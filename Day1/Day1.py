def part1():
    row1 = []
    row2 = []
    totalDistance = 0
    with open('Advent2024\Day1\input.txt', 'r') as file:
        for line in file:
            numbers = line.strip().split("   ")
            row1.append(numbers[0])
            row2.append(numbers[1])
    for i in range(len(row1)):
        minRow1 = min(row1)
        minRow2 = min(row2)
        distance = abs(int(minRow1) - int(minRow2))
        row1.pop(row1.index(minRow1))
        row2.pop(row2.index(minRow2))
        totalDistance += distance
    print(totalDistance)
def part2():
    row1 = []
    row2 = []
    totalDistance = 0
    seen = 0
    multiple = 0
    with open('Advent2024\Day1\input.txt', 'r') as file:
        for line in file:
            numbers = line.strip().split("   ")
            row1.append(numbers[0])
            row2.append(numbers[1])
    for i in row1:
        seen = i
        for j in row2:
            if seen == j:
                multiple += 1
        distance = int(seen) * multiple
        multiple = 0
        totalDistance += distance
    print(totalDistance)
part1()
part2()