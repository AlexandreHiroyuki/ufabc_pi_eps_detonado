## EP2_10 - Autonomia do avião

Um avião de carga possui uma autonomia que depende do peso da carga sendo transportada:

> Carga	Autonomia (em km) </br>
> até 50000kg | 18000 km </br>
> 50001kg a 200000kg | 9000 km </br>
> 200001 a 250000kg | 3000 km </br>

A capacidade máxima desse avião é 250000kg. Além disso, dependendo das condições de voo, esse avião pode ter uma autonomia até 10% maior.

Escreva um programa que recebe o peso total da carga, as coordenadas de partida (Ax, Ay) as coordenadas do destino (Bx, By) e então imprima a distância e também se o avião tem autonomia para chegar ao destino. Imprima:
```
"SIM" (se o avião tem autonomia para chegar no destino com a carga)
"TALVEZ" (se o avião tem autonomia para chegar no destino com a carga, mas considerando o adicional de 10% que depende de condições de voo)
"NAO" (se o avião não tem autonomia para chegar no destino com a carga, mesmo considerando o adicional de 10% que depende de condições de voo)
```
Para calcular a distância a ser percorrida (em km), considere a distância Euclidiana em linha reta entre os pontos (Ax,Ay) e (Bx,By). Veja o exercício EP1_4 - Distância entre pontos para detalhes sobre como calcular a distância entre dois pontos.

Considere que o avião apenas é usado para cargas inferiores a 250000kg e, portanto, não é necessário prever o caso que a carga é superior a sua capacidade máxima.

Entrada
```
Carga (em kg)
Ax
Ay
Bx
By
```
Saída
```
Distância (imprima o valor com duas casas decimais após a vírgula)
SIM/TALVEZ/NAO (de acordo com os critérios apresentados no enunciado)
```
