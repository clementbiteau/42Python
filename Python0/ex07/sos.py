import sys

NESTED_MORSE = {    
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',     'F': '..-.',  'G': '--.',    'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',    'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',     'U': '..-',   'V': '...-',  'W': '.--',    'X': '-..-',
    'Y': '-.--',  'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',

    ' ': '/'
    }

def main():
    """Simple program that takes a string as input and prints the morse code version of it.
    Note: the dictionnary of Nested Morse does not include special characters. If any are viewed by the main(),
    it will be immediately discarded as an Assertion Error"""
    if len(sys.argv) != 2:
        raise AssertionError("not able to evaluate input")
    res = sys.argv[1].upper()
    if not all(char in NESTED_MORSE for char in res):
        raise AssertionError("the arguments are bad")

    res = (' '.join(NESTED_MORSE[char] for char in res.upper()))
    print(res)

if __name__ == "__main__":
    main()
    