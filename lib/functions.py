#!/usr/bin/env python3

def greet_programmer():
   print('Hello')

greet_programmer()
def greet(name):
    print(f'Hello, {name}')
greet('John')

def greet_with_default(name="programmer"):
    print(f'Hello, {name}')
greet_with_default()

def add(num1, num2):
    '''return num1 + num2'''
    total = num1 + num2
    print(total)
add(4,5)


def halve(number):
    divided = number//2;
    print(divided)
halve(10)
