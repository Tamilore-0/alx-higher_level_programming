#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return None
    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    roman_string += 'Z'
    for i in range(len(roman_string) - 1):
        current = roman_string[i]
        forward = roman_string[i + 1]
        for key, value in my_dict.items():
            if current == key:
                if current == roman_string[-2]:
                    sum -= my_dict[key]
                    break
                if my_dict[current] < my_dict[forward]:
                    sum += my_dict[key]
                else:
                    sum -= my_dict[key]
    return abs(sum)
roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))