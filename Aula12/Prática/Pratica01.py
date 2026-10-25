import unidecode

print('\033[35m-'*150, '\033[m')
nome = unidecode.unidecode(input('Digite seu nome: ').strip().lower())

if nome in ['neymar','enzo']:
    print('\033[31mQue nome bonito!\033[m')

elif nome in ['maria', 'joao', 'paulo']:
    print('\033[35mSeu nome é popular\033[m')

else:
    print('\033[37mSeu nome é bem normal.\033[m')
print('\033[34mTenha um ótimo dia, {}!'.format(nome))

