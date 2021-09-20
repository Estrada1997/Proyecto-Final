from componentes import Meu, Valida
from helpers import borrar_Pantalla, gotoxy
from crudArchvos import Archivo
from Proyecto import *
from datetime import date
import time
# Procesos de las Opciones del Menu Mantenimiento
def empAdministrativos():
    borrarPantalla()
    depaAdmin,carAdmin,grabar,=[],[],""
    val=Valida()
    gotoxy(20,2);print("MANTENIMIENTO DE EMPLEADOS ADMINISTRATIVOS")
    gotoxy(15,4);print("Nombre: ")
    gotoxy(23,4);nom = input().title()
   #CODIGO DEPARTAMENTO-VALIDACIÓN
    while not depaAdmin:
        gotoxy(15,5);print("Código Departamento: ")
        gotoxy(36,5);cd= input()
        archiDepa = Archivo("PROYECTO/archivos/departamento.txt","|")
        depaAdmin = archiDepa.buscar(cd)
        if depaAdmin:
            DA = Departamento(depaAdmin[1],depaAdmin[0])
            gotoxy(36,5);print(DA.descripcion)
        else:
            gotoxy(36,5);print(" No existe Departamento con ese codigo[{}]".format(cd))
            time.sleep(2);gotoxy(36,5);print(" "*50)
   #CODIGO CARGO-VALIDACIÓN
    while not carAdmin:
        gotoxy(15,6);print("Código Cargo: ")
        gotoxy(29,6);car= input()
        archiCar = Archivo("PROYECTO/archivos/cargo.txt","|")
        carAdmin = archiCar.buscar(car)
        if carAdmin:
            CA = Departamento(carAdmin[1],carAdmin[0])
            gotoxy(29,6);print(CA.descripcion)
        else:
            gotoxy(29,6);print(" No existe Cargo con ese codigo[{}]".format(car))
            time.sleep(2);gotoxy(29,6);print(" "*50)

    gotoxy(15,7);print("Dirección: ")
    gotoxy(26,7);dir= input().title()
    gotoxy(15,8);print("Cédula: ")
    ced = val.cedula(" Error: Menos de 10 digitos",23,8)
    gotoxy(15,9);print("Teléfono: ")
    gotoxy(25,9);tel= input()
    gotoxy(15,10);print("Fecha de Ingreso: ")
    gotoxy(15,11);print("Dia: ")
    dia=val.solo_dia(" Error: Solo 31 dias",20,11)
    gotoxy(15,12);print("Mes: ")
    mes=val.solo_mes(" Error: Solo 12 Meses",20,12)
    gotoxy(15,13);print("Año: ")
    año=val.solo_año(" Error: Menor a 0",20,13)
    fi= date(año,mes,dia)  
    gotoxy(15,14);print("Sueldo: ")
    suel=val.solo_decimales(" Error: Solo decimales",23,14)
    while not grabar == "s":
        gotoxy(15,16);print("Esta seguro de guardar el mantemiento(s/n):")
        grabar=val.grabar(" Error:Solo 's' o 'n'",59,16)
        if grabar == "s":
            archiEmpA = Archivo("PROYECTO/archivos/administrativo.txt","|")
            EA = archiEmpA.leer()
            if EA : idEa="A"+str(len(EA)+1)
            else: idEa="A1"
                Obre = Obrero(nom,DA,CA,dir,ced,tel,fi,suel,idEa)
                datos = Obre.getEmpleado()
                datos = '|'.join(datos)
                archiEmpA.escribir([datos],"a")
                gotoxy(10,19);input("El Mantenimiento se ha guardado Satisfactoriamente\n Presione una tecla para continuar...")
        else:
            gotoxy(10,19);input("El Mantenimiento  No fue Grabado\n presione una tecla para continuar...")     

