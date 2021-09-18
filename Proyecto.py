import os 
from datetime import date
from abc import ABC, astractmethod
from helpers import gotoxy
class Empresa:
    def __init__(self, nombre = "My Code Poo", jefe = "Ing. Anderson Estrda", ruc ="0921171617001", telf ="0982971849", direc ="Bucay (Ganl. Antonio Elizalde"):
        self.nombre = nombre 
        self.ruc = ruc 
        self.jefe = jefe 
        self.telefono = telf 
        self.direccion = direc 
    def mostrar_Empresa(self):
        print("Empresa: {} \nJefe: {:30} Ruc:{}  \nDirecc: {}".format(self.nombre, self.jefe, self.ruc,  self.direccion)) 

class Departamento:
    def __init__(self, descrip ="Seguro", id = 1):
        self.__id = id
        self.descrip = descrip
     @property
    def id(self):
        return self.__id
    def mostrar_Departamento(self):
        print("{}. Departamento de {}".format(self.id, self.descrip))
        print(" ")

class Cargo: 
    def __init__(self,descrip, id=1):
        self.__id = id
        self.descrip = descrip
    @property
    def id(self):
        return self.__id
    def mostrar_Cargo(self):
        print("{}. Cargo {}".format(self.id, self.descrip))
    def get_Cargo(self):
        return [str(self.id), self.descrip]

class Empleado(ABC):
    def __init__(self, id, nom, depart, cargo, direc, ced, telf, sueldo, Fe_Ingreso):
        self.__id = id 
        self.nom = nom 
        self.depart = depart
        self.cargo = cargo
        self.direc = direc
        self.cedula = ced 
        self.telefono = telf
        self.sueldo = sueldo
        self.Fe_Ingreso = Fe_Ingreso  
    @property
    def id(self):
        return self.__id
    @abstractmethod
    def valor_Hora(self):
        return self.sueldo/240
    def mostrar_Empleado(self):
        print("{} Empleado: {:30} Cedula: {} \nDerieccion: {} \nCargo: {:30} Departamento: {}".format(self.id, self.nom, self.ced, self.direc, self.cargo, self.depart))

class Administrativo(Empleado):
    def __init__(self, id, nom, depart, cargo, direc, ced, telf, sueldo, Fe_Ingreso, comision): 
        super().__init__( id, nom, depart, cargo, direc, ced, telf, sueldo, Fe_Ingreso)
        self.comision = comision
    def mostrar_Empleado(self):  # FALTA DOTOS EN   ADMNISTRATIVO 
        prnt(" {:10} Administrativo: {} \nCedula:{:20} Dreccion: {} \nCargo:{:30} Departamento:{}".format(self.id, self.nom, self.cedula, self.drec, self.cargo, self.depart))
        print("Comision:{}".format(self.comision))
    def valor_Hora(self):
        return super().valor_Hora()
    def get_Empleado(self):
        return [self.id, self.nom, str(self.depart.id), str(self.cargo.id), self.direc, self.cedula, self.telefono, str(self.Fe_Ingreso), str(self.sueldo), str(self.comision)]

class Obrero(Empleado): 
    def __init__(self, id, nom, depart, cargo, direc, ced, telf, sueldo, Fe_Ingreso, CC=True):  
        super().__init__(id, nom, depart, cargo, direc, ced, telf, sueldo, Fe_Ingreso)
        self.cc= cc
    def mostrar_Empleado(self):
        print(" {:10}Obrero:{} Cedula:{} \nDireccion:{} Cargo:{} \nDepartamento:{}".format(self.id, self.nom, self.cedula, self.direc, self.cargo, self.depart))
        print("CColectivo:{}".format(self.cc))
    def valor_Hora(self):
        return super().valor_Hora()
    def get_Empleado(self):
        return [self.id, self.nom, str(self.depart.id), str(self.cargo.id), self.direc, self.cedula, self.telefono, str(self.Fe_Ingreso), str(self.sueldo), str(self.cc)]

