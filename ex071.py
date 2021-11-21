from time import sleep

print('=' * 50)
print(f'{"SEJA BEM VINDO(A) AO BANCO WAA!":^50}')
print('=' * 50)

sleep(2)

print("NOTAS DISPONÍVEIS:")
print("R$ 50.00\nR$ 20.00\nR$ 10.00")

sleep(2)

saque = int(input('Qual valor você quer sacar? R$ '))

sleep(2)

while True:
    if saque % 50 == 0:
        print(f'{saque // 50} notas de R$ 50.00')

    elif saque % 50 != 0:
        print(f'{saque // 50} notas de R$ 50.00')
        print(f'{(saque % 50) // 20} notas de R$ 20.00')

        if saque % 50 != 0 and saque % 20 == 0:
            print(f'{saque // 20} notas de R$ 20.00')
        
    elif saque % 20 != 0 and (saque % 20) % 10 == 0:
        print(f'{saque // 10} notas de R$ 10.00')
    break
sleep(2)
print('=' * 50)
print(f'{"FIM":^50}')
print('Obrigado por usar o caixa eletrônico do Banco WAA!')
print(f'{"VOLTE SEMPRE!!!":^50}')
print('=' * 50)
