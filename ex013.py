'''Faça um algoritimo que leia o salario de um funcionario e mostre seu novo
salario com 15% de aumento'''
#dados de entrada
salario = float(input('Informe seu salario R$:'))
#processamento
novo_salario = salario +(salario *(15/100))
print(f'Seu novo salario com 15% de aumento é R${novo_salario}')