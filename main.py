from tests import *

def main():
    try:
        testNot()
        testNand()
        testAnd()
        testOr()
        testXOr()
        testXnor()
        print("all 6 gates passed!")
    except AssertionError as e:
        print("Test failed:", e)

if __name__ == "__main__":
    main()
