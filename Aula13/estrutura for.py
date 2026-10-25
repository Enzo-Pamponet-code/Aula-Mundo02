def acao():
    def passar(self):
        print('Passou')

    def pegar(self):
        print('Pegar')

    for i in range(1, 10):
        passar('')
    pegar('')
a = input('Deseja fazer um acao?: ').strip().lower()
if a in ['sim', 's']:
    acao()
else:
    print('not')
#----- código copiado do universo python----------
cores = ["vermelho", "azul", "verde"]

for indice, cor in enumerate(cores):
    print(f"Índice {indice}: cor {cor}")
#-----------------------------------------
#--------testes----------
a = enumerate(cores)
print(a)
b = range(len(cores))
print(b)
#-------------------
#--------perguntas---------
lista = ['frog-stand: ', 'elbow-lever: ','l-sit: ']
for c in lista:
    input(c)