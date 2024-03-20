def intercalar(v1, v2):
    v3 = [None] * 10
    for i in range(5):
        v3[i*2] = v1[i]
        v3[(i*2)+1] = v2[i]
    return v3
