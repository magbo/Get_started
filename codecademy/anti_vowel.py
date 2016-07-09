# takes one string, text, as input and returns the text with all of the vowels removed. Does't count Y as a vowel


def anti_vowel(text):
    vowels = ["a","e", "i", "o", "u", "A", "E", "I", "O", "U"]
    new_text = ''
    for w in text:
        if w not in vowels:
            new_text += w
    return new_text