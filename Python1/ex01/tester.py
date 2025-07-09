from array2D import slice_me

family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]
print(slice_me(family, 0, 2)) # family[0] && family[2]
print(slice_me(family, 1, -2)) # 1 set start from row 1-> family[2] && exclude family[len::-2] = family[2]
print(slice_me(family, 1, -1)) # family[1] && exclude last element so family[len::-1] = family[3]
print(slice_me(family, 0, 4)) # all cols, all rows
print(slice_me(family, 0, -len(family)+1)) # only first element