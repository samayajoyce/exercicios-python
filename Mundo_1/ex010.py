'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar'''
#dados de entrada
#cotação do dolar em 2025 é de R$5,45
money = float(input('How much do you have in your wallet? '))
#processamento
conversor = money / 5.45
#dados de saida
print(f'with R${money} you can buy U$$ {conversor:.2f}')