import time

lines = []
         
with open("/workspaces/Advent2024/Day4/input.txt", "r") as file:
    for line in file:
        lines.append(line.strip())
def part1():
    count = 0
    for i,row in enumerate(lines):
        for j,nums in enumerate(row):
            #check horizontal "SAMX" or "XMAS"
            if j+4 <= len(row):
                check = row[j:j+4]
                if check == "XMAS" or check == "SAMX":
                    count += 1
                       
            # check vertical "SAMX" or "XMAS"
            if i+4 <= len(lines):
                check = lines[i][j] + lines[i+1][j] + lines[i+2][j] + lines[i+3][j]
                if check == "XMAS" or check == "SAMX":
                    count += 1
            # check diagonal "SAMX" or "XMAS"
            if i+4 <= len(lines) and j+4 <= len(row):
                check = lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2] + lines[i+3][j+3]
                if check == "XMAS" or check == "SAMX":
                    count += 1
            # check anti-diagonal "XMAS"
            if i+4 <= len(lines) and j-3 >= 0:
                check = lines[i][j] + lines[i+1][j-1] + lines[i+2][j-2] + lines[i+3][j-3]
                if check == "XMAS" or check == "SAMX":
                    count += 1
    print(count)
def part2():
    count = 0
    check = 0
    for i,row in enumerate(lines):
        for j,num in enumerate(row):
            if i+3 <= len(lines) and j+3 <= len(lines[0]):
                check = lines[i][j] + lines[i][j+2] + lines[i+1][j+1] + lines[i+2][j] + lines[i+2][j+2]
                if check == "MMASS" or check == "SSAMM" or check == "MSAMS" or check == "SMASM":
                    count+=1

    print(count)
start = time.time()
part1()
print(time.time() - start)
part2()
