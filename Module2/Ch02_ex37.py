# Write a program to generate the following arithmetic examples.
# Hints:
# (1) Divide-and-conquer: what simpler problem do you need to solve? (2) Consider using strings to build numbers and then convert.
# (3) The range iterator may be helpful.

# read input variables par and score
par = int(input("Enter the par value in the range 3 to 5: "))
while(par < 3 or par > 5):
    print("You have entered the invalid par value!!!")
    par = int(input("Enter the par value in the range 3 to 5: "))
    score = int(input("Enter the user Score: "))
    # check whether the par is equal to the score
    if par == score:
        print("Par")
        # Check whether the score is less than the par
    elif score < par:
        if score == par-3:
            print("Albatross")
        elif score == par-2:
            print("Eagle")
        elif score == par-1:
            print("Birdie")
        else:
            print("You are not allowed to score less than 3 under par")
    # check whether the score is greater than the par
    elif score > par:
        if score == par+1:
            print("Bogey")
        elif score == par+2:
            print("Double Bogey")
        elif score == par+3:
            print("Tryiple Bogey")
        elif score > par+3:
            print("bad hole")
    # end of program
