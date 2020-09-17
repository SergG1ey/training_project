my_list = ['a', 'b', 'c', 'd', 'e']
dictionary = {}
for i in my_list:
    dictionary.update({my_list.index(i): i})
print(dictionary)
