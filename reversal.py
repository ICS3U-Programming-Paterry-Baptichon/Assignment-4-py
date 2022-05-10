#!/usr/bin/env python3

# Created by: Paterry Baptichon
# Created on: 2022-05-01
# This program finds the reverse of a number

# Title of the program and user input 
def main():
    	
    number = print("\033[1;33;40m I am  going to reverse inputed number\n")
    number_string = input('Enter a number : ')
    reversed = 0

    # the user to input an integer and then outputs the 
    # number with the digits reversed.
    try:
        number = int(number_string)
# process of the reversal number
        while (number != 0):
            reverse = int(number % 10)
            reversed = reversed*10 + reverse
            number = int(number/10)
# dispaly the answer to the user.
        print("\033[1;36;40mthe answer is:")
        print(reversed)
        print("\n")
# Ask if user would like to calculate again 
        print("\033[1;39;40mWould you like to try with a again")
        play_again = str(input("Y or N:"))
        if(play_again == ("Y") or (play_again ==  "y")):
                main()
# if user input is negative or anything other than a ppositive integer than 
# display invalid input.
    except ValueError:
        print("\033[1;31;40m\n")
        print('Given input is not a number.')


if __name__ == "__main__":
    main()