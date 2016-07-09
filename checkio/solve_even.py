def checkio(array):
    result = 0
    for n in array:

        if n % 2 == 0:
            result += array[n]

    total = result * array[len(array)-1]
    return total



print(checkio([0, 1, 2, 3, 4, 5]))
print(checkio([1, 3, 5]))