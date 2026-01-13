print("Exemplo de importação de um módulo padrão:")
import math # Importar todo o módulo math
from math import pi, sqrt # Importar funções específicas do módulo math

pi = math.pi
print(f"O valor de pi é {pi}")

raiz_quadrada = math.sqrt(25)
print(f"A raiz quadrada de 25 é {raiz_quadrada}")

print("\nExemplo de criação e utilização de um módulo personalizado:")
import meu_modulo # Importar todo o módulo personalizado
from meu_modulo import saudacao, dobro # Importar funções específicas do módulo personalizado

mensagem = meu_modulo.saudacao("Igor")
print(mensagem)

resultado = meu_modulo.dobro(10)
print(f"O dobro de 10 é {resultado}")