def emp_Obreros():
    borrarPantalla()
    depaObre,carObre,grabar,name,nom=[],[],"",[],""
    val=Valida()
    gotoxy(20,2);print("MANTENIMIENTO DE EMPLEADOS OBREROS")
    gotoxy(15,4);print("Nombre: ")
    gotoxy(23,4);nom = input().title()
   #CODIGO DEPARTAMENTO-VALIDACIÓN
    while not depaObre:
        gotoxy(15,5);print("Código Departamento: ")
        gotoxy(36,5);cd= input()
        archiDepa = Archivo("PROYECTO/archivos/departamento.txt","|")
        depaObre = archiDepa.buscar(cd)
        if depaObre:
            DO = Departamento(depaObre[1],depaObre[0])
            gotoxy(36,5);print(DO.descripcion)

        else:
            gotoxy(36,5);print(" No existe Departamento con ese codigo[{}]".format(cd))
            time.sleep(2);gotoxy(36,5);print(" "*50)
   #CODIGO CARGO-VALIDACIÓN
    while not carObre:
        gotoxy(15,6);print("Código Cargo: ")
        gotoxy(29,6);car= input()
        archiCar = Archivo("PROYECTO/archivos/cargo.txt","|")
        carObre = archiCar.buscar(car)
        if carObre:
            CO = Departamento(carObre[1],carObre[0])
            gotoxy(29,6);print(CO.descripcion)
        else:
            gotoxy(29,6);print(" No existe Cargo con ese codigo[{}]".format(car))
            time.sleep(2);gotoxy(29,6);print(" "*50)
    gotoxy(15,7);print("Dirección: ")
    gotoxy(26,7);dir= input()
    gotoxy(15,8);print("Cédula: ")
    ced = val.cedula(" Error: Menos de 10 digitos",23,8)
    gotoxy(15,9);print("Teléfono: ")
    gotoxy(25,9);tel= input()
    gotoxy(15,10);print("Fecha de Ingreso: ")
    gotoxy(15,11);print("Dia: ")
    dia=val.solo_dia(" Error: Solo 31 dias",20,11)
    gotoxy(15,12);print("Mes: ")
    mes=val.solo_mes(" Error: Solo 12 Meses",20,12)
    gotoxy(15,13);print("Año: ")
    año=val.solo_año(" Error: Menor a 0",20,13)
    fi= date(año,mes,dia)  
    gotoxy(15,14);print("Sueldo: ")
    suel=val.solo_decimales(" Error: Solo decimales",23,14)
    while not grabar == "s":
        gotoxy(15,16);print("Esta seguro de guardar el mantemiento(s/n):")
        grabar=val.grabar(" Error:Solo 's' o 'n'",59,16)
        if grabar == "s":
            archiEmpO = Archivo("PROYECTO/archivos/obrero.txt","|")
            EO = archiEmpO.leer()
            if EO : idEo="O"+str(len(EO)+1)
            else: idEo="O1"
                Obre = Obrero(nom,DO,CO,dir,ced,tel,fi,suel,idEo)
                datos = Obre.getEmpleado()
                datos = '|'.join(datos)
                archiEmpO.escribir([datos],"a")
                gotoxy(10,19);input("El Mantenimiento se ha guardado Satisfactoriamente\n Presione una tecla para continuar...")
        else:
            gotoxy(10,19);input("El Mantenimiento  No fue Grabado\n presione una tecla para continuar...")     

def cargos():
    borrarPantalla()
    val=Valida()
    grabar=""
    gotoxy(20,2);print("MANTENIMIENTO DE CARGOS")
    gotoxy(15,4);print("Codigo: ")
    gotoxy(15,5);print("Descripcion Cargo: ")
    gotoxy(33,5)
    desCargo = input()
    while not grabar == "s":
        gotoxy(15,7);print("Esta seguro de guardar el mantemiento(s/n):")
        grabar=val.grabar(" Error:Solo 's' o 'n'",59,7)
        if grabar == "s":
            archiCargo = Archivo("PROYECTO/archivos/cargo.txt","|")
            cargos = archiCargo.leer()
            if cargos : idSig = int(cargos[-1][0])+1
            else: idSig=1
                cargo = Cargo(desCargo,idSig)
                datos = cargo.getCargo()
                datos = '|'.join(datos)
                archiCargo.escribir([datos],"a")
                gotoxy(10,9);input("El Mantenimiento se ha guardado Satisfactoriamente\n Presione una tecla para continuar...")
        else:
            gotoxy(10,9);input("El Mantenimiento  No fue Grabado\n presione una tecla para continuar...")     

