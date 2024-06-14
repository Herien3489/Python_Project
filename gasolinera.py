#Nombre: Eli Noe Herrera Loria

while True:
    #HACEMOS EL INICIO DE SESION Y REPETIMOS MIENTRAS SEA DIFERENTE
    print('PROGRAMA QUE SIMULA UNA GASOLINERA')
    user = str(input('Ingresa el usuario'))
    pasw = str(input('Ingresa la contraseña'))

    #REINCIAMOS VALORES PARA CADA VUELTA
    dinero_total = 0
    litros_totales = 0
    cap_final_diesel = 0
    cap_final_premium = 0
    cap_final_magna = 0


    while True:

        #SI ES CORRECTO EL USUARIO Y CONTRASEÑA SEGUIMOS CON EL PROCESO
        if user == 'admin' and pasw == 'admin':
            #PREGUNTAMOS AL USUARIO QUE QUIERE HACER
            print('1: abrir caja, 2: cerrar caja')
            op = int(input())

            #SI ESCOGE 1 EMPEZARA SU TURNO Y HAREMOS EL PROCESO
            if op == 1:
                
                #PEDIMOS INGRESAR EL PRECIO DE LOS TIPOS DE GASOLINA
                diesel = float(input('Ingresa el precio del Diesel'))
                magna = float(input('Ingresa el precio de la magna'))
                premium = float(input('Ingresa el precio de la premium'))
                #PEDIMOS INGRESAR LA CAPACIDAD DE LA CISTERNA DE CADA TIPO DE GASOLINA
                cap_diesel = float(input('Capacidad de la cisterna de Diesel'))
                cap_magna = float(input('Capacidad de la cisterna de Magna'))
                cap_premium = float(input('Capacidad de la cisterna de Premium'))

                while True:

                    #PREGUNTAMOS QUE TIPO DE GASOLINA CARGARA Y CUANTOS LITROS
                    print('1: Magna, 2: Premium, 3: Diesel')
                    carga = int(input('Que tipo de gasolina cargaras o 0 para salir?'))

                    #SI DIJITA 0 ENTONCES EL PROCESO TERMINARA
                    if carga == 0:
                        break

                    #SI ESCOGE ALGUNA DE LAS OPCIONES REALIZA EL PROCESO NECESARIO
                    #SI EN CUALQUIERA DE LOS PROCESOS NO QUEDA SUFICIENTE GASOLINA
                    #SALTARA UN MENSAJE QUE DIGA QUE NO QUEDA
                    if carga == 1:
                        litros = float(input('Cuantos litros deseas cargar?'))
                        precio = carga * litros
                        cap_final_magna = cap_magna - litros

                        if cap_final_magna <= 0:
                            print('No queda más gasolina')
                        
                        else:
                                print('-----TICKET-----')
                                print('Precio: ', precio)
                                print('Litros: ',litros)
                                cap_final_magna = cap_magna - litros

                    elif carga == 2:
                        litros = float(input('Cuantos litros deseas cargar?'))
                        precio = litros * premium
                        cap_final_premium = cap_premium - litros
                        if cap_final_premium <= 0:
                            print('No queda más gasolina')
                            
                        else:
                            print('-----TICKET-----')
                            print('Precio: ', precio)
                            print('Litros: ',litros)
                            cap_final_premium = cap_premium - litros

                    elif carga == 3:
                        litros = float(input('Cuantos litros deseas cargar?'))
                        precio = litros * diesel
                        cap_final_diesel = cap_diesel - litros
                        
                        if cap_final_diesel <= 0:
                            print('No queda más gasolina')
                        
                        else:
                            print('-----TICKET-----')
                            print('Precio: ', precio)
                            print('Litros: ',litros)
                            cap_final_diesel = cap_diesel - litros
                    
                    #HACEMOS NUESTROS ACUMULADORES PARA EL DINERO VENDIDO Y LOS LITROS VENDIDOS
                    dinero_total = dinero_total + precio
                    litros_totales = litros_totales + litros

                
            #CUANDO HAGAMOS CORTE DE CAJA, IMPRIMIREMOS NUESTRO CORTE CON LO QUE VENDIMOS EN EL TURNO
            #Y CUANTO QUEDÓ EN LA CISTERNA
            else:
                print('-----CORTE-----')
                print('Dinero Total: ', dinero_total)
                print('Litros:', litros_totales)
                print('Cisterna magna: ', cap_final_magna)
                print('Cisterna Premium: ', cap_final_premium)
                print('Cisterna Diesel: ', cap_final_diesel)
                print('-----CORTE-----')
                break