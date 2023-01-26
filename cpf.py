

while True:
    cpf = input('Digite o número do CPF: ')
    if cpf == 'sair':
        break
    # Removing non-numeric characters
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        print('Número inválido')
        continue
    if cpf == '00000000000' or cpf == '11111111111' or cpf == '22222222222' or cpf == '33333333333' or cpf == '44444444444' or cpf == '55555555555' or cpf == '66666666666' or cpf == '77777777777' or cpf == '88888888888' or cpf == '99999999999':
        print('Número inválido')
        continue
    # Calculating 1st digit
    first_digit = 0
    for i in range(9):
        first_digit += int(cpf[i]) * (10 - i)
    first_digit = ((first_digit*10) % 11)
    if first_digit > 9:
        first_digit = 0
    # Calculating 2nd digit
    second_digit = 0
    for i in range(10):
        if i<9:
            second_digit += int(cpf[i]) * (11 - i)       
        else:
            second_digit += int(first_digit) * (11 - i)
    second_digit = ((second_digit*10) % 11)
    if second_digit > 9:
        second_digit = 0
    # Checking if both digits match
    if int(cpf[-2]) == first_digit and int(cpf[-1]) == second_digit:
        print('CPF Válido')
        continue      
    else:
        print('CPF Inválido')
        continue
