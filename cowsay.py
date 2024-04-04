# used to take in command line arguments from user
import sys
# used to make use of cow objects
from heifer_generator import HeiferGenerator as farm

def main(args):
    # list of available cow objects
    cows = farm.get_cows()

    match args[1]:
        # checks if user wants to list out available cows and does so using the list_cows method
        case "-l":
            print(f"Cows available: {list_cows(cows)} ")
        # checks if user wants to specify a cow and searches for it using the find_cow method, returning an error message if the cow is not found
        case "-n":
            cow = find_cow(args[2], cows)

            if cow:
                print(f'\n{" ".join(args[3:])} \n{cow.image}')

                # checks if the specified cow is a dragon and prints whether it can breathe fire or not
                if cow.name == "dragon":
                    print("This dragon can breathe fire.")
                elif cow.name == "ice-dragon":
                    print("This dragon cannot breathe fire.")
            else:
                print(f"Could not find {args[2]} cow!")
        # if no specifications are made, prints out the user's message with the default cow
        case _:
            print(f'\n{" ".join(args[1:])} \n{cows[0].image}')

# method used to print out the names of the available cows in the cow list
def list_cows(cows):
    return " ".join(cow.name for cow in cows)

# method used to find a specific cow in the cow list by name, returning None if it is not found
def find_cow(name, cows):
    return next((cow for cow in cows if cow.name == name), None)

if __name__ == "__main__":
    main(sys.argv)