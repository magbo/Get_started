# takes a positive integer n as input and returns the sum of all that number's digits.


def digit_sum(n):
    n = str(n)
    strings_list = list(n)
    numbers_list = [int(n) for n in strings_list]
    result = sum(numbers_list)
    return result

print digit_sum(1234)
