j = 0
for i in range(240298, 784957):
    s = str(i)
    if int(s[5]) >= int(s[4]) >= int(s[3]) >= int(s[2]) >= int(s[1]) >= int(s[0]):
        if int(s[0]) == int(s[1]) or int(s[1]) == int(s[2]) or int(s[3]) == int(s[2]) or int(s[4]) == int(s[3]) or int(s[5]) == int(s[4]):
            print s
            j +=1
print(j)
#1660 is too high, but curiously someone elses answer
# - this was because I misread and was looking for decreasing instead of increasing
#corrected this and new answer 1149 - is too low
#OK, forgot python doesn't look at the last value in range() so opened it up to look at the whole puzzle input (240298 - 784956)
