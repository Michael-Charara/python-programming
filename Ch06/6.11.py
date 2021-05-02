safe_input = input(str("Enter a String Type you want to check: "))

test = safe_input("this is a string")
print('"{}" is a {}'.format(test, type(test)))
test = safe_input("this is a string", int)
print('"{}" is a {}'.format(test, type(test)))
test = safe_input("this is a string", float)
print('"{}" is a {}'.format(test, type(test)))
test = safe_input(5)
print('"{}" is a {}'.format(test, type(test)))
test = safe_input(5, int)
print('"{}" is a {}'.format(test, type(test)))
test = safe_input(5, float)
print('"{}" is a {}'.format(test, type(test)))
test = safe_input(5.044)
print('"{}" is a {}'.format(test, type(test)))
test = safe_input(5.044, int)
print('"{}" is a {}'.format(test, type(test)))
test = safe_input(5.044, float)
print('"{}" is a {}'.format(test, type(test)))


def safe_input(prompt, type_=str):
    if(type_ not in (str, int, float)):
        raise ValueError("Expected str, int or float.")

    while True:
        test = input(prompt)
        try:
            ret = type_(test)
        except ValueError:
            print("Invalid type, enter again.")
        else:
            break

    return ret
