import itertools as it
j = 0
for i in range(240298, 784957):
    s = str(i)
    if int(s[5]) >= int(s[4]) >= int(s[3]) >= int(s[2]) >= int(s[1]) >= int(s[0]): #NB this would be more concisely written as: for j in range(len(s)-1):    if s[j+1] >= s[j]:
        for k, g in it.groupby(s):
                if sum(1 for _ in g) == 2: #basically counting how many in g
                    j += 1
                    break #need this otherwise will count s twice if it has 2 number pairs
print(j)

#note to self still trying to get head around iteration and itertools but v. powerful
#consider s = '1223454'
#for k, g in itertools.groupby(s):
#   print(k)
#   print(list(g)) #will give:
#1
#['1']
#2
#['2', '2']
#3
#['3']
#4
#['4']
#5
#['5']
#4
#['4']
