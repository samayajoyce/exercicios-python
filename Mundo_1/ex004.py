'''Faça um programa que leia algo pelo teclado
e mostre na tela o seu tipo e todas as informaçoes
possiveis sobre ele.'''

algo = input("digite qualquer coisa: ")
print(f"seu tipo é {type(algo)}")
print(f"Só tem espaços? {algo.isspace()}")
print(f"É um numero? {algo.isnumeric()}")
print(f'É alfabetico? {algo.isalpha()}')
print(f'É alfanumerico? {algo.isalnum()}')
print(f'Está em maisculas? {algo.isupper()}')
print(f'Está em minusculas? {algo.islower()}')
print(f'Está capitalizada? {algo.istitle()}')