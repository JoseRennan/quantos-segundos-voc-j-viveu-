print('De acordo com a sua idade') 
print('Irei identificar algumas curiosidades sobre')
print('O seu tempo de vida!')
print(' ')

nome = str(input('Qual é o seu nome?'))
print(' ')
idade = float(input('Quantos anos você tem? '))
print(' ')

mes = int(idade * 12)
dia = int(idade * 365)
horas = int(idade * 8760)
minutos = int(idade * 525600)
segundos = int(idade * 31536000)


print('Você viveu por' ,mes , 'meses')
print(' ')
print('Você viveu por' ,dia, 'dias')
print(' ')
print('Você viveu por' ,horas, 'horas')
print(' ')
print('Você viveu por' ,minutos, 'minutos')
print(' ')
print('Você viveu por' ,segundos, 'segundos')
print(' ')

print('Gostou das curiosidades sobre sua idade?',nome)
print(' ')
print('Espero que sim :)',nome)
