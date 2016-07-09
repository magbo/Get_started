# removes duplicates from a list


def remove_duplicates(num_list):
    new_list= []

    for number in num_list:
        if number not in new_list:
            new_list.append(number)
    return new_list


print remove_duplicates([1,1,2,2])