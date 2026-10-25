print('-'*60,'com while', '-'*60)
c = 1
while c < 10:
    print(c)
    c += 1
print('fim')
#-------------------------------------------------------------------------
print('-'*60,'com for', '-'*60)
for c in range(1,10):
    print(c)
print('fim')
#--------------------------------------------------------------------------
print('-'*60,'com for', '-'*60)
for c in range(1, 5):
    n = int(input('Digite um valor: '))
#----------------------------------------------------------------------------
c = 0
r = 'S'
while r=='S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper().strip()
print('fim')