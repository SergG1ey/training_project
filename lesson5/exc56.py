def diction (dict):
    dictionary = {}
    for i in dict:
        value = dict[i]
        if bool(value):
            dictionary.update({i: value})
    return dictionary

my_dict = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
print(diction(my_dict))