def departamento():
   borrarPantalla()
   val=Valida()
   grabar=""
   gotoxy(20,2);print("MANTENIMIENTO DE DEPARTAMENTO")
   gotoxy(15,4);print("Codigo: ")
   gotoxy(15,5);print("Descripcion Departamento: ")
   gotoxy(40,5)
   desDepa = input()
   while not grabar == "s":
        gotoxy(15,7);print("Esta seguro de guardar el mantemiento(s/n):")
        grabar=val.grabar(" Error:Solo 's' o 'n'",59,7)
        if grabar == "s":
            archiDepa = Archivo("PROYECTO/archivos/departamento.txt","|")
            dp = archiDepa.leer()
            if dp : idSig = int(dp[-1][0])+1
            else: idSig=1
                dep = Departamento(desDepa,idSig)
                datos = dep.getDepa()
                datos = '|'.join(datos) 
                archiDepa.escribir([datos],"a")
                gotoxy(10,9);input("El Mantenimiento se ha guardado Satisfactoriamente\n Presione una tecla para continuar...")
        else:
            gotoxy(10,9);input("El Mantenimiento  No fue Grabado\n presione una tecla para continuar...")     

def empresa():
    borrarPantalla()
    val=Valida()
    grabar="" 
    gotoxy(20,2);print("MANTENIMIENTO DE EMPRESA")
    gotoxy(15,4);print("Razón Social:")
    gotoxy(15,5);print("Dirección: ")
    gotoxy(15,6);print("Teléfono: ")
    gotoxy(15,7);print("Ruc: ")
    gotoxy(29,4);razon = input()
    gotoxy(26,5);dir = input()
    gotoxy(25,6);tel = input()
    gotoxy(20,7);ruc = input()
    while not grabar == "s":
        gotoxy(15,9);print("Esta seguro de guardar el mantemiento(s/n):")
        grabar=val.grabar(" Error:Solo 's' o 'n'",59,9)
        if grabar == "s":
            archiEmp = Archivo("PROYECTO/archivos/empresa.txt","|")
            emp = Empresa(razon,dir,tel,ruc)
            datos = emp.getEmpresa()
            datos = '|'.join(datos)
            archiEmp.escribir([datos],"w")
            gotoxy(10,11);input("El Mantenimiento se ha guardado Satisfactoriamente\n Presione una tecla para continuar...")
        else:
            gotoxy(10,11);input("El Mantenimiento  No fue Grabado\n presione una tecla para continuar...")     


def deducciones():
    borrarPantalla()
    val=Valida()
    grabar=""
    gotoxy(20,2);print("MANTENIMIENTO DE DEDUCCIONES")
    gotoxy(15,4);print("Valor iess:")
    gotoxy(15,5);print("Valor Comisión: ")
    gotoxy(15,6);print("Valor Antiguedad: ")
    iess = val.solo_decimales(" Error: Solo númericos",27,4)
    comi = val.solo_decimales(" Error: Solo númericos",31,5)
    anti = val.solo_decimales(" Error: Solo númericos",33,6)
    while not grabar == "s":
        gotoxy(15,8);print("Esta seguro de guardar el mantemiento(s/n):")
        grabar=val.grabar(" Error:Solo 's' o 'n'",59,8)
        if grabar == "s":
            archiDedu = Archivo("PROYECTO/archivos/deducciones.txt","|")
            dep = Deduccion(iess,comi,anti)
            datos = dep.getDeduccion()
            datos = '|'.join(datos)
            archiDedu.escribir([datos],"w")
            gotoxy(10,10);input("El Mantenimiento se ha guardado Satisfactoriamente\n Presione una tecla para continuar...")
        else:
            gotoxy(10,10);input("El Mantenimiento  No fue Grabado\n presione una tecla para continuar...")     
