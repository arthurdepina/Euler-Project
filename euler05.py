"""
Smallest Multiple

2520 is the smallest number that can be divided by each
of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20.
"""

def euler05(upper):
    i = 1
    for k in range(1, upper + 1): # Testando se i é divível por todos até 21
        if i % k > 0:  # Se o número atual não é divisível por k
            for j in range(1, upper + 1):
                # Encontrando um número j de modo que i * j seja divisível
                # por k. Quando encontrarmos um valor j que se adeque a essa
                # condição, todos os números i daqui para frente serão
                # divisíveis por k.
                if (i * j) % k == 0:
                    i *= j
                    break
    # Essa função funciona porque a partir do momento
    # que i é divisível por k, i * n para qualquer n
    # inteiro também será divisível por k. Obviamente.
    return i

print(euler05(20))

# Código original:

# i = 1
# for k in (range(1, 21)):
#     if i % k > 0:
#         for j in range(1, 21):
#             if (i*j) % k == 0:
#                 i *= j
#                 break
# print i

# Por lassevk em https://projecteuler.net/thread=5
