def is_palindrome_par(word):
    if len(word) == 0:
        return True
    elif word[0] == ' ':
        return is_palindrome_par(word[1:])
    elif word[-1] == ' ':
        return is_palindrome_par(word[:-1])
    elif word[0] == word[-1]:
        return is_palindrome_par(word[1:-1])
    else:
        return False


def is_palindrome_impar(word):
    if len(word) == 1:
        return True
    elif word[0] == ' ':
        return is_palindrome_impar(word[1:])
    elif word[-1] == ' ':
        return is_palindrome_impar(word[:-1])
    elif word[0].upper() == word[-1].upper():
        return is_palindrome_impar(word[1:-1])
    else:
        return False


def is_palindrome(word):
    if len(word)%2 == 0:
        return is_palindrome_par(word)
    else:
        return is_palindrome_impar(word)

print(is_palindrome('A baba baba'))