'''Crie um algoritimo que leia um numero
e mostre o seu dobro,triplo e raiz quadrada'''
#lendo o numero
numero = int(input('Digite um numero: '))
#manipulando esse numero
dobro = numero ** 2
triplo = numero ** 3
raiz_quadrada = numero ** (1/2)
#mostrando o resultado da manipulação
print(f'O seu dobro é {dobro}\nO seu triplo é {triplo}\nA sua raiz quadrada é {raiz_quadrada}')
