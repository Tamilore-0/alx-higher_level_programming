#!/usr/bin/python3
def fizzbuzz():
    for num in range(0, 101):
        if num % 3 == 0:
            print("Fizz", end=" ")
        elif num % 5 == 0:
            print("Buzz", end=" ")
        elif num % 5 and 3:
            print("FizzBuzz", end=" ")