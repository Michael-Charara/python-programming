#  In football, there is a statistic for quarterbacks called the passer rating. To calculate the passer rating, you need four inputs: pass completions, pass attempts, total passing yards, and interceptions. There are five steps in the algorithm. Write a program that asks for
# the five inputs and then prints the pass rating:
# (a) C is the “completions per attempt” times 100 − 30 all divided by 20.
# (b) Y is the “yards per attempt” − 3 all divided by 4.
# (c) T is the “touchdowns per attempt” times 20.
# (d) I is 2.375 minus (“interceptions per attempts” times 35).
# (e) The pass rating is the sum of C, Y, T, and I all divided by 6 and then multiplied by 100.

# Prompt user for completions per attempt
C_str = input('Enter completetions per attempt rating: ')
# Prompt user for yards per attempt
Y_str = input('Enter yards per attempts: ')
# Prompt user for touchdowns per attempt
T_str = input('Enter touchdowns per attempt: ')
# Prompt user for interceptions per attempt
I_str = input('Enter interceptions per attempt: ')

# Convert user inputs to floats
C_float = float(C_str)
Y_float = float(Y_str)
T_float = float(T_str)
I_float = float(I_str)

# Calculte completions per attempt
# multiple c_float with 100, subtract 30, divide by 20
C = ((C_float * 100)-30)/20

# calculate yards per attempt
# subtract y_float by 3, divide by 4
Y = (Y_float - 3)/4

# calculate touchdowns per attempt
# multiply T-float by 20
T = T_float * 20

# calculate intercpetions per attempt
# multiply value of I_float with 35, subtract result by 2.375
I = 2.375 - (I_float * 35)

# calculate passing rate
# add values C,Y,T,I and divide by 6 than multiply by 100
PassRate = ((C+Y+T+I)/6) * 100
print('The pass rating is: ', PassRate)
