# Entrada: 3 discos de um pedido
def obter_prazo_entrega(disco1, disco2, disco3):
    # Note: os casos únicos em que todos os discos são iguais ou todos são diferentes são tratados antes pois são exceções
    # já que em todos os outros casos intermediários, o prazo de entrega é 15 dias.
    if((disco1 == disco2) and (disco2 == disco3) and (disco3 == disco1)):
        return 5
    if((disco1 != disco2) and (disco2 != disco3) and (disco3 != disco1)):
        return 30
    return 15
