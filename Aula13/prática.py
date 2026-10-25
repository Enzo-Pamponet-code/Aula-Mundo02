def somatorio(initial, end, jump):
    initial = int(input('Escreva um numero: '))
    end = int(input('Escreva um numero: '))
    jump = int(input('Escreva um numero: '))
    p = int(initial)
    for c in range(1, end+1, jump):
        p += c
    print(p)

somatorio('','','')
