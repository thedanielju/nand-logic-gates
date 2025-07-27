from gates import *

def testNot():
    print("Testing NOT gate:")
    for a in [0, 1]:
        expected = 1 - a
        actual = NOT(a)
        assert actual == expected, f"NOT({a}) failed: got {actual}, expected {expected}"
    print("  NOT passed.\n")

def testNand():
    print("Testing NAND gate:")
    for a in [0, 1]:
        for b in [0, 1]:
            expected = 1 - (a & b)
            actual = NAND(a, b)
            assert actual == expected, f"NAND({a}, {b}) failed: got {actual}, expected {expected}"
    print("  NAND passed.\n")

def testAnd():
    print("testing AND gate:")
    for a in [0, 1]: ##loops through a = 0, 0
        for b in [0, 1]: ##loops through b = 0, 1
            expected = AND1(a,b)
            actual = AND(a,b)
            print( f" AND{a}, {b} = {actual} (expected: {expected})")
            assert actual == expected, f"AND failed for ({a}, {b})"
    print(" AND passed.\n")

def testOr():
    print("testing OR gate:")
    for a in [0, 1]: ##loops through a = 0, 0
        for b in [0, 1]: ##loops through b = 0, 1
            expected = OR1(a,b)
            actual = OR(a,b)
            print( f" OR{a}, {b} = {actual} (expected: {expected})")
            assert actual == expected, f"OR failed for ({a}, {b})"
    print(" OR passed.\n")

def testXOr():
    print("testing XOR gate:")
    for a in [0, 1]: ##loops through a = 0, 0
        for b in [0, 1]: ##loops through b = 0, 1
            expected = XOR1(a,b)
            actual = XOR(a,b)
            print( f" XOR{a}, {b} = {actual} (expected: {expected})")
            assert actual == expected, f"XOR failed for ({a}, {b})"
    print(" XOR passed.\n")

def testXnor():
    print("Testing XNOR gate...")
    for a in [0, 1]:
        for b in [0, 1]:
            expected = int(a == b)
            actual = XNOR(a, b)
            assert actual == expected, f"XNOR({a}, {b}) failed: got {actual}, expected {expected}"
    print("  XNOR passed.\n")
