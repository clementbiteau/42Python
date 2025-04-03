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
    if len(sys.argv) != 2:
        raise AssertionError("not able to evaluate input")
    res = sys.argv[1].upper()
    if not all(char in NESTED_MORSE for char in res):
        raise AssertionError("the arguments are bad")

    res = (' '.join(NESTED_MORSE[char] for char in res.upper()))
    print(res)

if __name__ == "__main__":
    main()
    