row1 = []
row2 = []
with open("/workspaces/Advent2024/Day1/input.txt", "r") as file:
        for line in file:
            numbers = line.strip().split("   ")
            row1.append(numbers[0])
            row2.append(numbers[1])
def part1():
    total_distance = 0
    row1.sort()
    row2.sort()
    for i,num in enumerate(row1):
        distance = abs(int(num) - int(row2[i]))
        totalDistance += distance
    print(total_distance)
def part2():
    total_distance = 0
    times_seen = {}
    for i in row2:
        if i in times_seen:
            times_seen[i] += 1
        else:
            times_seen[i] = 1
    for i,num in enumerate(row1):
        total_distance += int(num) * times_seen.get(num, 0)
    print(total_distance)
part2()
