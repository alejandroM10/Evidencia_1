import random
import datetime
clientes={}
salas={}
reservaciones={}
salas={1:["1", "Alianz", "50"],
       2:["2", "Camp Nou", "80"],
       3:["3", "Bernabeu", "60"]}
       
# Menú general
print("RESERVACION DE SALAS")
print("[1]. Registrar la reservación de una sala")
print("[2]. Editar el nombre del evento de una reservación ya hecha")
print("[3]. Consultar las reservaciones existentes para una fecha especificas")
print("[4]. Registrar a un nuevo cliente")
print("[5]. Registrar una sala")
print("[6]. Salir")

while True:
    opcion=input("¿Que desea hacer?: ")
    # Validar que selecciono una opcion del menu correcta
    if (not opcion in "123456"):
        print("Opción no valida, ingresa una opcion del menú")
        continue

    if opcion=="1":# Opcion Registrar reservación
        # Generar clave
        Folio_reserva=str(random.randrange(0,1001))
        if reservaciones.get(Folio_reserva)==None:
            clave_cliente=input("Ingresa la clave del cliente: ")
            if (not clave_cliente in clientes.keys()):
                print("Cliente no registrado. Primero registrarse")
            else:
                # Nombrar reservación
                nombre_evento=input("Ingresa el nombre del evento: ")
                # Verificar fecha
                Fecha_actual=datetime.date.today()
                fecha_reservacion=input("Ingresa la fecha a reservar: ")
                Fecha_reserva=datetime.datetime.strptime(fecha_reservacion, "%d/%m/%Y" ).date()
                mes1=Fecha_reserva.month  
                mes2=Fecha_actual.month
                dias_aprox=Fecha_reserva.day - Fecha_actual.day
                if dias_aprox <= 2 and mes1 <= mes2:
                    print("La reservacion se tiene que hacer con 2 dias de anticipacion")
                else:
                    # Seleccionar el turno
                    print("Turnos: ")
                    print("[A]. Matutino")
                    print("[B]. Vespertino")
                    print("[C]. Nocturno")
                    turno=input("Ingrese el turno que desea reservar : ")
                    if turno.upper()=="A":
                        turno="Matutino"
                        print("Seleccionado")
                    elif turno.upper()=="B":
                        turno="Vespertino"
                        print("Seleccionado")
                    elif turno.upper()=="C": 
                        turno="Nocturno"
                        print("Seleccionado")
                    else:
                        print("Valor incorrecto. Intenta de nuevo")
                        continue
                    # Seleccionar sala
                    print("Salas: ")
                    print(list(salas.items()))
                    sala=input("Ingresa que sala a reservar: ")
                    
                    if [fecha_reservacion,turno,sala] in reservaciones.values():
                        print("Fecha ocupada")
                    else:
                        reservaciones.update({Folio_reserva:[Folio_reserva,nombre_cliente,nombre_evento,fecha_reservacion,turno,sala]})
                        print("Reservación agregada")  
                        regresar=input("Regresar al menú da enter")
                        if regresar=="":
                            continue             
        else:
            print("Folio encontrado. No se puede repetir")
    elif opcion=="2":
        Modificar=input("Ingresa el folio de la reservación: ")
        cambio=reservaciones.get(Modificar)
        if cambio==None:
            print("Reservación no encontrada")
        else:
            print("Datos Actuales:", {cambio[0]},{cambio[1]},{cambio[2]},{cambio[3]},{cambio[4]})
            nombre_nuevo=input("Ingresa el nuevo nombre: ")
            nombre_cliente=nombre_nuevo
            reservaciones.update(({Folio_reserva:[Folio_reserva,nombre_cliente,nombre_evento,fecha_reservacion,turno,sala]}))
    elif opcion=="3":
        while True:
            buscar_fecha=input("Ingresa la fecha para ver las reservaciones: ")
            buscar_fecha=datetime.datetime.strptime(buscar_fecha,"%d/%m/%Y").date()
            for Fecha in reservaciones.keys():
                for valores in reservaciones.values():
                    print("*"*80)
                    print("*"*20,f"Reporte de reservaciones para el dia {buscar_fecha}","*"*20)
                    print("*"*80)
                    print(reservaciones.values())
                    print("*"*50)
                    print("{:<15} {:<15} {:<15} {:<15}".format("Sala","Cliente","Evento","Turno"))
                    print("*"*80)
                    print(f"{valores[5]}","   "*4,{valores[1]},"   "*4,{valores[2]},"   "*4,{valores[4]})
                    print("*"*35,"Fin del reporte","*"*35)
                    break
    elif opcion=="4": # Opcion Registrar un cliente
        clave_cliente=str(random.randrange(0,1001))
        if clientes.get(clave_cliente)==None:
            nombre_cliente=input("Ingresa el nombre: ")
            clientes.update({clave_cliente:[clave_cliente,nombre_cliente]})
            print(f"Cliente agregado: {clave_cliente,nombre_cliente}")
            print(clientes.keys())
        else:
            print("Cliente encontrado. No se puede repetir")
    elif opcion=="5":
        clave_sala=str(random.randrange(0,101))
        if salas.get(clave_sala)==None:
            nombre_sala=input("Ingresa el nombre: ")
            print(f"Sala agregada: {clave_sala,nombre_sala}")
        else:
            print("Sala encontrada. No se puede repetir")
    elif opcion=="6":
        print("Ejecución Finalizada")
        break
    else:
        print("Opción incorrecta. vuelve a intentar")
        continue