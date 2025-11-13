with open("/workspaces/Advent2024/Day2/input.txt", "r") as file:
        lines = file.readlines()
def part1():
    count = 0
    for line in lines:
        levels = line.split()
        check = 0
        if int(levels[0]) == int(levels[1]):
            continue
        if int(levels[0]) < int(levels[1]):
            check = 1
        if int(levels[0]) > int(levels[1]):
            check = 2
        for i,number in enumerate(levels):
            if i == len(levels)-1:
                count+=1
                break
            if check == 1 and int(number) >= int(levels[i+1]):
                break
            if check == 2 and int(number) <= int(levels[i+1]):
                break
            if abs(int(number)-int(levels[i+1])) > 3:
                break
    print(count)

def part2():
    count = 0
    for line in lines:
        levels = line.split()
        check = 0
        safe = False
        for j in range(len(levels)):
            test = levels.copy()
            test.pop(j)
            if int(test[0]) == int(test[1]):
                continue
            if int(test[0]) < int(test[1]):
                check = 1
            if int(test[0]) > int(test[1]):
                check = 2
            for i,number in enumerate(test):
                if i == len(test)-1:
                    count+=1
                    safe = True
                    break
                if check == 1 and int(number) >= int(test[i+1]):
                    break
                if check == 2 and int(number) <= int(test[i+1]):
                    break
                if abs(int(number)-int(test[i+1])) > 3:
                    break
            if safe:
                safe = False
                break
    print(count)       
part1()
part2()