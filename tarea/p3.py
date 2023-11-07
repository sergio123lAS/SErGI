import random
def n_random():
    l=[]
    for x in range(10):
        a=random.uniform(10,20)
        a=round(a,2)
        l.append(a)
    return l

print("respuesta:",end=" ")
print(n_random())