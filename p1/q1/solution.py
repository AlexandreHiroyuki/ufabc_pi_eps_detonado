def lua(m1, m2):
    if ((m1 >= 0 and m1 <= 2) and (m2 >= 0 and m2 <= 2)):
        return print("Nova")
    elif ((m1 >= 97 and m1 <= 100) and (m2 >= 97 and m2 <= 100)):
        return print("Cheia")

    if (m1 < m2):
        return print("Crescente")
    else:
        return print("Minguante")

# Código para testar
print(lua(0, 2))
print(lua(2, 3))
print(lua(99, 97))
print(lua(97, 94))