# ...........................................................
# Opciones del Menu Novedades
def sobretiempos():
    borrarPantalla()     
    gotoxy(20,2);print("INGRESO DE HORAS EXTRAS")
    empleado,entEmpleado,grabar = [],None,""
    aamm,h50,h100=0,0,0
    while not empleado:
        gotoxy(15,5);print("Empleado ID[    ]: ")
        gotoxy(27,5);id = input().upper()
        archiEmpleado = Archivo("PROYECTO/archivos/obrero.txt","|")
        empleado = archiEmpleado.buscar(id)
        if empleado:
            entEmpleado = Obrero(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],empleado[8],empleado[0]) 
            gotoxy(35,5);print(entEmpleado.nombre)
        else: 
            gotoxy(27,5);print("No existe Empleado con ese codigo[{}]:".format(id))
            time.sleep(2);gotoxy(27,5);print(" "*40)
    gotoxy(15,6);print("Periodo[aaaamm]")
    gotoxy(15,7);print("Horas50:")
    gotoxy(15,8);print("Horas100:")
    validar = Valida()
    aamm = validar.solo_numeros(" Error: Solo numeros",23,6)
    h50 = validar.solo_decimales(" Error: Solo númericos",23,7)
    h100 = validar.solo_decimales(" Error: Solo númericos",24,8)
    while not grabar == "s":
        gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
        grabar=validar.grabar(" Error:Solo 's' o 'n'",54,10) 
        if grabar == "s":
            archiSobretiempo = Archivo("PROYECTO/archivos/sobretiempo.txt","|")
            sobretiempos = archiSobretiempo.leer()
            if sobretiempos : idSig = int(sobretiempos[-1][0])+1
            else: idSig=1
                sobretiempo = Sobretiempo(entEmpleado,aamm,h50,h100,True,idSig)
                datos = sobretiempo.getSobretiempo()
                datos = '|'.join(datos)
                archiSobretiempo.escribir([datos],"a")                 
                gotoxy(10,12);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
        else:
            gotoxy(10,12);input("Registro No fue Grabado\n presione una tecla para continuar...")     
     
