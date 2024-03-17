## EP2_2 - Equação do segundo grau

Faça um programa que, dados os coeficientes a,b,c , resolva a equação de segundo grau:
```
ax2+bx+c=0
```

Caso a equação não tenha solução, o programa deverá exibir "Sem solucao real!" (sem utilizar acento e cedilha), seguido pelo valor de Δ, formatado com duas casas decimais.
Caso a equação tenha solução única, o programa deverá exibir apenas essa solução, formatada com duas casas decimais.
Caso a equação tenha duas soluções, o programa deverá exibi-las em linhas separadas, em ordem crescente, formatadas com duas casas decimais.

Entradas:
```
Coeficiente a (inteiro)
Coeficiente b (inteiro)
Coeficiente c (inteiro)
```
Saídas:
```
Soluções de ax2+bx+c=0
 (se existirem)
```

Observações:
1. Nexte exercício, pode utilizar funções prontas para calcular raiz quadrada.

Em Java:
```
import java.lang.Math;
double resultado = Math.sqrt(9)
```
Em Python:
```
import math
resultado = math.sqrt(9)
```

2. Formatação da saída:

Em Python, é possível formatar saídas das seguintes formas:
```
a = 3.14159
b = 2.71828
print("a vale %.2f e b vale %.3f" % (a, b))
print("a vale {:.2f} e b vale {:.3f}".format(a, b))
```
Em Java, é possível formatar saídas das seguintes formas:
```
double a = 3.14159;
double b = 2.71828;
System.out.printf("a vale %.2f e b vale %.3f\n", a, b);
System.out.println(String.format("a vale %.2f e b vale %.3f", a, b));
```

Exemplo 1:
Entradas:
```
1
2
3
```
Saídas:
```
Sem Solucao real!
Delta = -8.00
```

Exemplo 2:
Entradas:
```
4
-4
1
```
Saídas:
```
x = 0.50
```
Exemplo 3:
Entradas:
```
2
5
-4
```
Saídas:
```
x1 = -3.14
x2 = 0.64
```

_Exercício elaborado por Gabriel Ângelo Sembenelli (2022)._
