#
# Programa de exemplo para mostrar o que é strings
#
# Curso- Devenvolvimento para a web e dispositivos móveis
#
# UC- Algoritmos e Estrutura de Dados
#
# Nome- Guilherme Rodrigues
#
# Número- 22405041
#
# Data- 16/10/2024
#
frase = 'Hello wold'

print(f'A frase é: "{frase}"')

a = 'melancia'
b = 'pera'
c = a + ' e ' + b
print(c)
print(' e '.join([a, b]))

print(f'A dimensão da variavel c é: {len(c)}')

print(frase[:6])
print(frase[6:])
print(frase[6:9])
print(frase[6])

print(frase.find('wold'))
print(frase.replace('H','T'))
print(frase[frase.find('Hello')])