#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
    print("Happy New Year!")


def square_integers(int_list):
    squared_integers = [i**2 for i in int_list]
    return squared_integers


int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_integers(int_list)




def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 != 0:
            print('Fizz')
        elif i % 5 == 0 and i % 3 != 0:
            print('Buzz')
        elif i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        else:
            print(i)
