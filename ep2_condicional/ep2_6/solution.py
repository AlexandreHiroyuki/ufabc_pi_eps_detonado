# Entrada: 2 datas
def comparar_datas(d1, m1, a1, d2, m2, a2):
    # Note: as datas são comparadas em ordem decrescente de grandeza, ou seja, ano, mês e dia.
    # Isso é feito pois caso alguma das condições seja satisfeita para uma grandeza, não é necessário comparar as menores.
    # Note: as condicionais não usam elif pois caso uma das condições seja satisfeita, a função retorna o valor correspondente.
    # Sempre que uma função retorna um valor, ela para imediatamente de executar.
    if (a1 < a2):
        return -1
    if (a1 > a2):
        return 1

    if (m1 < m2):
        return -1
    if (m1 > m2):
        return 1

    if (d1 < d2):
        return -1
    if (d1 > d2):
        return 1

    return 0
