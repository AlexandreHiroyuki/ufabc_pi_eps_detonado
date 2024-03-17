## EP2_9 - Pedidos de discos voadores

Uma montadora de discos voadores possui fábricas em diversos planetas e faz entregas em diversas partes do universo. Essa empresa usa números de 6 dígitos para identificar a origem do disco, o destino do disco e o modelo, conforme formato a seguir:

OODDMM:
- OO: código do planeta de origem (onde o disco voador foi fabricado)
- DD: código do planeta de destino (onde o disco voador será entregue)
- MM: código do modelo

A empresa usa as seguintes tabelas com os códigos de planetas e modelos de discos voadores:

> Código | Planeta </br>
> 80 | Marte </br>
> 81 | Saturno </br>
> 90 | Netuno </br>
> 91 | HD21749b </br>

> Código | Modelo </br>
> 60	A6000 </br>
> 61	B7500 </br>
> 62	C9000 </br>

Portanto, o número 809162 será usado para um disco voador fabricado em Marte (código 80), entregue em HD21749b (código 91) e do modelo C9000 (código 62).

Escreva um programa que leia um número de 6 dígitos e então imprima o planeta de origem, o planeta de destino e o modelo.

Entrada
- Número de 6 dígitos

Saída
- Planeta de origem
- Planeta de destino
- Modelo do disco voador
