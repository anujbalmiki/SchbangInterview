given_str = str(input("Enter a string: "))


def double_str(given_str):
    new_str = ""

    for char in given_str:
        new_str += str(char) + str(char)
    print(new_str)


double_str(given_str)
