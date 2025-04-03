from ft_package import count_in_list

"""Quick tester to check if package using count_in_list outputs 2 then 0"""

print(count_in_list(["toto", "tata", "toto"], "toto"))  # Should output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # Should output: 0
