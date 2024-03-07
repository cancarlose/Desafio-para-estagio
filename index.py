# 1)
# O trecho de código apresenta um loop que soma os valores de 1 até o valor de INDICE, que é 13.
# Portanto, a variável SOMA conterá a soma dos números de 1 até 13. O valor final de SOMA será 91.

# <----------------------->

# 2)
# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

#IMPORTANTE:

# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

import math

def pertence_sequencia_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b

    if b == numero:
        print(f"{numero} pertence à sequência de Fibonacci.")
    else:
        print(f"{numero} não pertence à sequência de Fibonacci.")

# Exemplo de uso
pertence_sequencia_fibonacci(13)

# Neste exemplo, o número 13 é fornecido como entrada, e a função verifica se ele pertence à sequência de Fibonacci.
# A saída será que 13 pertence à sequência.

# <----------------------->

# 3)
# Lógica e Próximo Elemento:
# a) 9
# b) 128
# c) 49
# d) 100
# e) 13
# f) 20

# <----------------------->

# 4)
# Descobrindo os Interruptores e Lâmpadas:

# Ligue o primeiro interruptor e espere por alguns minutos.
# Desligue o primeiro interruptor e ligue o segundo interruptor.
# Entre na sala com as lâmpadas.
# A lâmpada acesa está conectada ao segundo interruptor.
# A lâmpada apagada, mas quente, está conectada ao primeiro interruptor.
# A lâmpada apagada e fria está conectada ao terceiro interruptor.

# <----------------------->

# 5)
import math

def inverter_string(s):
    inverted_string = ""
    for char in s:
        inverted_string = char + inverted_string
    return inverted_string

# Exemplo de uso
string_original = "Hello, World!"
string_invertida = inverter_string(string_original)
print(f"String Original: {string_original}")
print(f"String Invertida: {string_invertida}")

#Neste exemplo, a função inverter_string recebe uma string e retorna sua versão invertida, sem o uso de funções prontas como reverse.
# O resultado é então impresso

# <----------------------->