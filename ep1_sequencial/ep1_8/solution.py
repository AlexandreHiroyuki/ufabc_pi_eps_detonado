# O input receberá um número inteiro de 4 dígitos
# Para poder interagir com cada caractere do número, você deve transformar o número em uma string
number = str(input())
result = ""

# Um determinado método para encriptar números de 4 dígitos consiste em adicionar 1 em cada dígito do número
for e in number:
    x = 0
    # A condição abaixo é para quando o dígito for 9, pois 9 + 1 = 10, e o número deverá voltar ao digito 0
    if(int(e)+1 < 10):
        x = int(e)+1
    
    print(x, end="")
