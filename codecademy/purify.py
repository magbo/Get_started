def purify(num_list):
    new_list = []

    for number in num_list:
        if number % 2 == 0:
            new_list.append(number)
            print new_list
    return new_list

purify([1,2,3])

# why it is not possible to add printing after return
