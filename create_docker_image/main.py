"""The program open a command window, await for user input integer number and convert it to binary number"""
import numpy as np

def main():
    print("The program will convert a positive integer number to binary number\n")
    run_program = True
    while run_program:
        print("Please enter an integer number:")
        number = input()
        try:
            number = int(number)
            if number > 0:
                print(f"Binary representation: {np.binary_repr(number)}")
            else:
                print("Number is not a positive integer.")
        except ValueError:
            print("That's not an integer!")

        print("Do you want to continue? (y/n)")
        answer = input()   
        if answer == "n":
            run_program =  False
    print("Goodbye!")
if __name__ == "__main__":
    main()

Type