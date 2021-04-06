print()
vowels = ['a', 'e', 'i', 'o', 'u']
savedvowellist = set()
count = 0

while True:

    # Ask user for input
    inputstring = input('Enter a word: ')

    # Extract all the vowels from input string and make them lowercase
    inputstring = inputstring.lower()
    vowellist = [x for x in inputstring if x in vowels]

    # Add all the non duplicate vowels found into a temporary string
    vowellist = set(vowellist)
    savedvowellist = savedvowellist.union(vowellist)

    # End program when you all five vowels (aeiou) have been collected
    count += 1
    if len(savedvowellist) == 5:
        break


# print number of trials
print("It took {count} trials to collect all five vowel characters")