def prestamos():
    borrarPantalla()     
    gotoxy(20,2);print("PRESTAMO")
    empleado,empleado1,empleado2,entEmpleado,grabar = [],[],[],None,""
    aamm,valor,numpago,saldo,=0,0,0,0
    while not empleado:
        gotoxy(15,5);print("Empleado ID[    ]: ")
        gotoxy(27,5);id = input().upper()
        archiEmpleado = Archivo("PROYECTO/archivos/obrero.txt","|")
        empleado1 = archiEmpleado.buscar(id)
        archiEmpleado = Archivo("PROYECTO/archivos/administrativo.txt","|")
        empleado2 = archiEmpleado.buscar(id)
        if empleado1:
            entEmpleado = Obrero(empleado1[1],empleado1[2],empleado1[3],empleado1[4],empleado1[5],empleado1[6],empleado1[7],empleado1[8],empleado1[0]) 
            gotoxy(35,5);print(entEmpleado.nombre)
            empleado+=empleado1  
        elif empleado2:
            entEmpleado = Administrativo(empleado2[1],empleado2[2],empleado2[3],empleado2[4],empleado2[5],empleado2[6],empleado2[7],empleado2[8],empleado2[0]) 
            gotoxy(35,5);print(entEmpleado.nombre)
            empleado+=empleado2
        else: 
            gotoxy(27,5);print("No existe Empleado con ese codigo[{}]:".format(id))
            time.sleep(2);gotoxy(27,5);print(" "*40)
    
    gotoxy(15,6);print("Periodo[aaaamm]")
    gotoxy(15,7);print("Valor:")
    gotoxy(15,8);print("Número de Pagos:")
    gotoxy(15,9);print("Saldo:")
    validar = Valida()
    aamm=validar.solo_numeros(" Error: Solo numeros",23,6)
    valor = validar.solo_decimales(" Error: Solo numeros",22,7)
    numpago = validar.solo_numeros(" Error: Solo numeros",32,8)
    saldo = validar.solo_decimales(" Error: Solo numeros",22,9)
    while not grabar == "s":
        gotoxy(15,11);print("Esta seguro de Grabar El registro(s/n):")
        grabar=validar.grabar(" Error:Solo 's' o 'n'",54,11) 
        if grabar == "s":
            archiPrestamo = Archivo("PROYECTO/archivos/prestamo.txt","|")
            presta = archiPrestamo.leer()
            if presta : idSig = int(presta[-1][0])+1
            else: idSig=1
                pres = Prestamo(entEmpleado,aamm,valor,int(numpago),saldo,True,idSig)
                datos = pres.getPrestamo()
                datos = '|'.join(datos)
                archiPrestamo.escribir([datos],"a")                 
                gotoxy(10,13);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
        else:
            gotoxy(10,13);input("Registro No fue Grabado\n presione una tecla para continuar...")     
     
# opciones de Rol de Pago
def rolAdministrativo():
    borrarPantalla()
    grabar=""
    # Se ingresa los datos del rol a procesar     
    gotoxy(20,2);print("ROL ADMINISTRATIVO")
    aamm=0
    gotoxy(15,6);print("Periodo[aaaamm]")
    validar = Valida()
    aamm=validar.solo_numeros("Error: Solo numeros",23,6)
   # Se procesa el rol con la confirmacion del usuario
    while not grabar == "s":
        gotoxy(15,8);print("Esta seguro de Grabar El registro(s/n):")
        grabar=validar.grabar(" Error:Solo 's' o 'n'",54,8) 
        entEmpAdm = None
        if grabar == "s":
        # Obtener lista de empleados a procesar el rol
            archiEmp = Archivo("PROYECTO/archivos/administrativo.txt","|")
            ListaEmpAdm = archiEmp.leer()
            if ListaEmpAdm : 
                archiEmpresa = Archivo("PROYECTO/archivos/empresa.txt","|")
                empresa = archiEmpresa.leer()[0]
                entEmpresa = Empresa(empresa[0],empresa[1],empresa[2],empresa[3])
                archiDeducciones = Archivo("PROYECTO/archivos/deducciones.txt","|")
                deducciones = archiDeducciones.leer()[0]
                entDeduccion = Deduccion(float(deducciones[0]),float(deducciones[1]),float(deducciones[2]))
                #print(entDeduccion.getIess(),entDeduccion.getComision(),entDeduccion.getAntiguedad())
                nomina = Nomina(date.today(),aamm)
                for empleado in ListaEmpAdm:
                    #print(empleado)
                    entEmpAdm = Administrativo(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],float(empleado[8]),empleado[0]) 
                    #print(entEmpAdm.nombre,entEmpAdm.sueldo)
                    nomina.calcularNominaDetalle(entEmpAdm,entDeduccion)
                    # grabar cabecera del rol
                    datosCab = nomina.getNomina()
                    datosCab = '|'.join(datosCab)
                    archiRol = Archivo("PROYECTO/archivos/rolCabAdm.txt","|")
                    archiRol.escribir([datosCab],"a")
                    # grabar detalle del rol
                    archiDet = Archivo("PROYECTO/archivos/rolDetAdm.txt","|")
                    datosDet = nomina.getDetalle()
                    # se graba en el detalle empleado por empleado           
            for dt in datosDet:
                dt = nomina.aamm+'|'+'|'.join(dt)
                archiDet.escribir([dt],"a")
                # imprimir rol
                nomina.mostrarCabeceraNomina(entEmpresa.razonSocial,entEmpresa.direccion,entEmpresa.telefono,entEmpresa.ruc,"A D M I N I S T R A T I V O")
                nomina.mostrarDetalleNomina()
        else:
            gotoxy(10,10);input("Rol No fue Procesado\n presione una tecla para continuar...")     
    input(" Presione una tecla continuar...")  

