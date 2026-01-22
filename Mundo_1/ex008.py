'''escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros'''
#recebendo valor
valor = float(input('Digite valor em metros: '))
#manipulando esse valor
centimetro = valor * 100
milimetro = valor * 1000
#mostrando o resultado da conversão
print(f'O valor em centimetro é {centimetro}cm\nO valor em milimetro é {milimetro}mm')