alumnos=["Ana","Luis","Pedro","Marta","Nerea","Pablo"]
def lista_nueva(a=list):
    n_lista=[]
    for x in a:
        n_lista.append(x[0])
    return n_lista
print("respuesta:",end=" ")
print(lista_nueva(alumnos))
