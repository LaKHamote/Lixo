def is_palindromo(word):
    return word == word[::-1]
    
    
def quase_palindromo(word, um_erro):
    if len(word) == 0:
        return True
    elif word[0] == word[-1]:
        return quase_palindromo(word[1:-1], um_erro)
    elif not um_erro:
        um_erro = True
        return quase_palindromo(word[1:-1], um_erro)
    else:
        return False
        
        
um_erro = False 
word = input()
if (len(word)%2) != 0 and (is_palindromo(word) or quase_palindromo(word, um_erro)):
    print('POSSÍVEL')
elif (len(word)%2) == 0 and not is_palindromo(word) and quase_palindromo(word, um_erro):
    print('POSSÍVEL')
else:
    print('IMPOSSÍVEL')

