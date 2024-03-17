# Escreva um programa que leia os valores VP, FN, FP e VN
vp = int(input())
fn = int(input())
fp = int(input())
vn = int(input())

# Então imprima o valor das métricas acurácia, precisão e sensibilidade
print(f"{((vp+vn)/(vp+vn+fp+fn)):.2f}")
print(f"{(vp/(vp+fp)):.2f}")
print(f"{(vp/(vp+fn)):.2f}")
