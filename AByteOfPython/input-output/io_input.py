# encoding=utf-8

__author__ = 'daniloqb'

special_chars = [' ', ',', '.', ':', ';', '-', '_']

def reverse(text):
    return text[::-1]  # usando slicing para reverter o texto ::-1


def sanitize(text):
    sanitized_text = ''

    for index in range(len(text)):
        if text[index] not in special_chars:
            sanitized_text += text[index]

    return sanitized_text.lower()


def is_palindrome(text):
    return sanitize(text) == sanitize(reverse(text))


if __name__ == '__main__':

    something = raw_input("Enter some text: ")
    while something != '':
        if is_palindrome(something):
            print "Yes, it is a palindrome"
        else:
            print "No, it is not a palindrome"

        print sanitize(something)
        print reverse(sanitize(something))
        something = raw_input("Enter some text: ")



