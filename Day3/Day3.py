import re
import time
with open("/workspaces/Advent2024/Day3/input.txt", "r") as file: 
     lines = file.read()
def part1():
     regex = r'(mul)\((\d+),(\d+)\)'
     m = re.findall(regex, lines)
     result = 0
     for i in m:
          a = int(i[1])
          b = int(i[2])
          result += a * b
     print(result)
def part2():
     regex = r"(mul)\((\d+),(\d+)\)|(do)\(\)|(don't)\(\)"
     m = re.findall(regex, lines)
     result = 0
     do = True
     while m:
          if m[0][-2] == "do":
               do = True
               m.pop(0)
          elif m[0][-1] == "don't":
               do = False
               m.pop(0)
          if do and m[0][0] == "mul":
               a = int(m[0][1])
               b = int(m[0][2])
               result += a * b
          m.pop(0)


     #print(result)
start = time.time()
part1()
print(time.time() - start)
part2()