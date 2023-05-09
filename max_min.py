num_list = [1, 3, 5, 3, 78, 23, 5, 100]


def max_min(num_list):
    max = num_list[0]
    min = num_list[0]

    for value in num_list:
        if value < min:
            min = value
        elif value > max:
            max = value

    print("Max value is: ", max)
    print("Min value is: ", min)


max_min(num_list)