def consultaRol():
    borrarPantalla()
    validar = Valida()
    grabar,rol = "",""
    # Se ingresa los datos del rol a Consultar     
    gotoxy(20,2);print("CONSULTA DE ROL OBRERO - ADMINISTRATIVO")
    aamm=""
    gotoxy(15,4);print("Obrero-Administrativo(O/A): ")
    rol=validar.rol(" Error: 'O' o 'A'",44,4)
    gotoxy(15,6);print("Periodo[aaaamm]")
    aamm=validar.solo_numeros("Error: Solo numeros",23,6)
    while not grabar == "s":
        gotoxy(15,8);print("Esta seguro de Procesar el Rol(s/n):")
        grabar=validar.grabar(" Error:Solo 's' o 'n'",54,8) 
        if grabar == "s":
            if rol == "A": 
                tit = "A D M I N I S T R A T I V O"
                archiRolCab = Archivo("PROYECTO/archivos/rolCabAdm.txt","|")
                archiRolDet = Archivo("PROYECTO/archivos/rolDetAdm.txt","|")
            else: 
                tit = "O B R E R O"
                archiRolCab = Archivo("PROYECTO/archivos/rolCabObr.txt","|")
                archiRolDet = Archivo("PROYECTO/archivos/rolDetObr.txt","|")
                cabrol = archiRolCab.buscar(aamm)
                if cabrol:
                    entCabRol = Nomina(cabrol[1],cabrol[0])
                    entCabRol.totIngresos=float(cabrol[2])
                    entCabRol.totDescuentos=float(cabrol[3])
                    entCabRol.totPagoNeto=float(cabrol[4])
                    detalle= archiRolDet.buscarLista(aamm)
                    for det in detalle:
                        entCabRol.detalleNomina.append(det[1:])    
                        # print(entCabRol.getNomina())
                        # print(entCabRol.getDetalle())
                        # input()
                        # imprimir rol    
                        archiEmpresa = Archivo("PROYECTO/archivos/empresa.txt","|")
                        empresa = archiEmpresa.leer()[0]
                        entEmpresa = Empresa(empresa[0],empresa[1],empresa[2],empresa[3])
                        entCabRol.mostrarCabeceraNomina(entEmpresa.razonSocial,entEmpresa.direccion,entEmpresa.telefono,entEmpresa.ruc,tit)
                        entCabRol.mostrarDetalleNomina()
                else:
                    gotoxy(10,10);input("No existe rol con ese periodo\n presione una tecla para continuar...")     
        else:
            gotoxy(10,10);input("Consulta Cancelada\n presione una tecla para continuar...")     
    input("  Presione una tecla continuar...")  

