def NAND(a, b):
    if a==1 and b == 1:
        return 0
    else:
        return 1

def AND(a, b):
    temp = NAND(a, b)
    return NAND(temp, temp)

def AND1(a, b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0

def OR(a, b):
##OR(a, b) = NOT(AND(not (a), not(b)))
## not (A) = nand(A, A) 
## not (B) = nand(B, B)
    temp1 = NAND(a, a)
    temp2 = NAND(b, b)
    return NAND(temp1, temp2)

def OR1(a, b):
    if a == 1 or b == 1:
        return 1
    else:
        return 0

def NOR(a, b):
    temp = OR(a, b)
    return NAND(temp, temp)

def XOR(a, b):
## a = not(B) --> a = nand(B,B)    
##    if a == NAND(b, b):
##        return 1
##    else:
##        return 0
    temp1 = NAND(a, b) #NOT A AND B
    temp2 = NAND(a, temp1) #NOT A
    temp3 = NAND(b, temp1) #NOT B
    return NAND(temp2, temp3)

def XOR1(a, b):
##returns 1 if only a or b is 1
##if (a == 1 or b == 1) and AND(a, b) != 1:
##        return 1
##    else:
##        return 0
    if a != b:
        return 1
    else:
        return 0
    
def XNOR(a, b):
##return 1 when a==b, or not XOR
    temp = XOR(a, b)
    return NAND(temp, temp)

def NOR(a, b):
##NOT or
    temp = OR(a, b)
    return NAND(temp, temp)

def NOTA_AND_B(a, b):
    temp = NOT(a)
    return AND(temp, b)

def A_AND_NOTB(a, b):
    temp = NOT(b)
    return AND(a, temp)

def NOTA_OR_B(a, b):
    temp = NOT(a)
    return OR(temp, b)

def A_OR_NOTB(a, b):
    temp = NOT(b)
    return OR(a, temp)

def TRUE():
    return 1

def FALSE():
    return 0

def A(a):
    return a

def B(b):
    return b

def NOT(x):
    return (NAND(x, x))

