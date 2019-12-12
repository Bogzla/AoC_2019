import math
fuel = 0
with open('01_in.txt') as f:
    for line in f:
        i = int(line)
        while i>0:
            i = (int(math.floor(int(i)/3))-2)
            fuel += i
        fuel -= i
print(fuel)
