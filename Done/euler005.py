"""
Smallest Multiple

2520 is the smallest number that can be divided by each
of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20.
"""

def euler05(upper):
    i = 1
    for k in range(1, upper + 1):         # Testando se i é divível por todos até 21
        if i % k > 0:                     # Se o número atual não é divisível por k
            for j in range(1, upper + 1): # Encontrando um número j de modo que i * j seja divisível por k.
                if (i * j) % k == 0:      # Encontrando um número j de modo que i * j seja divisível por k
                    i *= j                # Quando encontrarmos um valor j que se adeque a essa condição
                    break                 # todos os números i * n daqui para frente serão divisíveis por k.
    return i

    # Essa função funciona porque a partir do momento
    # em que encontramos um j de modo que i = i * j é
    # múltiplo de k, todos os números i * n daqui para
    # para frente serão divisíveis por k. Obviamente.

print(euler05(20))

# Código original:
# Por lassevk em https://projecteuler.net/thread=5
#
# i = 1
# for k in (range(1, 21)):
#     if i % k > 0:
#         for j in range(1, 21):
#             if (i*j) % k == 0:
#                 i *= j
#                 break
# print i
