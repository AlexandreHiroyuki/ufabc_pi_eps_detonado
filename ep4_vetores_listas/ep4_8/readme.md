## EP4_8 - Vetor crescente

Escreva um programa que leia um vetor de inteiros com n elementos. Depois verifique se o vetor está ordenado em ordem crescente.

Observação: após a leitura do valor n, os elementos do vetor estão todos dispostos em apenas uma linha. Por exemplo:
```
3
3 1 2
```

Dica (Python): para ler elementos em uma mesma linha, pode ser usado o método split após a leitura. Veja exemplo a seguir:
```python
n = int(input())
v = [0] * n

itens_linha = input().split(" ")
for i in range(n):
    v[i] = int(itens_linha[i])
```

Entrada:
- Um valor n (0 <= n <= 50);
- n inteiros

Saída:
- Imprima "SIM" se o vetor estiver ordenado e "NAO" caso contrário (observe que não há um til no NAO)