def rolObrero():
   borrarPantalla()
   # Se ingresa los datos del rol a procesar 
   grabar = ""
   gotoxy(20,2);print("ROL OBRERO")
   aamm=0
   gotoxy(15,6);print("Periodo[aaaamm]")
   validar = Valida()
   aamm=validar.solo_numeros("Error: Solo numeros",23,6)
   while not grabar == "s":
        gotoxy(15,8);print("Esta seguro de Procesar el Rol(s/n):")
        grabar=validar.grabar(" Error:Solo 's' o 'n'",54,8) 
        entEmpAdm = None
        # Se procesa el rol con la confirmacion del usuario
        if grabar == "s":
        # Obtener lista de empleados a procesar el rol
            archiEmp = Archivo("PROYECTO/archivos/obrero.txt","|")
            ListaEmpAdm = archiEmp.leer()
            if ListaEmpAdm : 
                archiEmpresa = Archivo("PROYECTO/archivos/empresa.txt","|")
                empresa = archiEmpresa.leer()[0]
                entEmpresa = Empresa(empresa[0],empresa[1],empresa[2],empresa[3])
                archiDeducciones = Archivo("PROYECTO/archivos/deducciones.txt","|")
                deducciones = archiDeducciones.leer()[0]
                entDeduccion = Deduccion(float(deducciones[0]),float(deducciones[1]),float(deducciones[2]))
                #print(entDeduccion.getIess(),entDeduccion.getComision(),entDeduccion.getAntiguedad())
                nomina = Nomina(date.today(),aamm)
                for empleado in ListaEmpAdm:
                    #print(empleado)
                    entEmpAdm = Obrero(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],int(empleado[7][:4]),float(empleado[8]),empleado[0]) 
                    #print(entEmpAdm.nombre,entEmpAdm.sueldo)
                    nomina.calcularNominaDetalle(entEmpAdm,entDeduccion)
                    # grabar cabecera del rol
                    datosCab = nomina.getNomina()
                    datosCab = '|'.join(datosCab)
                    archiRol = Archivo("PROYECTO/archivos/rolCabObr.txt","|")
                    archiRol.escribir([datosCab],"a")
                    # grabar detalle del rol
                    archiDet = Archivo("PROYECTO/archivos/rolDetObr.txt","|")
                    datosDet = nomina.getDetalle()
                    # se graba en el detalle empleado por empleado           
                    for dt in datosDet:
                        dt = nomina.aamm+'|'+'|'.join(dt)
                        archiDet.escribir([dt],"a")
                        # imprimir rol
                        nomina.mostrarCabeceraNomina(entEmpresa.razonSocial,entEmpresa.direccion,entEmpresa.telefono,entEmpresa.ruc,"O B R E R O S")
                        nomina.mostrarDetalleNomina()
        else:
            gotoxy(10,10);input("Rol No fue Procesado\n presione una tecla para continuar...")     
    input(" Presione una tecla continuar...")  

# Menu Proceso Principal
opc=''
while opc !='4':  
    borrarPantalla()      
    menu = Menu("Menu Principal",["1) Mantenimiento","2) Novedades","3) Rol de Pago","4) Salir"],20,10)
    opc = menu.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='7':
            borrarPantalla()    
            menu1 = Menu("Menu Mantenimiento",["1) Empleados Administratvos","2) Empleados Obreros","3) Cargos","4) Departamentos","5) Empresa","6) Parametros","7) Salir"],20,10)
            opc1 = menu1.menu()
            if opc1 == "1":
                empAdministrativos()
            elif opc1 == "2":
                empObreros()
            elif opc1 == "3":
                cargos()
            elif opc1 == "4":
                departamento()
            elif opc1 == "5":
                empresa()
            elif opc1 == "6":
                deducciones()      

    elif opc == "2":
            borrarPantalla()
            menu2 = Menu("Menu Novedades",["1) Sobretiempo","2) Prestamos","3) Salir"],20,10)
            opc2 = menu2.menu()
            if opc2 == "1":
                sobretiempos()
            elif opc2 == "2":
                prestamos()

    elif opc == "3":
            borrarPantalla()
            menu3 = Menu("Menu Rol",["1) Rol Administrativos","2) Rol Obreros","3) Consulta Rol","4) Salir"],20,10)
            opc3 = menu3.menu()
            if opc3 == "1":
                rolAdministrativo()
            elif opc3 == "2":
                rolObrero()
            elif opc3 == "3":
                consultaRol()

    elif opc == "4":
           borrarPantalla()
           print("Gracias por su visita....")
    else:
          print("Opcion no valida") 
input("Presione una tecla para salir")
borrarPantalla()
