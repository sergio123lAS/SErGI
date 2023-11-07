lima = {"22/05/2019":17 , "23/05/2019":17 , "24/05/2019":19 ,
"25/05/2019":23 , "26/05/2019":20 , "27/05/2019":18 ,
"28/05/2019":20 , "29/05/2019":19 , "30/05/2019":22 ,
"31/05/2019":19 , "01/06/2019":20 , "02/06/2019":19 ,
"03/06/2019":17 , "04/06/2019":16 , "05/06/2019":18 ,
"06/06/2019":21 , "07/06/2019":19 , "08/06/2019":15 ,
"09/06/2019":17 , "10/06/2019":20 , "11/06/2019":15 ,
"12/06/2019":22 , "13/06/2019":14 , "14/06/2019":16 }

def temperaturas(n=int):
    for x in range(n):
        fecha=input("Ingrese la fecha: ")
        temperatura=int(input("Ingrese la temperatura: "))
        lima[fecha]=temperatura
    maximo=max(lima.values())
    minimo=min(lima.values())
    for k,v in lima.items():
        if v==maximo:
            clave_max=k
            break
    for k,v in lima.items():
        if v==minimo:
            clave_min=k
            break
    print(f"La fecha donde la temperatura fue más alta fue: {clave_max}")
    print(f"La fecha donde la temperatura fue más baja fue: {clave_min}")

while True:
    a=int(input("Ingrese la cantidad de datos a cargar: "))
    print(temperaturas(a))
