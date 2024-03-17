# Seu programa irá receber o primeiro termo da progressão, a1, a razão da progressão, r, e o número de termos, n
a1 = int(input())
r = int(input())
n = int(input())

# Então, calcule e imprima a soma dos termos de a1 até an
an = a1 + (n-1)*r

s = (n*(a1 + an))/2

print(s)
