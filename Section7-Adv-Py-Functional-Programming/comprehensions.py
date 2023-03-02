# list, set, dictonary

my_list = []

for char in 'jello':
    my_list.append(char)

# print(my_list)

comp_set = {char for char in 'lerolero'}
# print(comp_set)


simple_dict = {
    'a': 1,
    'b': 2
}
comp_dict = {key: value**2 for key, value in simple_dict.items()}

comp_dict2 = {str(num): num*2 for num in [1, 2, 3]}
print(comp_dict2)

# print(comp_dict)

comp_list = [param for param in 'hello']
comp_list2 = [n for n in range(0, 100)]
comp_list3 = [n**2 for n in range(0, 100)]
comp_list4 = [n for n in comp_list3 if n % 2 == 0]
# print(comp_list)
# print(comp_list2)
# print(comp_list3)
# print(comp_list4)
