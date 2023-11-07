datos=[[40,35,29],
       [39,32,28],
       [26,33,27],
       [23,30,26],
       [22,31,27]]

def total_medalla(l=list,a=int):
    sum=0
    c=0
    for x in l:
        sum+=x[a-1]
        c+=1
    return sum

oro = total_medalla(datos,1)
plata = total_medalla(datos,2)
bronce = total_medalla(datos,3)
print(f"Oro: {oro}\nBronce: {plata}\nPlata: {bronce}")
print(f"La medalla más repartida fue: {max(oro,plata,bronce)}")

