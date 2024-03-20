## EP4_2 - Duplas

Escreva um programa que leia um inteiro N positivo, que irá representar o tamanho de um vetor V. Em seguida, leia os valores de cada elemento desse vetor. Ao final, verifique se é um vetor onde todos os elementos vêm em duplas.

Uma dupla é formada quando há dois elementos iguais e em posições consecutivas. Por exemplo, o vetor [1,1,2,2,3,3] é um vetor de duplas, enquanto [1,1,2,2,2] não é um vetor de duplas, pois os quatro primeiros elementos formam duplas, mas não restam elementos para o último 2 formar dupla. O vetor [1,2,1,2,3,3] também não é um vetor de duplas, pois 1 e 2 não formam uma dupla.

Saídas possíveis (não inclua o til na impressao de "Nao"):

- Eh um vetor de duplas!
- Nao eh um vetor de duplas!

Entradas:
- Tamanho _N_ do vetor (inteiro > 1)
- Elementos _ai_ que compõem o vetor (inteiros)

Saída:
- Formam duplas ou não


Exemplo 1:
Entradas:
```
6
1
1
2
2
3
3
```
Saídas:
```
Eh um vetor de duplas!
```

Exemplo 2:
Entradas:
```
5
1
1
2
2
2
```
Saídas:
```
Nao eh um vetor de duplas!
```

Exercício adaptado de Gabriel Ângelo Sembenelli (2022).
