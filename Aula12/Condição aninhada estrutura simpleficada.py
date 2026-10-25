print('-'*120)
a = input('Digite algo: ')
print('-'*120)
if a.isnumeric():
    print('\033[32m Você digitou um numero')
elif a.isalpha():
    print('\033[33m Você digitou uma letra')
elif a.isalnum():
    print('\033[34mVocê digitou um alphanumerico')
else:
    print('\033[35mDigitou algum caractere diferente')
print('\033[m-'*120)