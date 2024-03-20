## EP4_4(função) - Shift

Implemente:

1. Uma função/método (inserir) que leia (Scanner/input) 10 valores inteiros e insira esses elementos em um vetor (a função/método retorna (return) esse vetor preenchido com 10 inteiros);
2. Uma segunda função/método (imprimir) que receba o vetor criado em (a) e imprima os seus elementos (inclua um caractere espaço entre cada elemento impresso; quebre uma linha após a impressão do último elemento);
3. Uma terceira função/método (shift) que receba o vetor criado em (a) e faça um shift para a direita em cada elemento inserido no vetor. Além disso, o vetor  deve ser circular, ou seja, o valor da última posição deve ser o valor da primeira. Por exemplo,

```
Vetor original: [2, 4, 1, 5, 2, 18, 9, 3, 5, 10]
Vetor após shift: [10, 2, 4, 1, 5, 2, 18, 9, 3, 5] 
```

Funções/métodos a serem implementados:

Python (o arquivo submetido deve ter a extensão .py):
```python
def inserir():
    #código da função

def imprimir(v):
    #código da função

def shift(v):
    #código da função
```

Importante: submeta apenas as três funções/métodos.

Neste exercício, não é permitido utilizar:
- Em Python: as funções de listas: del, append, extend, insert, remove, pop.

Formato do caso de teste: esse é o formato dos casos de teste que aparecem ao avaliar a atividade.

Entrada:
```
10 valores inteiros (elementos do vetor)
```
Saída:
```
Elementos do vetor lido
Elementos do vetor após o shift
```

O programa que está fixo no Moodle realizará as seguintes chamadas (utilizando as funções/métodos submetidas nesta atividade):
Python:
```python
v = inserir()
imprimir(v)
shift(v)
imprimir(v)
```

_Exercício adaptado de Prof. Wagner Tanaka Botelho - Processamento da Informação 2022_
