# calculates a median value


def median(numbers):
    numbers = sorted(numbers)
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers)/2] + numbers[len(numbers)/2 - 1])/2.0
    else:
        return numbers[len(numbers)/2 - 0.5]

print median([7, 12, 3, 1, 6])
