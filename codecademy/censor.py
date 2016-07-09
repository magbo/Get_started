# takes two strings, text and word, as input. It should return the text with the word you chose replaced with asterisks.


def censor(text, word):

    asterisks_num = len(word)
    words_in_text = text.split()
    new_word = '*' * asterisks_num
    new_text = []

    print words_in_text
    print words_in_text[1]

    for i in words_in_text:
        print i
        if i == word:
            new_text.append(new_word)
        else:
            new_text.append(i)
    new_text = ' '.join(new_text)
    print new_text
    return new_text


censor("hello world", "world")