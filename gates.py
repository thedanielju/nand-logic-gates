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

def XOR(a, b):
## a = not(B) --> a = nand(B,B)    
    if a == NAND(b, b):
        return 1
    else:
        return 0

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