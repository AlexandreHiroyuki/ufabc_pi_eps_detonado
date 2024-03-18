## Questão 1

As fases da Lua referem-se à mudança aparente da porção visível iluminada do satélite devido a sua variação da posição em relação à Terra e ao Sol. O ciclo completo, denominado lunação, leva pouco mais de 29 dias para se completar. Nesse período, a lua passa da fase nova, quando a sua porção iluminada visível passa a aumentar gradualmente até que, duas semanas depois ocorre a lua cheia e, cerca de duas semanas seguintes, volta a diminuir e o satélite entra novamente na fase nova.

Foi convencionado que, em duas avaliações realizadas em duas noites consecutivas é possível informar em qual fase a lua se encontra:

- se a porção visível da lua no momento estiver entre 0% e 2%, é lua nova;
- se estiver entre 3% e 96%, é lua crescente;
- se estiver entre 97% e 100%, é lua cheia;
- se estiver entre 96% e 3% (diminuindo), é lua minguante.

Faça uma função lua(m1, m2), onde m1 e m2 são inteiros no intervalo [0,100]. m1 é a medida de porção visível da Lua na primeira noite; m2 é a medida na segunda noite.

A função deve imprimir na tela uma das seguinte palavras: Nova, Cheia, Crescente ou Minguante, de acordo com a convenção explicada.

Exemplos:
```
lua(0, 2)
Nova

lua(2, 3)
Crescente

lua(99, 97)
Cheia

lua(97, 94)
Minguante
```
