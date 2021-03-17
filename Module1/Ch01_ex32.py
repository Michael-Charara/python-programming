# A telephone directory has N lines on each page, and each page has exactly C columns. An entry in any column has a name with the corresponding telephone number. On which page, column, and line is the X th entry (name and number) present? (Assume that page, line, column numbers, and X all start from 1.)

# prompt user for entry a number
Entry_number = input('Enter the number of your entry: ')
# Convert value to integer
Entry_number_int = int(Entry_number) - 1

# Assuming 20 items per colum and 4 columns per page
# Assign columns in a page
Columns = 4
# Assign lines in a page
Lines = 20

# calculate number of items per page
Items = Columns * Lines

# Divide entry number by items and add 1 to find page number
Page = Entry_number_int / Items + 1
# round to the neares whole number and print
print('The page is: ', round(Page))

# Modulus entry by item value and divide by columns and add 1 to find line number
Line_value = (Entry_number_int % Items) / Columns + 1
# round to the nearest whole number and print
print('The line is: ', round(Line_value))

# Modulus entry by item and modules result by column. Than add 1 to find columns
Column_value = (Entry_number_int % Items) % Columns + 1
print('The column is: ', Column_value)
