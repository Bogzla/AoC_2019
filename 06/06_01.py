#create dictionary with outer orbit as key
orbit={}
with open('06_in.txt') as f:
    for line in f:
        orbit[line[4:7]] = line[:3]
#for each outer orbit, trace it back to COM counting 1 each time        
i = 0
for key in orbit:
    s = key
    while s != 'COM':
        print(s, '->', orbit[s])
        s=orbit[s]
        i += 1
print(i)
