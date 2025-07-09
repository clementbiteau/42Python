import sys
import string
from ft_filter import ft_filter

def main():
    """main() defined to take a string and an integer.
    We first split the string and appropriately use the lambda anonymous function that will
    check if the len of a word is greater than N"""
    def check_input(text: str)->bool:
        """checking the input if there are any non accepted format chars like punctuation as per constraints"""
        for w in text:
            if w in string.punctuation:
                return False
        return True
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        return
    try:
        text = sys.argv[1]
        try:
            min_len = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
        if not check_input(text) or min_len < 0:
            raise AssertionError("the arguments are bad")

        ft = ft_filter(lambda w: len(w) > min_len, text.split())
        print(ft)
        
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()