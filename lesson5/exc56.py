def remove_none_from_dict(some_dict):
  return { key: value for key, value in some_dict.items() if value is not None }

my_dict = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
print(remove_none_from_dict(my_dict))
