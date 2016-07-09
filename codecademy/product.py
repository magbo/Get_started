def product(num_list):
    total = 1

    for number in num_list:
        total *= number
    return total

print product([4, 5, 5])
