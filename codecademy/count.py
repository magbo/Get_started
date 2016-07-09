def count(sequence, item):
    result = 0
    for i in sequence:
        if i == item:
            result += 1
            #print result

    print result
    return result


count([1,2,1,1], 1)