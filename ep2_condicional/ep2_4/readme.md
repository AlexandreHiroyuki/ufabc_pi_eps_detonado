## EP2_4(função) - Fábrica de discos voadores

Uma fábrica de discos voadores produz diversos modelos que são entregues para clientes na galáxia. Nesta fábrica, os discos voadores são vendidos em pacotes com três unidades. Portanto, não é possível comprar apenas um disco voador nesta fábrica. Ao solicitar os três discos voadores, devem ser especificados os modelos dos discos. Dependendo dos modelos solicitados, o prazo de entrega pode ser diferente:

Quando os três discos voadores solicitados são do mesmo modelo (tem o mesmo código), o prazo de entrega é de 5 dias;
Quando dois discos voadores são do mesmo modelo (tem o mesmo código) e o outro é de outro modelo (outro código), o prazo de entrega é de 15 dias;
Quando os três discos voadores são de modelos diferentes (três códigos diferentes), o prazo de entrega é de 30 dias.


O gerente da fábrica escreveu um programa para calcular o prazo de entrega dependendo dos modelos solicitados pelo cliente, mas faltou implementar a função/método para calcular o prazo de entrega:

Python:
```
def obter_prazo_entrega(disco1, disco2, disco3):
    #codigo da funcao aqui
    
d1 = int(input())
d2 = int(input())
d3 = int(input())
prazo_entrega = obter_prazo_entrega(d1, d2, d3)
print("Disco1 =", d1)
print("Disco2 =", d2)
print("Disco3 =", d3)
print("Prazo de entrega =", prazo_entrega)
```
Escreva a função/método para obter o prazo de entrega. Essa função/método recebe os códigos de três discos voadores e deve retornar o prazo de entrega dependendo dos códigos dos discos voadores solicitados.



Python (o arquivo submetido deve ter a extensão .py):
```
def obter_prazo_entrega(disco1, disco2, disco3):
    #codigo da funcao
```

Importante: submeta apenas a função/método e não realize leitura de dados (input/Scanner) ou impressão de dados (print/System.out).

Formato do caso de teste: esse é o formato dos casos de teste que aparecem ao avaliar a atividade; não inclua impressão de dados no código, essa impressão é feita automaticamente pelo sistema de correção de acordo com o retorno da função submetida.

Entrada:
```
Código do modelo do disco voador 1
Código do modelo do disco voador 2
Código do modelo do disco voador 3
```
Saída:
```
Códigos dos modelos dos discos voadores
Valor retornado pela função/método
```
