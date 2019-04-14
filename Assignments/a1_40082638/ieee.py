#!/usr/bin/env python3
decimal = input("Decimal number to convert: ")
neg = float(decimal) < 0

g_than0 = int(decimal[0:decimal.index(".")])
g_than0 = bin(g_than0)[2 if not neg else 3:]

l_than0 = float("0." + decimal[decimal.index(".")+1:])
binround = len(str(l_than0))-2

count = 0
binrep = ""
calcs = []
while count < 32:
    tmp = round(l_than0,binround)
    l_than0 *= 2;
    l_than0 = round(l_than0, binround)

    calcs.append(str(tmp) + " * 2 = " + str(l_than0))

    if l_than0 >= 1:
        binrep += "1"
        l_than0 -= 1
    else:
        binrep += "0"

    if l_than0 == 0 or l_than0 == "0":
        break;
    count+=1;

BIAS = 127

exp = len(g_than0)-1
g_than0 = g_than0[0]+"."+g_than0[1:]
binrep = g_than0 + binrep

sign = 1 if neg else 0
exponent = bin(exp + BIAS)[2:]
mantissa = binrep[2:25]

calcs = calcs[:24]
calccol = ""
for x in range(len(calcs)//3):
    calccol += calcs[x] + "    |    " + calcs[x+8] + "    |    " + calcs[x+16] + "\n";

print(calccol)
print(str(sign) + " | " + str(exponent) + " | " + str(mantissa) + " |")
