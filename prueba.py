'''ESTE ALGORITMO GESTIONA UNA EMPRESA DE PINTURAS
'''
import pathlib,csv,json
pinturas=[]
menu=["Ver listado de pinturas","Buscar pintura","Agregar pintura","Eliminar pintura","Exportar pinturas"]
while True:
    for indice,valor in enumerate(menu):
        print(f"{indice+1}.{valor}")
    ans=input("Indique la opción que desea:\n")
    if ans=="1":
        print("###VER LISTADO DE PINTURAS###\n")
        if pinturas==[]:
            print("NO HAY PINTURAS PARA MOSTRAR, POR FAVOR INGRESE UNA:\n")
        else:
            for x in pinturas:
                print("NOMBRE:",x["nombre"])
                print("TIPO:",x["tipo"])
                print("PRECIO:",x["precio"])
                print("STOCK:",x["stock"])
                print("CODIGO:",x["codigo"])
                print()
    elif ans=="2":
        print("###BUSCAR PINTURA###\n")
        if pinturas==[]:
            print("NO HAY NINGUNA PINTURA INGRESADA PARA BUSCAR, INGRESE UNA\n")
        else:
            ans=input("Ingrese como desea buscar la pintura:\n1.Código\n2.Nombre\n")
            if ans=="1":
                try:
                    buscar_code=int(input("Ingrese el código de la pintura que desea buscar:\n"))
                except ValueError:
                    print("Porfavor ingrese DIGITOS, intentelo de nuevo!\n")
                    continue
                for pintura in pinturas:
                    if pintura["codigo"]==buscar_code:
                        print()
                        print(f"Se han encontrado coincidencias para el codigo {buscar_code}\n")
                        print("NOMBRE:",pintura["nombre"])
                        print("TIPO:",pintura["tipo"])
                        print("PRECIO:",pintura["precio"])
                        print("STOCK:",pintura["stock"])
                        print("CODIGO:",pintura["codigo"])
                        print()
            elif ans=="2":
                buscarname=input("Ingrese el NOMBRE de la pintura que desea buscar:\n").lower()
                for pintura in pinturas:
                    if pintura["nombre"]==buscarname:
                        print()
                        print(f"Se han encontrado coincidencias para la búsqueda {buscarname}.\nEstos son sus datos:\n")
                        print("NOMBRE:",pintura["nombre"])
                        print("TIPO:",pintura["tipo"])
                        print("PRECIO:",pintura["precio"])
                        print("STOCK:",pintura["stock"])
                        print("CODIGO:",pintura["codigo"])
                        print()
    elif ans=="3":
        print("###AGRERAR PINTURA###")
        nombre=input("Ingrese el nombre del color:\n").lower()
        ans=input("Ingrese el tipo de pintura que tiene:\n1.Acrilico\n2.Látex\n")
        if ans=="1":
            tipo="Acrilico"
            print("Se ha agregado el tipo de pintura ACRILICO con éxito!\n")
        elif ans=="2":
            tipo="Latex"    
            print("Se ha agregado el tipo de pintura LATEX con éxito!\n")
        else:
            print("Ingrese una opción correcta!\n")
            continue
        try:    
            precio=int(input("Ingese el precio de la pintura:\n"))
        except ValueError:
            print("Porfavor ingrese un valor númerico!\n")
            continue
        try:
            stock=int(input("Ingrese el total de STOCK de la pintura:\n"))
        except ValueError:
            print("Porfavor ingrese un valor númerico!. Intentelo de nuevo\n")
            continue
        if pinturas==[]:
            codigo=380560
            str(codigo)
            pintura={"nombre":nombre,"tipo":tipo,"precio":precio,"stock":stock,"codigo":codigo}
            print(f"Se le ha entregado el codigo por default de {codigo}")
            pinturas.append(pintura)
            print("Se ha agredado la pintura con éxito!\n")
        else:
            codigo +=1
            str(codigo)
            pintura={"nombre":nombre,"tipo":tipo,"precio":precio,"stock":stock,"codigo":codigo}
            print(f"Se le ha entregado el codigo por default de {codigo}")
            pinturas.append(pintura)
            print("Se ha agredado la pintura con éxito!\n")
    elif ans=="4":
        print("###ELIMINAR PINTURA###")
        if pinturas==[]:
            print("NO HAY NINGUNA PINTURA INGRESADA PARA ELIMINAR\n")
        else:
            try:
                borrar=int(input("Ingrese el CODIGO de la pintura que desea eliminar:\n"))
                for pintura in pinturas:
                    if pintura["codigo"]==borrar:
                        pinturas.remove(pintura)
                        print("Se la eliminado la pintura con éxito!\n")
            except ValueError:
                print("Porfavor ingrese un codigo NUMERICO, intentelo de nuevo!\n")
                continue
    elif ans=="5":
        print("###EXPORTAR PINTURAS###")
        archivo_csv="mandarina.csv"
        with open("mandarina.csv",mode="w",newline="") as archivo:
            escribir=csv.writer(archivo)
            escribir.writerows(pinturas)
            print("Se ha creado el archivo mandarina.csv con éxito!")
    else:
        print("Ingrese alguna opción válida!")