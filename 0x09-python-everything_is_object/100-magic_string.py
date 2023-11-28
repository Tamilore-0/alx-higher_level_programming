#!/usr/bin/python3
def magic_string(counter=[0]):
    counter[0] += 1
    return ", ".join("BestSchool" for _ in range(counter[0]))
