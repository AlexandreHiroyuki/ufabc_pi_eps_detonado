## EP5_1 - Busca elemento

Faça um programa que busque um número específico dentro de uma matriz.
O tamanho da matriz será definido pelo usuário, que vai entrar com a quantidade de linhas e depois com a quantidade de colunas. Após isso, o usuário vai inserir cada um dos elementos da matriz e, ao final, vai inserir qual é o número a ser buscado (é garantido que o número buscado aparece no máximo uma vez na matriz). Ao final, o programa deverá imprimir a posição do número buscado, ou seja, o número da linha e o número da coluna em que se encontra (note que o índice [0][0] no programa corresponde à posição da linha=1 e coluna=1). Caso o número não exista na matriz, imprima apenas o número -1.

Entradas:
- Número de linhas da matriz (inteiro > 0)
- Número de colunas da matriz (inteiro > 0)
- Elementos que compõem a matriz (inteiros)
- Número a ser buscado na matriz (inteiro)

Saídas:
- Posição do número buscado (ou -1 caso não exista)

### Exemplo 1:
Entradas:
```
2
3
1
2
3
4
5
6
4
```
Saídas:
```
2 1
```

### Exemplo 2:
Entradas:
```
2
3
1
2
3
4
5
6
8
```
Saídas:
```
-1
```
