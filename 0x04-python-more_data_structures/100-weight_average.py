#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:  # Check if the list is empty
        return 0

    total_weighted_sum = 0
    total_weight = 0

    for score, weight in my_list:
        total_weighted_sum += score * weight
        total_weight += weight

    if total_weight == 0:  # Avoid division by zero
        return 0

    weighted_average = total_weighted_sum / total_weight
    return weighted_average
