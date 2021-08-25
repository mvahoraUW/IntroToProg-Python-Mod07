# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with Pickles and error handling,
#              When the program starts, it ask the user of 2 numbers
#              and it divides them. If the inputs are invalid or if a
#              they cannot be divided an error message is displayed. The
#              program saves the user user stored in a dictionary as a
#              "pickled" file and reloads it as well.
# ChangeLog (Moiz Vahora,8/23/2021, started Assignment07.py file):
# <Moiz Vahora>,<08.24.2021>,Modified code and formatted it for submission
# ---------------------------------------------------------------------------- #

# importing the modules requried for this program
import pickle

print("We are going to divide 2 numbers")

# Asking for user for 2 inputs with error handling implemented.
try:
    num1 = float(input("Please enter the numerator: "))
    num2 = float(input("Please enter the denominator: "))
except Exception as e:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
    print("Please restart the program!!!")
    # Using exit() to exit the program if an error occur
    exit()

# dividing the two user inputs with zero division error handling
try:
    divide = num1 / num2
except ZeroDivisionError as e:
    print("Please do not use Zero for the second number!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
    print("Please restart the program!!!")
    # Using exit() to exit the program if an error occurs
    exit()

# created a dictionary with user inputs and calculation
data_dict = {"Numerator": num1, "Denominator": num2, "Calculation": divide}

# Using 'with' statement to open and close file automatically

# using the pickle.dump function to pickle the dictionary with the user inputs/calculations and save the results
with open('data_pick.pkl', 'wb') as pickle_file:
    pickle.dump(data_dict, pickle_file)

# using the pickle.load function to load and "un-pickle" the file saved previously.
with open('data_pick.pkl', 'rb') as pickle_file:
    un_pickle = pickle.load(pickle_file)

# Printing both the user inputs and the de-pickled results into the pickle file.
print("Before Pickling the results\n")
print(data_dict)
print("\nAfter Pickling the results\n")
print(un_pickle)
