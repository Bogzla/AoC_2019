import math
fuel = 0
with open('01_in.txt') as f:
    for line in f:
        fuel += (int(math.floor(int(line)/3))-2)
print(fuel)
