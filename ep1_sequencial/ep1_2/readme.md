## EP1_2 - Formatação

Exercite a formatação de saídas. Seu programa irá receber 3 valores, então deverá imprimir o primeiro formatado com nenhuma casa decimal, o segundo com duas casas e o terceiro com três casas, seguindo o mesmo estilo da saída de exemplo.

Entradas:
3 números (observe que os dois últimos números são do tipo float)
Saídas:
Primeiro número com 0 casas decimais
Segundo número com 2 casas decimais
Terceiro número com 3 casas decimais


Exemplo (observe que a saída não deve possuir acentos):
Entradas:
```
2
1.41421
3.14159
```
Saídas:
```
Primeiro numero = 2
1.41 eh o segundo numero
Finalmente 3.142 eh o terceiro numero
```

Observações:
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
_Exercício elaborado por Gabriel Ângelo Sembenelli (2022)._
