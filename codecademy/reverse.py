# takes a string text and returns that string in reverse
# DOES NOT WORK


def reverse(text):
    reverse_string = ''
    for w in text range(len(text)-1, 1, -1):
        print
        reverse_string += str(w)
    return reverse_string

print reverse('abcd')
