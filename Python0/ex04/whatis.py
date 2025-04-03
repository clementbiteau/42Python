import sys

def whatis():
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    if len(sys.argv) == 2:
        try:
            arg = int(sys.argv[1])
            print("I'm Even.") if (arg % 2 == 0) else print("I'm Odd.")
        except ValueError:
            raise AssertionError("argument is not an integer")
        
whatis()