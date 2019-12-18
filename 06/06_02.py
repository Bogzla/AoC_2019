#create dictionary with outer orbit as key
orbit={}
with open('06_in.txt') as f:
    for line in f:
        orbit[line[4:7]] = line[:3]
#Start with YOU and move toward COM, creating a new dictionary, storing # of orbital transfers on the way
yorbit={}
i = 0
s = 'YOU'
while s != 'COM':
    print(s, '->', orbit[s])
    s = orbit[s]
    yorbit[s] = i
    i += 1
print('\0')
#Now start with SAN and move toward COM looking for an orbit YOU have passed, counting on the way
i = 0
s = 'SAN'
while s != 'COM':
    print(s, '->', orbit[s])
    s = orbit[s]
    if s in yorbit: #once we find the first common orbit, simply add orbital transfers of YOU and SANTA to both get here
        transfers = i + yorbit[s]
        print(transfers)
        break
    i += 1