class Deduccion:
    def __init__(self, iess, comision, antiguedad):
        self.__iess = iess
        self.__comision = comision
        self.__antiguedad = antiguedad
    def iess(self):
        return round(self.__iess/100,4)
    def comision(self):
        return round(self.__comision/100,2)
    def antiguedad(self):
        return round(self.__antiguedad/100,2)
    def mostrar_Deduccion(self):
        print("Valor Iess = $ {} \n Valor comision ({}) = \n Valor antiguedad ({})")

class Prestamo:
    def __init__(self, empleado, aamm, valor, nuPago, sueldo, estado=True, id=1):
        self.__id = id
        self.empleado = empleado
        self.aamm = aamm
        self.valor = valor 
        self.nuPago = nuPago 
        self.saldo = saldo 
        self.cuota = valor/nuPago
        self.estado = estado
    @property
    def id(self):
        return self.__id 
    def mostrar_Prestamo(self):
        print('''{}° Prestamo Realizado: {}
          - Empleado = {}
          - Valor = $ {}
          - Numeros Pagos = {}
          - Cuota = $ {:.2f}
          - Saldo = $ {:.2f}
          - Estado = {}'''.format(self.id, self.aamm, self.empleado.nom, self.valor, self.nuPago, self.cuota, self.saldo, self.estado))
    def get_Prestamo(self):
        return [str(self.id), self.empleado.id, self.aamm, str(self.valor), str(self.nuPago), str(self.cuota), str(self.saldo),str(self.estado)]

class Sobre_Tiempo:
    def __init__(self, empleado, aamm, hSuplemetarias, hExtrardinarias, estado=True, id=1):
        self.__id = id
        self.empleado = empleado
        self.aamm = aamm
        self.h50 = hSuplemetarias
        self.h100 = hExtrardinarias
        self.estado = estado
    @property
    def id(self):
        return self.__id
    def sobre_tiempo(self):
        return round(self.empleado.valor_Hora()+(self.h50*1.5 + self.h100*2), 2)
    def mostrar_Sobre_Tiempo(self):
        print('''{}°Sobre tiempo:{}
         - Empleado = {}
         - H50 = {}
         - H100 = {}
         - Estado = {}'''.format(self.id, self.aamm, self.empleado.nom, self.h50, self.h100, self.valor, self.estado))
    def get_Sobre_Tiempo(self):
        return [str(self.id), str(empleado.id), self.aamm, str(self.h50), str(h100), self.valor, self.estado]

class Calculo(ABC):
    @abstractmethod
    def get_Sueldo(self):
        pass
    @abstractmethod
    def get_Sobre_Tiempo(self, aamm):
        pass
    @abstractmethod
    def get_Comision(self):
        pass
    @abstractmethod
    def get_Atiguedad(self):
        pass
    @abstractmethod
    def get_Iess(self):
        pass
    @abstractmethod
    def get_Prestamo(self, aamm):
        pass

