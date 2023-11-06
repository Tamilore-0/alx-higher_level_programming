#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list):
        return my_list
    i = 0
    while i < len(my_list):
        if i == idx:
            del my_list[i]
            i += 1
            continue
        i += 1
    return my_list
    

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)