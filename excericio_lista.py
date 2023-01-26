import os

os.system('cls')

lista = list()

while True:
    print ('Selecione uma opção:')
    dado = input ('[i]ncluir  [a]pagar  [l]istar: ')    

    if dado == 'sair':
        print(lista)
        break

    if (dado!='i') and (dado!='a') and (dado!='l'):
        print ('Opção inválida')

    if dado=='i':
        valor = input ('Digite o item: ')
        lista.append(valor)
    
    if dado=='a':
        er = input ('Digite o número do item: ')
        indice = int(er)-1
        if (indice>=0) and (indice < len(lista)):
            del lista[indice]                    
            
    
    if dado == 'l':
        if len(lista) == 0:
            print ('Nada para listar')
        else:
            for i, valor in enumerate(lista):
                print (i+1, f'\t{valor}')
         

       

