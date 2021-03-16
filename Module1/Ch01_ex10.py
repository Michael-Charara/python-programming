# A nursery rhyme: As I was going to St. Ives, I met a man with seven wives.Every wife had seven sacks, and every sack had seven cats, every cat had seven kittens. Kittens, cats, sacks, and wives, how many were going to St. Ives? There are interesting aspects to this puzzle, such as who is actually going to St. Ives. For our purposes, assume that everyone and everything are headed to St. Ives. Write a program to calculate that total.

# Assign value for number of wives per man
wives_per_man = 7
# Assign value for number of sacks per wife
sacks_per_wife = 7
# Assign value for number of cats per sack
cats_per_cat = 7
# Assign value for number of kitterns per cat
kittens_per_cat = 7

# Calculate total
total = wives_per_man*sacks_per_wife*cats_per_cat*kittens_per_cat

# Display the total
print('Total going to St. Ives: ', total)
