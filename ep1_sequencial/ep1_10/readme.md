## EP1_10 - Desempenho preditivo

A área de Aprendizado de Máquina tem crescido bastante nos últimos anos. Uma tarefa importante nesse contexto é a classificação. Algoritmos de classificação são capazes de aprender a partir de experiência prévia (e.g. dados históricos). Os classificadores podem então realizar predições para novos dados. Por exemplo, um algoritmo de classificação pode aprender a partir de e-mails antigos e se eles foram classificados como spam ou não spam pelos usuários. Depois, o classificador treinado poderá predizer se novos e-mails são spam ou não. Esse também é um exemplo de classificação binária, em que há duas classes possíveis: spam ou não spam.

O desempenho de classificadores binários pode ser medido utilizando uma série de métricas. Nesse contexto, existe um conceito conhecido como matriz de confusão. Essa matriz é preenchida com a contagem de predições corretas e incorretas realizadas pelo classificador. A matriz de confusão tem o seguinte formato:

> Classe predita
> Positiva	Negativa
> Classe verdadeira	Positiva	VP	FN
> Negativa	FP	VN

Nessa matriz, positiva e negativa representam as duas classes. No caso do spam, a classe positiva poderia representar classificar um e-mail como spam e a negativa classificar como não spam. Os valores na matriz são:

- VP: número de vezes que exemplos positivos foram classificados corretamente como positivos.
- FN: número de vezes que exemplos positivos foram classificados de forma incorreta como negativos.
- FP: número de vezes que exemplos negativos foram classificados de forma incorreta como positivos.
- VN: número de vezes que exemplos negativos foram classificados corretamente como negativos.

Exemplo de matriz preenchida:

> Classe predita
> Positiva	Negativa
> Classe verdadeira	Positiva	40	10
> Negativa	15	35

Com base nos valores na matriz de confusão, podem ser calculadas métricas para avaliação de desempenho. Algumas dessas métricas são apresentadas a seguir:

- Acurácia = VP+VN / VP+VN+FP+FN
- Precisão = VP / VP+FP
- Sensibilidade = VP / VP+FN

No exemplo apresentado:
- Acurácia = (40 + 35) / (40 + 35 + 15 + 10) = 0,75
- Precisão = 40 / (40 + 15) = 0,73
- Sensibilidade = 40 / (40 + 10) = 0,80

Escreva um programa que leia os valores VP, FN, FP e VN e então imprima o valor das métricas acurácia, precisão e sensibilidade.

Entrada
```
Valor de VP (inteiro)
Valor de FN (inteiro)
Valor de FP (inteiro)
Valor de VN (inteiro)
```
Saída
```
Acurácia
Precisão
Sensibilidade
```

Observação: imprima todos os valores com **duas casas** decimais após a vírgula
