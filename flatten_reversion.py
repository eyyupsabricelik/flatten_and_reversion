my_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
def flatten_list(nested_list):
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else: 
            flattened.append(item)
    return flattened
#reversion
def reverse_nested_list(nested_list):
    reversed_list = []
    for item in reversed(nested_list):
        if isinstance(item, list):
            reversed_list.append(reverse_nested_list(item))
        else:
            reversed_list.append(item)
    return reversed_list
flattened_my_list = flatten_list(my_list)
flattened_and_reversed_my_list = reverse_nested_list(flattened_my_list)

print(flattened_and_reversed_my_list)