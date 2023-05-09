def decimal_binary(num):
    if num == 0:
        return 0
    else:
        return num % 2 + 10 * decimal_binary(int(num/2))


print(decimal_binary(20))
