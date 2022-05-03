#!/usr/bin/env python3

# Created by: Paterry Baptichon
# Created on: 2022-05-01
# This program finds the reverse of a number

# Title of the program and user input 
def main():
    number = print(" I am  going to reverse inputed number")
    number_string = input('Enter a number : ')
    reversed = 0

    # the user to input an integer and then outputs the 
    # number with the digits reversed.
    try:
        number = int(number_string)
# execute a minimum of 0 times
        while (number != 0):
            reverse = int(number % 10)
            reversed = reversed*10 + reverse
            number = int(number/10)
# if user input is negative or anything other than a ppositive integer than 
# display invalid input.
        print(reversed)
    except ValueError:
        print('Given input is not a number.')


if __name__ == "__main__":
    main()