'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua area e a quanttidade de tinta necessaria
para pinta-la sabendo que cada litro de tinta pinta uma area de 2m²'''
#recebendo dados do usuario
largura = float(input('Informe a largura da pareda: '))
altura = float(input('Informe a altura da parede: '))
#processamento
area_parede = largura * altura
quantidade_tinta = area_parede / 2
print(f'Sua parede mede {area_parede} m² e vai precisa de {quantidade_tinta} litros de tinta para pinta-la.')