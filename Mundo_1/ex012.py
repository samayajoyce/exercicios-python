'''Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto'''
#dados de entrada
preco = float(input('Informe o valor do produto R$:'))
#procesamento
novo_preco = preco - (preco* (5/100))
print(f'O valor do porduto com 5% de desconto R${novo_preco}')