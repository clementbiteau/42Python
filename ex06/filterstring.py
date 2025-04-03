from ft_filter import ft_filter
import sys

def main():
    """main() defined to take a string and an integer.
    We first split the string and appropriately use the lambda anonymous function that will
    check if the len of a word is greater than N"""
    if len(sys.argv) == 3:
        try:
            S = str(sys.argv[1])
            N = int(sys.argv[2])
        except ValueError:
            raise AssertionError("could not evaluate input")
        
        # Here we use list comprehension
        # we store in result_l_c a list that takes a word (split from string S) if the len of the word is greater than N.
        result_list_comprehension = [word for word in S.split() if (lambda x: len(x) > N)(word)]
        print(result_list_comprehension)

        # Here we use ft_filter(), our own function to perform the same operation
        # We store in result_list a created list using the ft_filter()
        result_list = list(ft_filter(lambda word: len(word) > N, S.split()))
        print(result_list)
    else:
        raise AssertionError("the arguments are bad")

if __name__ == "__main__":
    main()