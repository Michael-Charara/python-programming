# Code Listing 3.1

a = input("give a number: ")
b, c = 1, 0
while b <= a:
    c = c+b
    b = b+1
print(a, b, c)
print("Result: ", c/b-1)

# First, it is hard to tell what the program does. Part of the problem is that the variable names are not descriptive. We will see that there is a time and a place for single-character variables, but a readable program will have few. Second, there are no comments. What is the program supposed to be doing? Third, there are two errors in this program, and its lack of readability makes them difficult to find. If you run the code, the first error prevents the code from running. (What is it?). Second, if that first error is fixed, we end up with the wrong answer.
