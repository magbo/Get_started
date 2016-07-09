from collections import Counter


def find_message(text):
    output = ''
    words = text.split()
    #wordCount = Counter(words)
    for word in words:
        letters = list(word)
        print("letters=", letters)
        for letter in letters:
            print("letter=", letter)
            if letter.isupper():
                output += letter
                print("O=", output)
    return output

print (find_message("Hello World"))
