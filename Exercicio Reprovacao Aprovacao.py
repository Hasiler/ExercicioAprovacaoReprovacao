nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
faltas = int(input('Quantidade de Faltas'))
media = float

media = nota1 + nota2 / 2
print('Sua média é:', media)

if media >= 7.0 and faltas <= 3:
    print('Aprovado')
else:
    print('Reprovado')
