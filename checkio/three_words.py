def checkio(words):

    count = 0

    for word in words.split():
        print(word)
        if word.isalpha():
            count += 1
            if count >= 3:
                return True
        else:
            count = 0
    if count < 3:
        return False

print(checkio("Hello World hello"))
print(checkio("He is 123 man"))
print(checkio("one two 3 four five six 7 eight 9 ten eleven 12"))

