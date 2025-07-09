import sys
import string

def count_str(s: str):
    """This is a helper function for the main. It will count the number of chars of each specified set"""
    Upper = sum(1 for char in s if char.isupper())
    Lower = sum(1 for char in s if char.islower())
    Punc = sum(1 for char in s if char in string.punctuation)
    Spaces = sum(1 for char in s if char.isspace())
    Digits = sum(1 for char in s if char.isdigit())
    
    
    
    print("The text contains", len(s), "characters:")
    print(Upper, "upper letters")
    print(Lower, "lower letters")
    print(Punc, "punctuation marks")
    print("1 space" if Spaces == 1 else f"{Spaces} spaces")
    print(Digits, "digits")

def main():
    """This function attempts to do 3 steps
    1) Length of input must be 1 string (no more no less = AssertionError)
        - Python3 > building.py > string --> string as None or nothing will request user to enter a string to count
    2) Counts the length of the string
    3) Print -> number of (Upper Case chars) + (Lower Case chars ) + (Punctuation marks) + (Spaces) + (Digits)
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("Too many Arguments: Only One String is Expected.")
        if len(sys.argv) == 2 and sys.argv[1] != "None":
            res = sys.argv[1]
        else:
            print("What is the text to count?")
            res = input()
            while res == "None" or len(res) < 1:
                print("Come on we need a text to count...")
                res = input()
        count_str(res)
    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()