class Nomina:
    secuencia = 0
    def __init__(self, fecha, aamm, tipoRol):
        Nomina.secuencia += 1
        self.__id = Nomina.secuencia
        self.fecha = fecha
        self.aamm = aamm
        self.rol = tipoRol
        self.totIngreso = 0
        self.totDescuento = 0
        self.totPagoNeto = 0
        self.canEmp = 0
        self.detalleNomina = []
    @property
    def id(self):
        return self.__id 
    def calcular_NominaDetalle(self, empleado):
        detalle = DetalleNomina(empleado)
        rubrosIngresos = detalle.calcularRubrosIngresos(self.aamm)
        rubrosEgresos = detalle.calcularRubrosEgresos(self.aamm)
        self.totIngreso += detalle.totIngreso
        self.totDescuento += detalle.totDes
        self.totPagoNeto += detalle.totLiq
        self.detalleNomina.append([[empleado], rubrosIngresos, rubrosEgresos])
    def mostrar_CabeceraNomina(self, nombre, direc, telef, ruc):
        os.system("cls")
        print("            {} Ruc: {} \nDireccion: {} Telefono: {}".format(self.nombre, self.ruc, self.direc, self.telef))
        print("-------------------------------------------------------------------------------------------")
        print("FECHA: {}  NOMINA DE PAGO DE EMPLEADORES: {}".format(self.datetime, self.depart))  # faltqa reviar
        print("Nomina #: {} Correspondencia al periodo: {}".format(self.id, self.aamm))
        print("--"*59)
        print(" "*5, "EMPLEADOS", "Ingresos", "Egresos")                                                           # MEJORA ESTA PARTE
        print("Nombre        Cargo      Departamento     Sueldo       SobreTiempo        Antiguedad     Comision        Total Ingreso      IESS       Prestamo     Total Descuento            Monto")    # FALTA DATOS 
    def mostrar_DetalleNomina(self):
        fila = 8
        for det in omina.detalleNomina:
            emp = det[0][0]
            ing = det[1]
            des = det[2]
            gotoxy(1,fila);print(emp.nombre,end="")
            gotoxy(10,fila);print(emp.cargo.descripcion,end="")
            gotoxy(25,fila);print(emp.departamento.descripcion,end="")
            gotoxy(43,fila);print(ing[0],end="")
            gotoxy(53,fila);print(ing[1],end="")
            gotoxy(67,fila);print(ing[2],end="")
            gotoxy(78,fila);print(ing[3],end="")
            gotoxy(86,fila);print(ing[4],end="")
            gotoxy(95,fila);print(des[0],end="")
            gotoxy(104,fila);print(des[1],end="")
            gotoxy(114,fila);print(des[2],end="")
            gotoxy(122,fila);print(des[3],end="")
            fila += 1
class DetalleNomina(Calculo_Rol):
    secuencia = 0
    def __init__(self, empleado, idNomina):
        DetalleNomina.secuencia += 1
        self.__id = DetalleNomina.secuencia
        self.empleado = empleado
        self.nomina = idNomina
        self.totIng = 0
        self.totDes = 0
        self.totLiq = 0
    def get_Sueldo(self):
        return self.empleado.sueldo
    def get_Sobre_Tiempo(self, aamm):
        if self.empleado.id[0]=="0":
            calSob = 20
            return calSob
        else: return 0
    def get_Atiguedad(self):
        if self.empleado.id[0]=="0":
            calAnt = 20
            return calAnt
        else: return 0
    def get_Comision(self):
        return round(self.empleado.valor_Hora()*ded.comision(),2)
    def get_Iess(self):
        return round(self.empleado.sueldo* ded.iess(),2)
    def get_Prestamo(self, aamm):
        archiPrestamo = Archivo("./archivos/prestamo.txt", "||")
        prestamo = archiPrestamo.buscarRol(self.empleado.id.aamm)
        if prestamo:
            entPrestamo = Prestamo(prestamo[1], prestamo[2], prestamo[3], prestamo[4], prestamo[4], prestamo[6], prestamo[7])
            return entPrestamo.cuato
        else: return 0
    def calcularRubrosIngresos(self, aamm):
        ingresos = []
        ingresos.append(self.get_Sueldo())
        ingresos.append(self.get_Sobre_Tiempo(aamm))
        ingresos.append(self.get_Atiguedad())
        ingresos.append(self.get_Comision())
        for valor in ingresos:
            self.totIng += valor 
        ingresos.append(self.totIng)
        return ingresos
    def calcularRubrosEgresos(self):
        descuento = []
        descuento.append(self.get_Iess())
        descuento.append(self.get_Prestamo(aamm))
        for valor in descuentos:
            self.totDes += valor
        self.totLiq = round(self.totIng - self.totDes,2)
        descuentos.append(self.totDes)
        descuentos.append(self.totLiq)
        return descuentos