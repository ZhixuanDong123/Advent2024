with open("Advent2024/Day2/input.txt", "r") as file:
    lines = file.readlines()
count = 0
for line in lines:
    levels = line.split()
    if levels[0] == levels[1]:
        continue
    if levels[0] < levels[1]:
        check = 1
    elif levels[0] > levels[1]:
        check = 2
    for i,number in enumerate(levels):
        if i == len(levels)-1:
            count+=1
            break
        if check == 1 and int(number) > int(levels[i+1]):
            break
        if check == 2 and int(number) < int(levels[i+1]):
            break
        if abs(int(number)-int(levels[i+1])) > 3:
            break
        if number == levels[i+1]:
            break
print(count)
                
        