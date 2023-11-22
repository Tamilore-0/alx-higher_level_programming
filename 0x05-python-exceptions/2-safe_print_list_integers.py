#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0

    for i in range(x):
        try:
            # Try to print the integer value of my_list[i] with formatting
            print("{:d}".format(my_list[i]), end="")
            count += 1  # Increment count if successful
        except (ValueError, TypeError):
            continue  # Skip to the next iteration if the element is not an integer

    print()  # Print a newline after printing the integers
    return count 







my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))     