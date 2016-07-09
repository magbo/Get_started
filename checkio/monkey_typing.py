def count_words(text, words):

    used_words = []

    # joined_text = text.replace(" ", "") => without spaces
    print(text)
    for word in words:
        if word in text.lower():  # text.find(word)
            used_words.append(word)
            print(used_words)
    used_words = list(set(used_words))  # => removing duplicates
    # print(used_words)

    result = len(used_words)
    return result






print(count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}))  # result => 3
print(count_words("Bananas, give me bananas!!!", {"banana", "bananas"}))  # result => 2
print(count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                  {"sum", "hamlet", "infinity", "anything"})) # result => 1
