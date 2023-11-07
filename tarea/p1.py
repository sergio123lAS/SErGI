def separar(s=str):
    l=[[],[]]
    for x in s:
        if x==" ":
            pass
        else:
            if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
                l[0].append(x)
            else:
                l[1].append(x)
    return l

def v_repeticiones(a=list):
    n_lista=[]
    if len(a)==0:
        return n_lista
    else:
        n_lista.append(a[0])
        for x in a:
            if x in n_lista:
                pass
            else:
                n_lista.append(x)
        return n_lista

while True:
    a=input("Ingrese su texto: ")
    if a=="-1":
        break
    else:
        lista=separar(a)
        vocales=lista[0]
        letras=lista[1]
        #print(vocales)
        #print(letras)
        print(v_repeticiones(vocales))
        print(v_repeticiones(letras))
