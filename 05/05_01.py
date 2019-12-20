import math
#pgm = [3,0,4,0,99]
pgm = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,40,93,224,1001,224,-3720,224,4,224,102,8,223,223,101,3,224,224,1,224,223,223,1101,56,23,225,1102,64,78,225,1102,14,11,225,1101,84,27,225,1101,7,82,224,1001,224,-89,224,4,224,1002,223,8,223,1001,224,1,224,1,224,223,223,1,35,47,224,1001,224,-140,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1101,75,90,225,101,9,122,224,101,-72,224,224,4,224,1002,223,8,223,101,6,224,224,1,224,223,223,1102,36,63,225,1002,192,29,224,1001,224,-1218,224,4,224,1002,223,8,223,1001,224,7,224,1,223,224,223,102,31,218,224,101,-2046,224,224,4,224,102,8,223,223,101,4,224,224,1,224,223,223,1001,43,38,224,101,-52,224,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,1102,33,42,225,2,95,40,224,101,-5850,224,224,4,224,1002,223,8,223,1001,224,7,224,1,224,223,223,1102,37,66,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1007,226,677,224,1002,223,2,223,1005,224,329,1001,223,1,223,1007,226,226,224,1002,223,2,223,1006,224,344,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,359,1001,223,1,223,108,677,677,224,1002,223,2,223,1006,224,374,1001,223,1,223,107,677,677,224,1002,223,2,223,1005,224,389,101,1,223,223,8,677,677,224,1002,223,2,223,1005,224,404,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,419,101,1,223,223,1008,677,677,224,1002,223,2,223,1005,224,434,101,1,223,223,1008,226,226,224,1002,223,2,223,1005,224,449,101,1,223,223,7,677,226,224,1002,223,2,223,1006,224,464,1001,223,1,223,7,226,226,224,1002,223,2,223,1005,224,479,1001,223,1,223,1007,677,677,224,102,2,223,223,1005,224,494,101,1,223,223,1108,677,226,224,102,2,223,223,1006,224,509,1001,223,1,223,8,677,226,224,102,2,223,223,1005,224,524,1001,223,1,223,1107,226,226,224,102,2,223,223,1006,224,539,1001,223,1,223,1008,226,677,224,1002,223,2,223,1006,224,554,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,569,1001,223,1,223,1108,677,677,224,102,2,223,223,1005,224,584,101,1,223,223,7,226,677,224,102,2,223,223,1006,224,599,1001,223,1,223,1108,226,677,224,102,2,223,223,1006,224,614,101,1,223,223,107,226,677,224,1002,223,2,223,1005,224,629,101,1,223,223,108,226,677,224,1002,223,2,223,1005,224,644,101,1,223,223,8,226,677,224,1002,223,2,223,1005,224,659,1001,223,1,223,107,226,226,224,1002,223,2,223,1006,224,674,101,1,223,223,4,223,99,226]
#print('programme length:',len(pgm)) #debugging
i = 0
op = 0
while op != 99:
    code = str(pgm[i])
    #print('ctr:',i, '-> instr:', code) #debugging
    #op = int(code[-2:]) #op code
    print('op: ',op) #debugging
    m1 = 0  #mode parameter 1
    m2 = 0  #mode parameter 2
    m3 = 0  #mode parameter 3
    if len(code) > 2:
        m1 = int(code[-3:-2])
        if len(code) > 3:
            m2 = int(code[-4:-3])
            if len(code) > 4:
                m3 = int(code[-5:-4])
    #print('m1:',m1, ' m2:',m2,' m3:',m3) #debugging  
    if op == 99: #end programme
        break
    if m1 == 0: #get parameter values, either literal or from address depending on mode
        p1 = pgm[pgm[i+1]]
    else:
        p1 = pgm[i+1]
    if op == 1 or op == 2: #op codes 1 and 2 only have parameters 2 and 3
        if m2 == 0:
            p2 = pgm[pgm[i+2]]
        else:
            p2 = pgm[i+2]
        if m3 == 0:
            p3 = pgm[pgm[i+3]]
        else:
            p3 = pgm[i+3]
    if op == 1: #[opcode1, a, b, c] // c=a+b
        pgm[pgm[i+3]] = p1+p2
        i += 4
    elif op == 2: #[opcode2, a, b, c] // c=a*b
        pgm[pgm[i+3]] = p1*p2
        i += 4
    elif op == 3: #[opcode3, a] // a = input
        print('Enter Input: ')
        pgm[pgm[i+1]] = int(input())
        i += 2
    elif op == 4: #[opcode4, a] // output = a
        print('Output: ', p1)
        i += 2
    #input('Continue..') #debugging
