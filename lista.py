#
# Programa de exemplo para mostrar listas
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

nomes = ['Manel', 'Maria', 'Sara', 'Francisco']
outra = ['Maria', 33, True]
terceira = [1, 2, 3, 4, 5, 6]

print(f"Número de nomes na lista: {len(nomes)}")
print(f"O segundo nome da lista é: {nomes[1]}")
print(f"O 3º nome da lista é: {nomes[2:3]}")
print(f"Os nomes a partir do 2º são: {nomes[1:]}")
print('Mariana' in nomes)
print(outra)

print([2 * x for x in terceira])            # outra lista com dobros
print([x for x in terceira if x % 2 == 0])  # sublista só com paresr x in terceira)