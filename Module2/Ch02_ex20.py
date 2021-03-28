# Write a program that prompts for an integer and prints the integer, but if something other than an integer is input, the program keeps asking for an integer. Here is a sample session:
# Input an integer: abc
# Error: try again. Input an integer: 4a Error: try again. Input an integer: 2.5 Error: try again. # Input an integer: 123 The integer is: 123
# Hint: The string isdigit method will be useful.

# Get integer input
num = input("Enter an integer number: ")

# Look executes until input is other than integer
while num.isdigit() == False:
    # display the error message and get another input
    num = input("Error: trye again, Enter an integer number: ")
else:
    # convert the input to integer
    number_int = int(num)
    # Display the integer number
    print("The integer number is: ", number_int)
