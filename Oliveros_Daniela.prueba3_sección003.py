import csv
lista=[]
def sep():
    print("")
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
    print("")
def menu():
    print("-.-.-.-.-MENÚ-.-.-.-.-")
    print("")
    print("1.-Agregar plan")
    print("2.-Listar planes")
    print("3.-Eliminar plan por id")
    print("4.-Generar bbdd")
    print("5.-Cargar bbdd")
    print("6.-Estadisticas")
    print("0.-Salir")
    print("")
def estadistica(l):
    acum=0
    mayor=-100
    for x in l:
        acum=acum+int(x[1])
        if int(x[1])>mayor:
            mayor=int(x[1])
    promedio=acum/len(l)
    print(f"la efectividad promedio es: {promedio}")
    print(f"La efectividad más alta es: {mayor}")
    
while (True):
    menu()
    op=int(input("Ingrese una opción: \n"))
    if op==1:
        sep()
        lista_chica=[]
        por=False
        print("-.-.-.-.-AGREGAR MENU-.-.-.-.-")
        print("")
        id=int(input("Ingrese id: \n"))
        efectividad=int(input("Ingrese porcentaje de efectividad: \n"))
        if efectividad>=0 and efectividad<=100:
            por=True
            print("efectividad correcta...")
        else:
            por=False
            print("efectividad debe ser entre 0 y 100, reingrese...")
        if por==True:
            if efectividad>=0 and efectividad<=25:
                categoria=("Chiste")
            elif efectividad>=26 and efectividad<=50:
                categoria=("Anécdota")
            elif efectividad>=51 and efectividad<=75:
                categoria=("Peligro")
            elif efectividad>=76 and efectividad<=99:
                categoria=("atención")
            elif efectividad==100:
                categoria=("Esclavitud")
            else:
                categoria=("no tiene categoria")
            lista_chica=[id,efectividad,categoria]
            lista.append(lista_chica)
            print ("agregado correctamente...")
    elif op==2:
        sep()
        for x in lista:
            print(f"id: {x[0]} efectividad: {x[1]} categoria: {x[2]}")
    elif op==3:
        sep()
        print("-.-.-.-.-ELIMINAR PLAN-.-.-.-.-")
        print("")
        eliminar=int(input("Ingrese el id del plan que desea eliminar: \n"))
        for x in lista:
            if int(x[0])==eliminar:
                print ("usted eliminará: ")
                print(f"id: {x[0]} efectividad: {x[1]} categoria: {x[2]}")
                pregunta=input("Esta segura que desea eliminar: (si/no) \n").lower()
                if pregunta=="si":
                    lista.remove(x)
                    print("Eliminado correctamente!")
                else:
                    print("No se ha eliminado el plan...")
    elif op==4:
        sep()
        print("-.-.-.-.-GENERAR CSV-.-.-.-.-")
        print("")
        with open('plan_csv.csv','w',newline='') as plan_csv:
            escribir_csv=csv.writer(plan_csv)
            escribir_csv.writerow(['id','efectividad','categoria'])
            escribir_csv.writerows(lista)
        print("")
        print("Archivo creado correctamente...")
    elif op==5:
        sep()
        lista.clear()
        print("-.-.-.-.-CARGAR CSV-.-.-.-.-")
        print("")
        with open('plan_csv.csv','r',newline='') as plan_csv:
            lector_csv=csv.reader(plan_csv)
            for x in lector_csv:
                print(x)
                lista.append(x)
            lista.pop(0)
    elif op==6:
        sep()
        print("-.-.-.-.-ESTADISTICAS-.-.-.-.-")
        print("")
        estadistica(lista)
    elif op==7:
        sep()
        print("Adios....")
        break
    else:
        sep()
        print("opcion no valida, ingrese una opcion del menú...")