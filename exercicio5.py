#Crie um programa que dados o valor, a taxa e o tempo, efetuar o cálculo
#do valor de uma prestação em atraso,utilizando a fórmula:
#prestação = valor + (valor * (taxa/100) * tempo)

v=float(input('Digite o valor:'))
tx=int(input('Digite a taxa:'))
t=int(input('Digite o tempo:'))
p= v + (v * (tx/100) * t)

print('A prestação em atraso é de ', p)

