def registrar_dep():
    l=[]
    lista_numeros=["0","1","2","3","4","5","6","7","8","9"]
    direccion=input("Direccion: ")
    l.append(direccion)
    distrito=input("Distrito: ")
    l.append(distrito)
    contador1=0
    piso=input("Piso: ")
    for x in piso:
        for y in lista_numeros:
            if x==y:
                contador1+=1 
    while contador1!=len(piso):
        contador1=0
        piso=input("Piso: ")
        for x in piso:
            for y in lista_numeros:
                if x==y:
                    contador1+=1 
    l.append(piso)
    contador2=0
    n_habitaciones=input("Numero de habitaciones: ")
    for x in n_habitaciones:
        for y in lista_numeros:
            if x==y:
                contador2+=1 
    while contador2!=len(n_habitaciones):
        contador2=0
        n_habitaciones=input("Numero de habitaciones: ")
        for x in n_habitaciones:
            for y in lista_numeros:
                if x==y:
                    contador2+=1 
    l.append(n_habitaciones)    
    contador3=0
    area=input("Area m2: ")
    for x in area:
        for y in lista_numeros:
            if x==y:
                contador3+=1
    while contador3!=len(area):
        contador3=0
        area=input("Area m2: ")
        for x in area:
            for y in lista_numeros:
                if x==y:
                    contador3+=1             
    l.append(area)    
    contador4=0
    precio=input("Precio S/: ")
    for x in precio:
        for y in lista_numeros:
            if x==y:
                contador4+=1
    while contador4!=len(precio):
        contador4=0
        precio=input("Precio S/: ")
        for x in precio:
            for y in lista_numeros:
                if x==y:
                    contador4+=1
    l.append(precio)
    return l

def dep_disponibles(iteraciones=int,l_save=list):
    print("Departamentos disponibles")
    print("\tDistrito \tN.Hab \tPiso \tArea \tPrecio(S/)")
    for x in range(iteraciones):
        print(f"{x+1}\t{l_save[x][1]} \t{l_save[x][2]} \t{l_save[x][3]} \t{l_save[x][4]} \t{l_save[x][5]}")
    print("Seleccione")
    print("0. Regresar Menu Principal")
    print("1. Comprar Departamento")
    opcion=input("Opcion: ")
    while opcion!="0" and opcion!="1":
        opcion=input("Opcion: ")
    return opcion        

l_save=[]
l_buy=[]
l_series=[]
iteraciones=0
iteraciones_finales=0
while True:
    print("INMOBILIARIA")
    print("1.Registar Departamentos")
    print("2.Departamentos disponibles")
    print("3.Departamentos vendidos")
    opcion=input("opcion: ")
    while opcion!= "1" and opcion != "2" and opcion != "3" and opcion !="salir":
        opcion = input("opcion: ")
    
    if opcion == "1":
        registros = registrar_dep()
        l_save.append(registros)
        #print(f"l_save={len(l_save)}")
        regresar=input("0. Regresar Menu Principal ")
        while regresar!="0":
            regresar=input("0. Regresar Menu Principal ")
        iteraciones+=1

    if opcion == "2":
        if iteraciones==0:
            print("No se han registrado departamentos")
        else:
            eleccion=dep_disponibles(iteraciones,l_save)
            if eleccion=="0":
                print()
            if eleccion=="1":
                dato_validacion=0
                n_serie=input("N. Serie: ")
                for x in range(iteraciones): # Iteracion importante para la validacion del numero
                    if n_serie==str(x+1):
                        dato_validacion+=1
                if dato_validacion==0:
                    while dato_validacion==0:
                        n_serie=input("N. Serie: ")
                        for x in range(iteraciones):
                            if n_serie==str(x+1):
                                dato_validacion+=1
                n_serie=int(n_serie)
                contador=0
                for x in l_series:
                    if n_serie==x:
                        contador+=1
                if contador!=0:
                    print("Ese departamento ha sido vendido")
                else:
                    print("ID \tDistrito \tN.Hab \tPiso \tArea \tPrecio(S/)")
                    print(f"{n_serie} \t{l_save[n_serie-1][1]} \t{l_save[n_serie-1][2]} \t{l_save[n_serie-1][3]} \t{l_save[n_serie-1][4]} \t{l_save[n_serie-1][5]}")
                    nombre=input("Nombre: ")
                    dni=input("DNI: ")
                    lista_numeros=["0","1","2","3","4","5","6","7","8","9"]
                    comprobacion_dni=0
                    for x in dni:
                        for y in lista_numeros:
                            if x==y:
                                comprobacion_dni+=1
                        if x=="-":
                            comprobacion_dni-=1
                    while comprobacion_dni!=8 or dni=="00000000":
                        dni=input("DNI: ")
                        comprobacion_dni=0
                        for x in dni:
                            for y in lista_numeros:
                                if x==y:
                                    comprobacion_dni+=1
                            if x=="-":
                                comprobacion_dni-=1
                    email=input("email: ")
                    contador_email=0
                    for x in email:
                        if x=="@":
                            contador_email+=1
                    while contador_email!=1:
                        email=input("email: ")
                        contador_email=0
                        for x in email:
                            if x=="@":
                                contador_email+=1
                    print("Está apunto de comprar el departamento")
                    print("1. Confirmar")
                    print("2. Cancelar")
                    seguridad=input("Decisión: ")
                    while seguridad!="1" and seguridad!="2":
                        seguridad=input("Decisión: ")
                    if seguridad=="1":
                        print("COMPRA REGISTRADA")
                        l_buy.append(l_save[n_serie-1]) #para agregar a la matriz
                        l_series.append(n_serie) #para guardar el numero de serie
                        regresar=input("0. Regresar Menu Principal ")
                        while regresar!="0":
                            regresar=input("0. Regresar Menu Principal ")
                        iteraciones_finales+=1
                    if seguridad=="2":
                        print("COMPRA CANCELADA")
    if opcion=="3":
        if iteraciones==0:
            print("No se han registrado compras")
        else:
            suma=0
            print("\tDistrito \tN.Hab \tPiso \tArea \tPrecio(S/)")
            for x in range(iteraciones_finales):
                print(f"{l_series[x]} \t{l_buy[x][1]} \t{l_buy[x][2]} \t{l_buy[x][3]} \t{l_buy[x][4]} \t{l_buy[x][5]}")
                suma+=int(l_buy[x][5])
            print(f"Total: {suma}")

    if opcion=="salir":
        break
    print()



