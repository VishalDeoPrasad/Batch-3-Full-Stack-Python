lst = [1,2,3,4,5,6,7,8,9,10]

even_list = list(filter(lambda n: (n%2 == 0), lst))
odd_list = list(filter(lambda n: (n%2 != 0), lst))
print(even_list)
print(odd_list)