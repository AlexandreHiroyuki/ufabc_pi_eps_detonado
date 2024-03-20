## EP5_9 - Matriz com múltiplos de 10

Escreva um programa que leia uma matriz e então verifique se a matriz possui somente múltiplos de 10 e se cada uma das linhas está ordenada (seja em ordem crescente ou decrescente).

Observação: após a leitura das dimensões da matriz, os elementos de cada linha da matriz estão dispostos linha por linha. Por exemplo (as duas primeiras linhas são as dimensões da matriz: número de linhas (2) e número de colunas(3)):
```
2
3
5 6 2
7 2 1
```

_Dica para Python ou Java: a leitura dos elementos da matriz da forma descrita aqui pode ser realizada com uma estratégia similar àquela apresentada no enunciado dos dois primeiros exercícios sobre matrizes (EP5_1 e EP5_2)._

Entrada:
- L (número de linhas)
- C (número de colunas)
- Elementos da matriz

Exemplo:
```
3
4
40 30 20 10
10 20 30 40
20 50 80 90
```

Saída:
- Imprima "SIM" se a matriz atende ao critério e "NAO" caso contrário (observe que não há um til no NAO)


Exemplo:
```
SIM
```

Neste exemplo, a saída foi sim, pois todos os valores são múltiplos de 10 e todas as linhas estão ordenadas (a primeira linha em ordem decrescente, e as outras duas linhas em ordem crescente)
