#-------------------------------------------------------------ESTACIONAMIENTO DE VEHICULOS------------------------------------------------------------------------------                                                                         

#----------------------------
# MÓDULOS                                                                                                                  
#----------------------------
import os # para usar system("cls") /clear screen
from tkinter import * # para usar la interfaz gráfica
from tkinter import messagebox #para desplegar mensajes de error
from datetime import datetime, timedelta #facilita utilizar medidas de tiempo
import pickle #permite leer datos
#----------------------------


#----------------------------
# FUNCIONES                                                                                                  
#----------------------------
#esta funcion se encarga de refrescar todos los diccionarios
def refrescar_diccionarios():
    global dic_moneda1, dic_moneda2, dic_moneda3, dic_billete1, dic_billete2, dic_billete3, dic_billete4, dic_billete5, moneda1, moneda2, moneda3, billete1, billete2, billete3, billete4,billete5, dic_total_billetes, dic_total_monedas
    try:
        dic_moneda1["entrada"][1] = dic_moneda1["entrada"][0] * moneda1
        dic_moneda1["salida"][1] = dic_moneda1["salida"][0] * moneda1
        dic_moneda1["saldo"][0] = dic_moneda1["entrada"][0] - dic_moneda1["salida"][0]
        dic_moneda1["saldo"][1] = dic_moneda1["entrada"][1] - dic_moneda1["salida"][1]
    except:
        dic_moneda1["entrada"][1] = 0
        dic_moneda1["salida"][1] = 0
        dic_moneda1["saldo"][0] = dic_moneda1["entrada"][0] - dic_moneda1["salida"][0]
        dic_moneda1["saldo"][1] = dic_moneda1["entrada"][1] - dic_moneda1["salida"][1]

    try:
        dic_moneda2["entrada"][1] = dic_moneda2["entrada"][0] * moneda2
        dic_moneda2["salida"][1] = dic_moneda2["salida"][0] * moneda2
        dic_moneda2["saldo"][0] = dic_moneda2["entrada"][0] - dic_moneda2["salida"][0]
        dic_moneda2["saldo"][1] = dic_moneda2["entrada"][1] - dic_moneda2["salida"][1]
    except:
        dic_moneda2["entrada"][1] = 0
        dic_moneda2["salida"][1] = 0
        dic_moneda2["saldo"][0] = dic_moneda2["entrada"][0] - dic_moneda2["salida"][0]
        dic_moneda2["saldo"][1] = dic_moneda2["entrada"][1] - dic_moneda2["salida"][1]


    try:
        dic_moneda3["entrada"][1] = dic_moneda3["entrada"][0] * moneda3
        dic_moneda3["salida"][1] = dic_moneda3["salida"][0] * moneda3
        dic_moneda3["saldo"][0] = dic_moneda3["entrada"][0] - dic_moneda3["salida"][0]
        dic_moneda3["saldo"][1] = dic_moneda3["entrada"][1] - dic_moneda3["salida"][1]
    except:
        dic_moneda3["entrada"][1] = 0
        dic_moneda3["salida"][1] = 0
        dic_moneda3["saldo"][0] = dic_moneda3["entrada"][0] - dic_moneda3["salida"][0]
        dic_moneda3["saldo"][1] = dic_moneda3["entrada"][1] - dic_moneda3["salida"][1]



    dic_total_monedas = {"entrada": [dic_moneda1["entrada"][0] + dic_moneda2["entrada"][0] + dic_moneda3["entrada"][0] , dic_moneda1["entrada"][1] + dic_moneda2["entrada"][1] + dic_moneda3["entrada"][1]], #(cantidad de monedas, total de dinero)
                    "salida": [dic_moneda1["salida"][0] + dic_moneda2["salida"][0] + dic_moneda3["salida"][0] , dic_moneda1["salida"][1] + dic_moneda2["salida"][1] + dic_moneda3["salida"][1]],
                    "saldo": [dic_moneda1["saldo"][0] + dic_moneda2["saldo"][0] + dic_moneda3["saldo"][0] , dic_moneda1["saldo"][1] + dic_moneda2["saldo"][1] + dic_moneda3["saldo"][1]]}


    try:
        dic_billete1["entrada"][1] = dic_billete1["entrada"][0] * billete1
        dic_billete1["salida"][1] = dic_billete1["salida"][0] * billete1
        dic_billete1["saldo"][0] = dic_billete1["entrada"][0] - dic_billete1["salida"][0]
        dic_billete1["saldo"][1] = dic_billete1["entrada"][1] - dic_billete1["salida"][1]
    except:
        pass

    try:
        dic_billete2["entrada"][1] = dic_billete2["entrada"][0] * billete2
        dic_billete2["salida"][1] = dic_billete2["salida"][0] * billete2
        dic_billete2["saldo"][0] = dic_billete2["entrada"][0] - dic_billete2["salida"][0]
        dic_billete2["saldo"][1] = dic_billete2["entrada"][1] - dic_billete2["salida"][1]
    except:
        pass

    try:
        dic_billete3["entrada"][1] = dic_billete3["entrada"][0] * billete3
        dic_billete3["salida"][1] = dic_billete3["salida"][0] * billete3
        dic_billete3["saldo"][0] = dic_billete3["entrada"][0] - dic_billete3["salida"][0]
        dic_billete3["saldo"][1] = dic_billete3["entrada"][1] - dic_billete3["salida"][1]
    except:
        pass

    try:
        dic_billete4["entrada"][1] = dic_billete4["entrada"][0] * billete4
        dic_billete4["salida"][1] = dic_billete4["salida"][0] * billete4
        dic_billete4["saldo"][0] = dic_billete4["entrada"][0] - dic_billete4["salida"][0]
        dic_billete4["saldo"][1] = dic_billete4["entrada"][1] - dic_billete4["salida"][1]
    except:
        pass

    try:
        dic_billete5["entrada"][1] = dic_billete5["entrada"][0] * billete5
        dic_billete5["salida"][1] = dic_billete5["salida"][0] * billete5
        dic_billete5["saldo"][0] = dic_billete5["entrada"][0] - dic_billete5["salida"][0]
        dic_billete5["saldo"][1] = dic_billete5["entrada"][1] - dic_billete5["salida"][1]
    except:
        pass


    dic_total_billetes = {"entrada": [dic_billete1["entrada"][0] + dic_billete2["entrada"][0] + dic_billete3["entrada"][0] + dic_billete4["entrada"][0] + dic_billete5["entrada"][0] , dic_billete1["entrada"][1] + dic_billete2["entrada"][1] + dic_billete3["entrada"][1] + dic_billete4["entrada"][1] + dic_billete5["entrada"][1]], #(cantidad de monedas, total de dinero)
                    "salida": [dic_billete1["salida"][0] + dic_billete2["salida"][0] + dic_billete3["salida"][0] + dic_billete4["salida"][0] + dic_billete5["salida"][0] , dic_billete1["salida"][1] + dic_billete2["salida"][1] + dic_billete3["salida"][1] + dic_billete4["salida"][1] + dic_billete5["salida"][1]],
                    "saldo": [dic_billete1["saldo"][0] + dic_billete2["saldo"][0] + dic_billete3["saldo"][0] + dic_billete4["saldo"][0] + dic_billete5["saldo"][0], dic_billete1["saldo"][1] + dic_billete2["saldo"][1] + dic_billete3["saldo"][1] + dic_billete4["saldo"][1] + dic_billete5["saldo"][1]]}
    
# esta funcion permite leer los datos de los archivos y asignarlos a las estructuras y variables del programa
#E:
#S: 
def leer_archivos():
    global num_espacios, precio_x_hora, pago_minimo, redondeo_tiempo, minutos_max, moneda1, moneda2, moneda3, billete1, billete2, billete3, billete4, billete5
    
    # leer archivo de configuración
    try:
        archivo_configuracion = open("configuración.dat", "r")
        num_espacios = archivo_configuracion.readline()[:-1]
        try:
            num_espacios = int(num_espacios)
        except:
            pass
        precio_x_hora = eval(archivo_configuracion.readline()[:-1])
        try:
            precio_x_hora = float(precio_x_hora)
        except:
            pass
        pago_minimo = eval(archivo_configuracion.readline()[:-1])
        try:
            pago_minimo = int(pago_minimo)
        except:
            pass
        redondeo_tiempo = eval(archivo_configuracion.readline()[:-1])
        try:
            redondeo_tiempo = int(redondeo_tiempo)
        except:
            pass
        minutos_max = eval(archivo_configuracion.readline()[:-1])
        try:
            minutos_max = int(minutos_max)
        except:
            pass
        moneda1 = eval(archivo_configuracion.readline()[:-1])
        try:
            moneda1 = int(moneda1)
        except:
            pass
        moneda2 = eval(archivo_configuracion.readline()[:-1])
        try:
            moneda2 = int(moneda2)
        except:
            pass
        moneda3 = eval(archivo_configuracion.readline()[:-1])
        try:
            moneda3 = int(moneda3)
        except:
            pass
        billete1 = eval(archivo_configuracion.readline()[:-1])
        try:
            billete1 = int(billete1)
        except:
            pass
        billete2 = eval(archivo_configuracion.readline()[:-1])
        try:
            billete2 = int(billete2)
        except:
            pass
        billete3 = eval(archivo_configuracion.readline()[:-1])
        try:
            billete3 = int(billete3)
        except:
            pass
        billete4 =eval(archivo_configuracion.readline()[:-1])
        try:
            billete4 = int(billete4)
        except:
            pass
        billete5 = eval(archivo_configuracion.readline()[:-1])
        try:
            billete5 = int(billete5)
        except:
            pass
    except: # cuando el archivo no existe se inicializan los datos respectivos
        num_espacios = 0
        precio_x_hora = ""
        pago_minimo = ""
        redondeo_tiempo = ""
        minutos_max = ""
        moneda1 = ""
        moneda2 = ""
        moneda3 = ""
        billete1 = ""
        billete2 = ""
        billete3 = ""
        billete4 = ""
        billete5 = ""

    # leer archivo de parqueo
    try:
        archivo_parqueo = open("parqueo.dat", "rb")
        parqueo = pickle.load(archivo_parqueo)
        archivo_parqueo.close()
    except: # cuando el archivo no existe se inicializan los datos respectivos
        parqueo = []

    
    # leer archivo de historial_parqueo
    try:
        archivo_historial_parqueo = open("historial_parqueo.dat", "rb")
        historial_parqueo = pickle.load(archivo_historial_parqueo)
        archivo_historial_parqueo.close()
    except: # cuando el archivo no existe se inicializan los datos respectivos
        historial_parqueo = []

    # leer archivo de cajero
    try:
        archivo_cajero = open("cajero.dat", "rb")
        cajero_datos = pickle.load(archivo_cajero)
        archivo_cajero.close()
    except: # cuando el archivo no existe se inicializan los datos respectivos
        dic_moneda1 = {"entrada": [0, 0], "salida": [0,0], "saldo": [0,0]}
        dic_moneda2 = {"entrada": [0,0], "salida": [0,0], "saldo": [0,0]}
        dic_moneda3 = {"entrada": [0,0], "salida": [0,0], "saldo": [0,0]}
        dic_billete1 = {"entrada": [0,0], "salida": [0,0], "saldo": [0,0]}
        dic_billete2 = {"entrada": [0,0], "salida": [0,0], "saldo": [0,0]}
        dic_billete3 = {"entrada": [0,0], "salida": [0,0], "saldo": [0,0]}
        dic_billete4 = {"entrada": [0,0], "salida": [0,0], "saldo": [0,0]}
        dic_billete5 = {"entrada": [0,0], "salida": [0,0], "saldo": [0,0]}
        cajero_datos = [dic_moneda1, dic_moneda2, dic_moneda3, dic_billete1, dic_billete2, dic_billete3, dic_billete4, dic_billete5]

    return num_espacios, precio_x_hora, pago_minimo, redondeo_tiempo, minutos_max, parqueo, historial_parqueo, moneda1, moneda2, moneda3, billete1, billete2, billete3, billete4, billete5, cajero_datos[0], cajero_datos[1], cajero_datos[2], cajero_datos[3], cajero_datos[4], cajero_datos[5], cajero_datos[6], cajero_datos[7]
#esta funcion permite grabar datos en los archivos
#datos del 
#archivos grabados
def grabar_archivos(num_espacios, precio_x_hora, pago_minimo, redondeo_tiempo, minutos_max, parqueo, historial_parqueo, moneda1, moneda2, moneda3, billete1, billete2, billete3, billete4, billete5, dic_moneda1, dic_moneda2, dic_moneda3, dic_billete1, dic_billete2, dic_billete3, dic_billete4, dic_billete5):
    # grabar archivo de configuración (archivo tipo string por líneas.)
    archivo_configuracion = open("configuración.dat", "w")
    archivo_configuracion.write(str(num_espacios) + "\n")
    archivo_configuracion.write(str(precio_x_hora) + "\n")
    archivo_configuracion.write(str(pago_minimo) + "\n")
    archivo_configuracion.write(str(redondeo_tiempo) + "\n")
    archivo_configuracion.write(str(minutos_max) + "\n")
    archivo_configuracion.write(str(moneda1) + "\n")
    archivo_configuracion.write(str(moneda2) + "\n")
    archivo_configuracion.write(str(moneda3) + "\n")
    archivo_configuracion.write(str(billete1) + "\n")
    archivo_configuracion.write(str(billete2) + "\n")
    archivo_configuracion.write(str(billete3) + "\n")
    archivo_configuracion.write(str(billete4) + "\n")
    archivo_configuracion.write(str(billete5) + "\n")
    archivo_configuracion.close()

    # grabar archivo de parqueo (archivo tipo binario)
    archivo_parqueo = open("parqueo.dat", "wb")
    pickle.dump(parqueo, archivo_parqueo)
    archivo_parqueo.close()

    # grabar archivo de historial_parqueo (archivo tipo binario)
    archivo_historial_parqueo = open("historial_parqueo.dat", "wb")
    pickle.dump(historial_parqueo, archivo_historial_parqueo)
    archivo_historial_parqueo.close()

    # grabar archivo de cajero (archivo tipo binario)
    archivo_cajero = open("cajero.dat", "wb")
    pickle.dump([dic_moneda1, dic_moneda2, dic_moneda3, dic_billete1, dic_billete2, dic_billete3, dic_billete4, dic_billete5], archivo_cajero)
    archivo_cajero.close()

#esta funcion se encarga de verificar el tamaño de un string
#entrada: un string, dos int
#salida: un booleano
def verificar_string(string, de, hasta):
    if len(string) >= de and len(string) <= hasta:
        return True
    else:
        return False

#esta funcion se encarga de verificar el tamaño de un entero
#entrada: un entero, tamaño mayor a y menor a 
#salida: un booleano
def verificar_entero(entero, mayor_igual, menor_igual):
    if isinstance(entero, int) == False:
        return False
    else:
        if mayor_igual == "x" and menor_igual == "x": #solo verifica que sea un entero
            return True
        elif mayor_igual == "x": #solo verifica que sea menor o igual a un numero
            if entero <= menor_igual:
                return True
            else:
                return False
        elif menor_igual == "x": #solo verifica que sea mayor o igual a un numero
            if entero >= mayor_igual:
                return True
            else:
                return False
        else: #verifica que sea mayor o igual a un numero y menor o igual a otro
            if entero <= menor_igual:
                if entero >= mayor_igual:
                    return True
                else:
                    return False
            else:
                return False

#esta funcion verifica que los datos de configuracion fueron llenados
def verificar_datos_conf():
    global num_espacios, precio_x_hora, pago_minimo, redondeo_tiempo, minutos_max, moneda1, moneda2, moneda3, billete1, billete2, billete3, billete4, billete5, parqueo
    if parqueo != [] and num_espacios != "" and precio_x_hora != "" and pago_minimo != "" and redondeo_tiempo != "" and minutos_max != "" and moneda1 != "" and moneda2 != "" and moneda3 != "" and billete1 != "" and billete2 != "" and billete3 != "" and billete4 != "" and billete5 != "":
        return True
    else:
        return False

#esta funcion permite vaciar el cajero
def vaciar_cajero():
    global dic_moneda1, dic_moneda2, dic_moneda3, dic_billete1, dic_billete2, dic_billete3, dic_billete4, dic_billete5, moneda1, moneda2, moneda3, billete1, billete2, billete3, billete4, billete5, dic_total_monedas, dic_total_billetes
    lista_dinero = [[dic_moneda1, moneda1], [dic_moneda2, moneda2], [dic_moneda3, moneda3], [dic_billete1, billete1], [dic_billete2, billete2], [dic_billete3, billete3], [dic_billete4, billete4], [dic_billete5, billete5]]
    for diccionario_moneda in lista_dinero:
        diccionario_moneda[0]["entrada"][0] = 0
        diccionario_moneda[0]["salida"][0] = 0
        #refrescar los demás valores
        diccionario_moneda[0]["entrada"][1] = diccionario_moneda[0]["entrada"][0] * diccionario_moneda[1]
        diccionario_moneda[0]["salida"][1] = diccionario_moneda[0]["salida"][0] * diccionario_moneda[1]
        diccionario_moneda[0]["saldo"][0] = diccionario_moneda[0]["entrada"][0] - diccionario_moneda[0]["salida"][0]
        diccionario_moneda[0]["saldo"][1] = diccionario_moneda[0]["entrada"][1] - diccionario_moneda[0]["salida"][1]
    dic_total_monedas = {"entrada": [dic_moneda1["entrada"][0] + dic_moneda2["entrada"][0] + dic_moneda3["entrada"][0] , dic_moneda1["entrada"][1] + dic_moneda2["entrada"][1] + dic_moneda3["entrada"][1]], #(cantidad de monedas, total de dinero)
                "salida": [dic_moneda1["salida"][0] + dic_moneda2["salida"][0] + dic_moneda3["salida"][0] , dic_moneda1["salida"][1] + dic_moneda2["salida"][1] + dic_moneda3["salida"][1]],
                "saldo": [dic_moneda1["saldo"][0] + dic_moneda2["saldo"][0] + dic_moneda3["saldo"][0] , dic_moneda1["saldo"][1] + dic_moneda2["saldo"][1] + dic_moneda3["saldo"][1]]}

    dic_total_billetes = {"entrada": [dic_billete1["entrada"][0] + dic_billete2["entrada"][0] + dic_billete3["entrada"][0] + dic_billete4["entrada"][0] + dic_billete5["entrada"][0] , dic_billete1["entrada"][1] + dic_billete2["entrada"][1] + dic_billete3["entrada"][1] + dic_billete4["entrada"][1] + dic_billete5["entrada"][1]], #(cantidad de monedas, total de dinero)
                "salida": [dic_billete1["salida"][0] + dic_billete2["salida"][0] + dic_billete3["salida"][0] + dic_billete4["salida"][0] + dic_billete5["salida"][0] , dic_billete1["salida"][1] + dic_billete2["salida"][1] + dic_billete3["salida"][1] + dic_billete4["salida"][1] + dic_billete5["salida"][1]],
                "saldo": [dic_billete1["saldo"][0] + dic_billete2["saldo"][0] + dic_billete3["saldo"][0] + dic_billete4["saldo"][0] + dic_billete5["saldo"][0], dic_billete1["saldo"][1] + dic_billete2["saldo"][1] + dic_billete3["saldo"][1] + dic_billete4["saldo"][1] + dic_billete5["saldo"][1]]}
    

#esta funcion permite mostrar los datos en tiempo real de las variables en la parte de cargar cajero
#cajita es lo que se escribe en la caja de texto
#saldo_antes es el saldo anterior
#moneda es el valor de la moneda
def sumar_tiempo_real(n, cajita, texto, saldo_antes, moneda):
    try:
        numero = int(cajita)
        resultado = (numero + saldo_antes) * moneda
        texto.config(text=f"{resultado}")
    except:
        texto.config(text="Resultado")

#esta funcion permite sumar varias monedas
def sumar_num(n, mon1, mon2, mon3, texto):
    try:
        resultado = int(mon1) + int(mon2) + int(mon3)
        texto.config(text=f"{resultado}")
    except:
        texto.config(text="Resultado")

#esta funcion permite sumar varios
def sumar_num_bill(n, bill1, bill2, bill3, bill4, bill5, texto):
    try:
        resultado = int(bill1) + int(bill2) + int(bill3) + int(bill4) + int(bill5)
        texto.config(text=f"{resultado}")
    except:
        texto.config(text="Resultado")

#esta funcion permite actualizar el saldo del cajero
def actualizar_saldo(c_mon1, c_mon2, c_mon3, c_bill1, c_bill2, c_bill3, c_bill4, c_bill5, t_mon1, t_mon2, t_mon3, t_bill1, t_bill2, t_bill3, t_bill4, t_bill5, c_total_mon, c_total_bill, t_total_mon, t_total_bill):
    global dic_total_billetes, dic_total_monedas
    try:
        c_mon1 = int(c_mon1)
        c_mon2 = int(c_mon2)
        c_mon3 = int(c_mon3)
        c_bill1 = int(c_bill1)
        c_bill2 = int(c_bill2)
        c_bill3 = int(c_bill3)
        c_bill4 = int(c_bill4)
        c_bill5 = int(c_bill5)
        t_mon1 = int(t_mon1)
        t_mon2 = int(t_mon2)
        t_mon3 = int(t_mon3)
        t_bill1 = int(t_bill1)
        t_bill2 = int(t_bill2)
        t_bill3 = int(t_bill3)
        t_bill4 = int(t_bill4)
        t_bill5 = int(t_bill5)
        c_total_mon = int(c_total_mon)
        t_total_mon = int(t_total_mon)
        c_total_bill = int(c_total_bill)
        t_total_bill = int(t_total_bill)

        dic_moneda1["saldo"][0] = c_mon1
        dic_moneda1["saldo"][1] = t_mon1
        dic_moneda2["saldo"][0] = c_mon2
        dic_moneda2["saldo"][1] = t_mon2
        dic_moneda3["saldo"][0] = c_mon3
        dic_moneda3["saldo"][1] = t_mon3
        dic_billete1["saldo"][0] = c_bill1
        dic_billete1["saldo"][1] = t_bill1
        dic_billete2["saldo"][0] = c_bill2
        dic_billete2["saldo"][1] = t_bill2
        dic_billete3["saldo"][0] = c_bill3
        dic_billete3["saldo"][1] = t_bill3
        dic_billete4["saldo"][0] = c_bill4
        dic_billete4["saldo"][1] = t_bill4
        dic_billete5["saldo"][0] = c_bill5
        dic_billete5["saldo"][1] = t_bill5

        dic_total_monedas["saldo"][0] = c_total_mon
        dic_total_monedas["saldo"][1] = t_total_mon
        dic_total_billetes["saldo"][0] = c_total_bill
        dic_total_billetes["saldo"][1] = t_total_bill
        return True
    except:
        messagebox.showerror("ERROR", "Los datos ingresados deben de ser enteros mayores o iguales a 0")
        return False

#esta funcion permite actualizaar el valor de las entradas del cajero
def actualizar_entradas(c_mon1, c_mon2, c_mon3, c_bill1, c_bill2, c_bill3, c_bill4, c_bill5, t_mon1, t_mon2, t_mon3, t_bill1, t_bill2, t_bill3, t_bill4, t_bill5, c_total_mon, c_total_bill, t_total_mon, t_total_bill):
    c_mon1 = int(c_mon1)
    c_mon2 = int(c_mon2)
    c_mon3 = int(c_mon3)
    c_bill1 = int(c_bill1)
    c_bill2 = int(c_bill2)
    c_bill3 = int(c_bill3)
    c_bill4 = int(c_bill4)
    c_bill5 = int(c_bill5)
    t_mon1 = int(t_mon1)
    t_mon2 = int(t_mon2)
    t_mon3 = int(t_mon3)
    t_bill1 = int(t_bill1)
    t_bill2 = int(t_bill2)
    t_bill3 = int(t_bill3)
    t_bill4 = int(t_bill4)
    t_bill5 = int(t_bill5)
    c_total_mon = int(c_total_mon)
    t_total_mon = int(t_total_mon)
    c_total_bill = int(c_total_bill)
    t_total_bill = int(t_total_bill)

    dic_moneda1["entrada"][0] += int(c_mon1)
    dic_moneda1["entrada"][1] += int(t_mon1)
    dic_moneda2["entrada"][0] += int(c_mon2)
    dic_moneda2["entrada"][1] += int(t_mon2)
    dic_moneda3["entrada"][0] += int(c_mon3)
    dic_moneda3["entrada"][1] += int(t_mon3)
    dic_billete1["entrada"][0] += int(c_bill1)
    dic_billete1["entrada"][1] += int(t_bill1)
    dic_billete2["entrada"][0] += int(c_bill2)
    dic_billete2["entrada"][1] += int(t_bill2)
    dic_billete3["entrada"][0] += int(c_bill3)
    dic_billete3["entrada"][1] += int(t_bill3)
    dic_billete4["entrada"][0] += int(c_bill4)
    dic_billete4["entrada"][1] += int(t_bill4)
    dic_billete5["entrada"][0] += int(c_bill5)
    dic_billete5["entrada"][1] += int(t_bill5)

    dic_total_monedas["entrada"][0] += int(c_total_mon)
    dic_total_monedas["entrada"][1] += int(t_total_mon)
    dic_total_billetes["entrada"][0] += int(c_total_bill)
    dic_total_billetes["entrada"][1] += int(t_total_bill)

#esta funcion permite contar el numero de los espacios disponibles en el parque
def num_espacios_parqueo():
    global parqueo
    resultado = 0
    for cada_parqueo in parqueo:
        if cada_parqueo == []:
            resultado +=1
    return resultado
    
#esta funcion permite encontrar un parqueo para el auto(retorna el indice)
def buscar_parqueo():
    global parqueo
    contador = 0
    for cada_parqueo in parqueo:
        if cada_parqueo == []:
            break
        contador += 1
    return contador

#esta funcion toma la hora actual para mostrarla en tiempo real
def actualizar_tiempo(hora_de_entrada):
    hora_fecha2 = datetime.now().strftime('%d/%m/%Y %H:%M')
    hora_de_entrada.config(text=f"{hora_fecha2}")


#esta funcion convierte un string en fecha
def convertir_string_fecha(string):
    try:
        string = datetime.strptime(string, '%d/%m/%Y').date()
        return string
    except: 
        messagebox.showerror("ERROR", "Ingrese una fecha válida")

#esta funcion despliega una ventana indicando que no hay espacio
def no_hay_espacio():
    os.system("cls")
    v_no_espacio = Toplevel()#nueva ventana
    v_no_espacio.title("ESTACIONAMIENTO - ENTRADA DEL VEHICULO")
    v_no_espacio.geometry("300x150")#dimensiones de la ventana
    v_no_espacio.focus()#para que seleccione la ventana abierta
    v_no_espacio.grab_set()#evita usar la ventana principal a menos que se haya cerrado la ventana abierta
    frame = Frame(v_no_espacio)
    frame.place(relheight=1, relwidth=1)
    no_espacio = Label(frame, text="NO HAY ESPACIO")
    no_espacio.config(font=("Verdana", 15), fg="red")
    no_espacio.place(anchor="center", relx=0.5, rely=0.5)


#esta funcion verifica si el auto ya está en el estacionamiento
def verificar_placa(placa):
    global parqueo
    for cada_parqueo in parqueo:
        try:
            if cada_parqueo[0] == placa:
                messagebox.showerror("ERROR", "Este auto ya está en el parqueo, verifique la placa")
                return False
        except:
            pass
    return True

#esta funcion agrega un vehiculo al estacionamiento
def reservar_espacio(placa, campo, hora_entrada):
    global parqueo
    if verificar_string(placa, 1, 8) == False:
        messagebox.showerror("ERROR", "La placa debe de tener entre 1 y 8 caracteres")
        return False
    parqueo[int(campo) - 1] = [placa, hora_entrada, "", 0]
    return True
    
#esta funcion destruye todos los widgets de cajero exceptuando la entrada de la placa
def destruir_widgets_cajero(frame):
    num = "1234567890"
    for widget in frame.winfo_children():
        if "entry" in str(widget): #evitamos destruir la entrada de la placa
            if str(widget).endswith("1") == True or str(widget).endswith("2") == True or str(widget).endswith("3") == True or str(widget).endswith("4") == True or str(widget).endswith("5") == True or str(widget).endswith("6") == True or str(widget).endswith("7") == True or str(widget).endswith("8") == True or str(widget).endswith("9") == True or str(widget).endswith("10") == True:
                widget.destroy()
                #si entra aqui quiere decir que es un widget diferente al de la entrada de la placa
            else:
                pass
        else:
            widget.destroy()

#esta funcion convierte de segundos a dias, horas y minutos
def segundos_a_segundos_minutos_y_horas(segundos):
    horas = int(segundos / 60 / 60)
    segundos -= horas*60*60
    minutos = int(segundos/60)
    segundos -= minutos*60

    #---------------------------
    dias = horas // 24
    horas = horas % 24
    return dias, horas, minutos

#busca la placa solicitada
def datos_placa(placa):
    global parqueo, minutos_max, historial_parqueo
    i = 0
    for cada_parqueo in parqueo:
        try:
            if cada_parqueo[0] == placa:
                if cada_parqueo[2] == "":
                    return cada_parqueo, "x"
                else:
                    diferencia = (datetime.now() - de_string_a_fecha_con_hora(cada_parqueo[2])).total_seconds()
                    if minutos_max == 0:
                        return False, "x"
                    elif (minutos_max*60) > diferencia:
                        return False, "x"
                    else:
                        historial_parqueo.append([cada_parqueo[0], i+1, cada_parqueo[1], cada_parqueo[2], cada_parqueo[3], str(datetime.now().strftime('%d/%m/%Y %H:%M'))])#se pasó el tiempo, por lo que se agrega el pago anterior a historial parqueo
                        cada_parqueo[1] = cada_parqueo[2]
                        cada_parqueo[2] = ""
                        cada_parqueo[3] = 0
                        return cada_parqueo, (segundos_a_segundos_minutos_y_horas(int(diferencia)))#h, m, s
        except:
            pass
        i += 1 
    return False, "x"

#esta funcion convierte un string a una fecha con hora
def de_string_a_fecha_con_hora(str):
    return datetime.strptime(str, '%d/%m/%Y %H:%M')

#esta funcion calcula el cobro
def calcular_cobro(d, h, m):
    global precio_x_hora, pago_minimo, redondeo_tiempo
    horas = int(str(d)) * 24 + int(h)
    mins = int(m) 
    #caso 1: pago minimo y redondeo son distintos a 0
    if pago_minimo != 0 and redondeo_tiempo != 0:
        minuto_redondeado = (((mins//redondeo_tiempo) * redondeo_tiempo) + redondeo_tiempo)
        minuto_redondeado = (precio_x_hora/60) * minuto_redondeado
        resultado = int((horas * precio_x_hora) + minuto_redondeado)
        if resultado < pago_minimo:
            return pago_minimo
        else:
            return resultado
        
    #caso 2 pago minimo es 0 y redondeo distinto a 0
    elif pago_minimo == 0 and redondeo_tiempo != 0:
        minuto_redondeado = (((mins//redondeo_tiempo) * redondeo_tiempo) + redondeo_tiempo)
        minuto_redondeado = (precio_x_hora/60) * minuto_redondeado
        resultado = int((horas * precio_x_hora) + minuto_redondeado)
        return resultado

    #caso 3: pago minimo es distinto a 0 y redondeo es 0
    elif pago_minimo != 0 and redondeo_tiempo == 0:
        resultado = (horas * precio_x_hora) + (mins * (precio_x_hora/60))
        if resultado < pago_minimo:
            return pago_minimo
        else:
            return int(resultado)
    #caso 4: pago minimo y redondeo son 0
    else:
        return int((horas * precio_x_hora) + (mins * (precio_x_hora/60)))



#esta funcion aumenta el pago por cada boton seleccionado en la parte de cajero
def aumentar_pago(monto_pago, pago, a_pagar_int, monto_pago_int):
    if monto_pago_int >= a_pagar_int:
        pass
    else:
        num = monto_pago.cget("text")
        num = int(num)
        monto_pago.config(font= ("Verdana", 13), text=f"{num + int(pago)}")

#esta funcion aumenta el num de monedas y billetes utilizados
def sumar_mon(mon, a_pagar_int, monto_pago_int):
    if monto_pago_int >= a_pagar_int:
        pass
    else:
        valor = mon.get()
        mon.set(value=valor + 1)

#esta funcion refresca cajero tras anular o realizar un pago
def refrescar_cajero(vcajero):
    frame = Frame(vcajero)
    frame.place(relheight=1, relwidth=1)
    titulo = Label(frame, text="CAJERO", borderwidth=10, relief="sunken").place(anchor="center", relx=0.5, rely=0.06)
    xx_por_hora = Label(frame, text=f"{precio_x_hora} POR HORA").place(anchor="center", relx=0.7, rely=0.06)
    Paso1 = Label(frame, text="PASO 1: SU PLACA").place(anchor="center", relx=0.1, rely=0.12)
    insertar_placa = Entry(frame)
    insertar_placa.place(anchor="center", relx=0.3, rely=0.12)
    insertar_placa.bind("<KeyRelease>", lambda e: cajero_parqueo2(frame, insertar_placa.get(), vcajero))

#esta funcion devuelve el siguiente numero mas cercano al segundo argumento, el cual es divisible por el primer argumento, esto para poder devolver correctamente el vuelto
def multiplo_de_cercano(num, num_cercano):
    if num == 0 or num_cercano == 0:    #validacion
        return 0
    elif (num_cercano / num) - int(num_cercano/num) != 0:
        valor1 = int(num_cercano / num) * num + num
        return valor1
    else:
        return num_cercano
    
#esta funcion busca la moneda de menos valor entre todas
def moneda_menos_valor(mon1, mon2, mon3, bill1, bill2, bill3, bill4, bill5):
    orden = [mon1, mon2, mon3, bill1, bill2, bill3, bill4, bill5]
    resultado = []
    for elemento in orden:
        if elemento != 0:
            resultado.append(elemento)
    resultado.sort()
    return resultado[0]

#esta funcion calcula el cambio que debe de dar
def cambio_calculo(mon1, mon2, mon3, bill1, bill2, bill3, bill4, bill5, cambio):
    if bill5 != 0:
        cambio_bill5 = cambio // bill5
        cambio = cambio % bill5
    else:
        cambio_bill5 = 0
    if bill4 != 0:
        cambio_bill4 = cambio // bill4
        cambio = cambio % bill4
    else:
        cambio_bill4 = 0
    if bill3 != 0:
        cambio_bill3 = cambio // bill3
        cambio = cambio % bill3
    else:
        cambio_bill3 = 0
    if bill2 != 0:
        cambio_bill2 = cambio // bill2
        cambio = cambio % bill2
    else:
        cambio_bill2 = 0
    if bill1 != 0:
        cambio_bill1 = cambio // bill1
        cambio = cambio % bill1
    else:
        cambio_bill1 = 0
    if mon3 != 0:
        cambio_mon3 = cambio // mon3
        cambio = cambio % mon3
    else:
        cambio_mon3 = 0
    if mon2 != 0:
        cambio_mon2 = cambio // mon2
        cambio = cambio % mon2
    else:
        cambio_mon2 = 0
    if mon1 != 0:
        cambio_mon1 = cambio // mon1
    else:
        cambio_mon1 = 0
    return [cambio_bill5, cambio_bill4, cambio_bill3, cambio_bill2, cambio_bill1, cambio_mon3, cambio_mon2, cambio_mon1]


#esta funcion verifica si existe esa cantidad de monedas en el cajero para ser devueltas
#cada_dic,cada_mon y lista_vuelto, lista_mon_ingresadas va en el orden: bill5, bill4..., mon3, mon2....
def hay_monedas(lista_vuelto, lista_mon_ingresadas, cada_dic, cada_mon):
    global dic_billete5, dic_billete4, dic_billete3, dic_billete2, dic_billete1, dic_moneda3, dic_moneda2, dic_moneda1
    #este for es para verificar que si se pueda efectuar el cobro antes de bajar la cantidad de monedas y billetes
    i = 0
    for cada_cambio in lista_vuelto:
        if cada_dic[i]["saldo"][0] < cada_cambio:
            #solo_hay = cada_dic[i]["saldo"][0]  #esta es la cantidad que se puede tomar del cajero
            necesita = (cada_cambio - cada_dic[i]["saldo"][0])    #esta es la cantidad que necesitamos de otra moneda
            habian_mon = False
            i_prox_mon = i + 1
            for moneda in cada_mon:
                #error de range
                try:
                    if (necesita * cada_mon[i]) % cada_mon[i_prox_mon] == 0:    #quiere decir que si es posible tomar esa cantidad
                        if cada_dic[i_prox_mon]["saldo"][0] >= (necesita * cada_mon[i]) / cada_mon[i_prox_mon]:     #quiere decir que si hay la cantidad que se necesita
                            lista_vuelto[i_prox_mon] += (necesita * cada_mon[i]) / cada_mon[i_prox_mon] #le agregamos la cantidad de monedas 
                            lista_vuelto[i] -= necesita #le restamos la cantidad que necesitaba
                            habian_mon = True
                            break
                    i_prox_mon +=1
                except:
                    pass
            if habian_mon == False:
                messagebox.showerror("ERROR", "No hay monedas o billetes suficientes para poder devolver el vuelto, debe de realizar el pago con tarjeta o esperar a que el cajero sea cargado")
                return False
        i += 1

    #este for quiere decir que si se puede realizar el cobro, por lo tanto se efectua
    agregar_monedas(lista_mon_ingresadas, cada_dic, cada_mon)
    restar_monedas(lista_vuelto, cada_dic, cada_mon)
    return lista_vuelto


#esta funcion se encarga de sumar las monedas a las entradas y el saldo del cajero
def agregar_monedas(lista_mon_ingresadas, cada_dic, cada_mon):
    global dic_billete5, dic_billete4, dic_billete3, dic_billete2, dic_billete1, dic_moneda3, dic_moneda2, dic_moneda1, dic_total_billetes, dic_total_monedas
    i = 0
    for dic in cada_dic:
        dic["entrada"][0] += int(lista_mon_ingresadas[i])
        #refrescar los diccionarios
        dic["entrada"][1] = dic["entrada"][0] * cada_mon[i]
        dic["salida"][1] = dic["salida"][0] * cada_mon[i]
        dic["saldo"][0] = dic["entrada"][0] - dic["salida"][0]
        dic["saldo"][1] = dic["entrada"][1] - dic["salida"][1]
        i +=1 
    dic_total_monedas = {"entrada": [dic_moneda1["entrada"][0] + dic_moneda2["entrada"][0] + dic_moneda3["entrada"][0] , dic_moneda1["entrada"][1] + dic_moneda2["entrada"][1] + dic_moneda3["entrada"][1]], #(cantidad de monedas, total de dinero)
                "salida": [dic_moneda1["salida"][0] + dic_moneda2["salida"][0] + dic_moneda3["salida"][0] , dic_moneda1["salida"][1] + dic_moneda2["salida"][1] + dic_moneda3["salida"][1]],
                "saldo": [dic_moneda1["saldo"][0] + dic_moneda2["saldo"][0] + dic_moneda3["saldo"][0] , dic_moneda1["saldo"][1] + dic_moneda2["saldo"][1] + dic_moneda3["saldo"][1]]}

    dic_total_billetes = {"entrada": [dic_billete1["entrada"][0] + dic_billete2["entrada"][0] + dic_billete3["entrada"][0] + dic_billete4["entrada"][0] + dic_billete5["entrada"][0] , dic_billete1["entrada"][1] + dic_billete2["entrada"][1] + dic_billete3["entrada"][1] + dic_billete4["entrada"][1] + dic_billete5["entrada"][1]], #(cantidad de monedas, total de dinero)
                "salida": [dic_billete1["salida"][0] + dic_billete2["salida"][0] + dic_billete3["salida"][0] + dic_billete4["salida"][0] + dic_billete5["salida"][0] , dic_billete1["salida"][1] + dic_billete2["salida"][1] + dic_billete3["salida"][1] + dic_billete4["salida"][1] + dic_billete5["salida"][1]],
                "saldo": [dic_billete1["saldo"][0] + dic_billete2["saldo"][0] + dic_billete3["saldo"][0] + dic_billete4["saldo"][0] + dic_billete5["saldo"][0], dic_billete1["saldo"][1] + dic_billete2["saldo"][1] + dic_billete3["saldo"][1] + dic_billete4["saldo"][1] + dic_billete5["saldo"][1]]}

#esta funcion se encarga de sumar las salidas y restar el saldo del cajero
def restar_monedas(lista_vuelto, cada_dic, cada_mon):
    global dic_billete5, dic_billete4, dic_billete3, dic_billete2, dic_billete1, dic_moneda3, dic_moneda2, dic_moneda1, dic_total_billetes, dic_total_monedas
    i = 0
    for dic in cada_dic:
        dic["salida"][0] += int(lista_vuelto[i])
        #refrescar los diccionarios
        dic["entrada"][1] = dic["entrada"][0] * cada_mon[i]
        dic["salida"][1] = dic["salida"][0] * cada_mon[i]
        dic["saldo"][0] = dic["entrada"][0] - dic["salida"][0]
        dic["saldo"][1] = dic["entrada"][1] - dic["salida"][1]
        i +=1 
    dic_total_monedas = {"entrada": [dic_moneda1["entrada"][0] + dic_moneda2["entrada"][0] + dic_moneda3["entrada"][0] , dic_moneda1["entrada"][1] + dic_moneda2["entrada"][1] + dic_moneda3["entrada"][1]], #(cantidad de monedas, total de dinero)
                "salida": [dic_moneda1["salida"][0] + dic_moneda2["salida"][0] + dic_moneda3["salida"][0] , dic_moneda1["salida"][1] + dic_moneda2["salida"][1] + dic_moneda3["salida"][1]],
                "saldo": [dic_moneda1["saldo"][0] + dic_moneda2["saldo"][0] + dic_moneda3["saldo"][0] , dic_moneda1["saldo"][1] + dic_moneda2["saldo"][1] + dic_moneda3["saldo"][1]]}

    dic_total_billetes = {"entrada": [dic_billete1["entrada"][0] + dic_billete2["entrada"][0] + dic_billete3["entrada"][0] + dic_billete4["entrada"][0] + dic_billete5["entrada"][0] , dic_billete1["entrada"][1] + dic_billete2["entrada"][1] + dic_billete3["entrada"][1] + dic_billete4["entrada"][1] + dic_billete5["entrada"][1]], #(cantidad de monedas, total de dinero)
                "salida": [dic_billete1["salida"][0] + dic_billete2["salida"][0] + dic_billete3["salida"][0] + dic_billete4["salida"][0] + dic_billete5["salida"][0] , dic_billete1["salida"][1] + dic_billete2["salida"][1] + dic_billete3["salida"][1] + dic_billete4["salida"][1] + dic_billete5["salida"][1]],
                "saldo": [dic_billete1["saldo"][0] + dic_billete2["saldo"][0] + dic_billete3["saldo"][0] + dic_billete4["saldo"][0] + dic_billete5["saldo"][0], dic_billete1["saldo"][1] + dic_billete2["saldo"][1] + dic_billete3["saldo"][1] + dic_billete4["saldo"][1] + dic_billete5["saldo"][1]]}

#esta funcion se encarga de verificar si la tarjeta es valida:
def ver_tarjeta(tarjeta, frame, monto_pago, monto_a_pagar, lista_plata_ingresada,  vcajero, monto_pago_mostrar, placa):
    try:
        tarjeta = int(tarjeta)
    except:
        return
    if tarjeta >= 1000000000:
        monto_pago_mostrar.config(text=f"{monto_a_pagar}")
        cajero_parqueo3(frame, monto_pago, monto_a_pagar, lista_plata_ingresada, vcajero, placa, True)
    else:
        return

#esta funcion se encarga de actualizar los datos de la placa luego de pagar
def actualizar_datos_placa(placa, valor_pagado):
    global parqueo
    for cada_parqueo in parqueo:
        try:
            if cada_parqueo[0] == placa:
                cada_parqueo[2] = (str(datetime.now().strftime('%d/%m/%Y %H:%M')))
                cada_parqueo[3] = valor_pagado
                break
        except IndexError:
            pass

#esta funcion se encarga de verificar si el auto puede salir o no
def verificar_salida(placa):
    global parqueo, minutos_max, historial_parqueo
    i = 0 
    salio = False
    for cada_parqueo in parqueo:
        try:
            if cada_parqueo[0] == placa:
                if minutos_max == 0:
                    if cada_parqueo[2] != "":#puede salir
                        historial_parqueo.append([cada_parqueo[0], i+1, cada_parqueo[1], cada_parqueo[2], cada_parqueo[3], str(datetime.now().strftime('%d/%m/%Y %H:%M'))])
                        parqueo = []
                        salio = True
                        break
                    else:
                        messagebox.showerror("ERROR", "Debe de pagar primero antes de salir")
                        return
                elif cada_parqueo[2] == "":
                    messagebox.showerror("ERROR", "Debe de pagar primero antes de salir")
                    return
                elif ( ( de_string_a_fecha_con_hora(datetime.now().strftime('%d/%m/%Y %H:%M')) - de_string_a_fecha_con_hora(cada_parqueo[2]) ).total_seconds() )> (minutos_max*60):
                    no_puede_salir(int( ( de_string_a_fecha_con_hora(datetime.now().strftime('%d/%m/%Y %H:%M')) - de_string_a_fecha_con_hora(cada_parqueo[2]) ).total_seconds() ))
                    return
                else:   #puede salir
                    historial_parqueo.append([cada_parqueo[0], i+1, cada_parqueo[1], cada_parqueo[2], cada_parqueo[3], str(datetime.now().strftime('%d/%m/%Y %H:%M'))])
                    parqueo[i] = []
                    salio = True
                    break
            else:
                pass
        except IndexError:
            pass
        i +=1 

    if salio == False:
        messagebox.showerror("ERROR", "El auto con esta placa no se encuentra en el parqueo")
        return

#esta funcion despliega una ventana con los datos del porqué el auto no puede salir
def no_puede_salir(segundos_durado):
    global minutos_max
    mensaje = Toplevel()
    mensaje.title("NO PUEDE SALIR DEL ESTACIONAMIENTO")
    mensaje.geometry("800x600")#dimensiones de la ventana
    mensaje.focus()#para que seleccione la ventana abierta
    mensaje.grab_set()#evita usar la ventana principal a menos que se haya cerrado la ventana abierta
    frame = Frame(mensaje)
    frame.place(relheight=1, relwidth=1)
    texto = Label(frame, text="No puede salir porque excedió el tiempo permitido para ello").place(anchor="center", relx= 0.5, rely=0.1)
    texto2 = Label(frame, text=f"Tiempo máximo para salir luego del pago: {minutos_max} minutos")
    texto2.place(anchor="center", relx= 0.5, rely=0.3)
    texto3 = Label(frame, text=f"Tiempo que usted ha tardado {segundos_durado//60} minutos")
    texto3.place(anchor="center", relx= 0.5, rely=0.5)
    texto4 = Label(frame, text="Debe regresar al cajero a pagar la diferencia").place(anchor="center", relx= 0.5, rely=0.7)
    aceptar = Button(frame, borderwidth=5, text="Aceptar", command=mensaje.destroy)
    aceptar.place(anchor="center", relx=0.5, rely=0.9)


#------------------------------------------------
# OPCIÓN CONFIGURACION                                                             
#------------------------------------------------
#esta función se encarga de mostrar la opcion de la configuración del estacionamiento
def configuracion():
    for espacios in parqueo:
        if espacios != []:  #validacion
            messagebox.showerror("Error","Solo se pueden realizar cambios a la configuración si el parqueo está vacio")
            return
    os.system("cls")
    vconfiguracion = Toplevel()#nueva ventana
    vconfiguracion.title("ESTACIONAMIENTO - CONFIGURACIÓN")
    vconfiguracion.geometry("800x600")#dimensiones de la ventana
    vconfiguracion.focus()#para que seleccione la ventana abierta
    vconfiguracion.grab_set()#evita usar la ventana principal a menos que se haya cerrado la ventana abierta
    frame = Frame(vconfiguracion)
    frame.place(relheight=1, relwidth=1)
    
    titulo = Label(frame, text="ESTACIONAMIENTO - CONFIGURACIÓN", borderwidth=10, relief="sunken").place(anchor="center", relx=0.5, rely=0.06)
    no_espacios = Entry(frame)#creamos un cuadro de texto
    no_espacios.place(anchor="center", relx=0.7, rely=0.13)#posicionamos el cuadro de texto
    no_espacios_text = Label(frame, text="Cantidad de espacios en el parqueo").place(anchor="center", relx=0.3, rely=0.13)#crear texto

    precio_hora = Entry(frame)
    precio_hora.place(anchor="center", relx=0.7, rely=0.18)
    precio_hora_text = Label(frame, text="Precio por hora").place(anchor="center", relx=0.3, rely=0.18)

    pago_min = Entry(frame)
    pago_min.place(anchor="center", relx=0.7, rely=0.23)
    pago_min_text = Label(frame, text="Pago mínimo").place(anchor="center", relx=0.3, rely=0.23)

    redondeo = Entry(frame)
    redondeo.place(anchor="center", relx=0.7, rely=0.28)
    redondeo_text = Label(frame, text="Redondear el tiempo cobrado al próximo minuto").place(anchor="center", relx=0.3, rely=0.28)

    min_max = Entry(frame)
    min_max.place(anchor="center", relx=0.7, rely=0.33)
    min_max_text = Label(frame, text="Minutos máximos para salir después del pago").place(anchor="center", relx=0.3, rely=0.33)

    tipo_mon_text = Label(frame, text="Tipos de moneda").place(anchor="center", relx=0.3, rely=0.38)
    
    mon1 = Entry(frame)
    mon1.place(anchor="center", relx=0.7, rely=0.43)
    mon1_text = Label(frame, text="Moneda 1, la de menor denominación").place(anchor="center", relx=0.3, rely=0.43)

    mon2 = Entry(frame)
    mon2.place(anchor="center", relx=0.7, rely=0.48)
    mon2_text = Label(frame, text="Moneda 2, denominación siguiente a la anterior").place(anchor="center", relx=0.3, rely=0.48)

    mon3 = Entry(frame)
    mon3.place(anchor="center", relx=0.7, rely=0.53)
    mon3_text = Label(frame, text="Moneda 3, denominación siguiente a la anterior").place(anchor="center", relx=0.3, rely=0.53)

    tipo_bill_text = Label(frame, text="Tipos de billetes").place(anchor="center", relx=0.3, rely=0.58)

    bill1 = Entry(frame)
    bill1.place(anchor="center", relx=0.7, rely=0.63)
    bill1_text = Label(frame, text="Billete 1, el de menor denominación").place(anchor="center", relx=0.3, rely=0.63)

    bill2 = Entry(frame)
    bill2.place(anchor="center", relx=0.7, rely=0.68)
    bill2_text = Label(frame, text="Billete 2, denominación siguiente a la anterior").place(anchor="center", relx=0.3, rely=0.68)

    bill3 = Entry(frame)
    bill3.place(anchor="center", relx=0.7, rely=0.73)
    bill3_text = Label(frame, text="Billete 3, denominación siguiente a la anterior").place(anchor="center", relx=0.3, rely=0.73)

    bill4 = Entry(frame)
    bill4.place(anchor="center", relx=0.7, rely=0.78)
    bill4_text = Label(frame, text="Billete 4, denominación siguiente a la anterior").place(anchor="center", relx=0.3, rely=0.78)

    bill5 = Entry(frame)
    bill5.place(anchor="center", relx=0.7, rely=0.83)
    bill5_text = Label(frame, text="Billete 5, denominación siguiente a la anterior").place(anchor="center", relx=0.3, rely=0.83)

    ok = Button(frame, text="Ok", borderwidth=5, command=lambda: vconfiguracion.destroy() if datos_conf(no_espacios.get(), precio_hora.get(), pago_min.get(), redondeo.get(), min_max.get(), mon1.get(), mon2.get(), mon3.get(), bill1.get(), bill2.get(), bill3.get(), bill4.get(), bill5.get()) == True else None).place(anchor="center", relx=0.4, rely =0.93)
    #.get obtiene los datos del cuadro de texto y lambda permite llamar a dos funciones con un solo boton
    #se utiliza lambda debido a la naturaleza del argumento command, este no permite llamar a mas funciones, por lo que se debe de utilizar solo una
    #True quiere decir que todo ocurrio con exito y cierra la ventana, none quiere decir que hubo un error, entonces se mantiene abierta la ventana para corregir el error
    cancelar = Button(frame, text="Cancelar", borderwidth=5, command=vconfiguracion.destroy).place(anchor="center", relx=0.55, rely =0.93)



def datos_conf(no_espacios, precio_hora, pago_min, redondeo, min_max, mon1, mon2, mon3, bill1, bill2, bill3, bill4, bill5):
    global num_espacios, precio_x_hora, pago_minimo, redondeo_tiempo, minutos_max, moneda1, moneda2, moneda3, billete1, billete2, billete3, billete4, billete5, parqueo
    #verificar: no_espacios
    if no_espacios == "":
        pass
    else:
        try:
            no_espacios = int(no_espacios)
        except ValueError:
            messagebox.showerror("Error","El número de espacios debe ser un entero mayor o igual a 1")
            return
        if verificar_entero(no_espacios, 1, "x") == False:
            messagebox.showerror("Error","El número de espacios debe ser un entero mayor o igual a 1")
            return
    
    # precio_hora
    if precio_hora == "":
        pass
    else:
        #---------------------------------------------------------------------#Verificar no. de decimales
        desde = 1
        for elemento in precio_hora:
            if elemento == ".":
                if len(precio_hora[desde:]) > 2:
                    messagebox.showerror("Error","El precio por hora debe ser un flotante con máximo 2 decimales, mayor o igual a 0")
                    return
                else:
                    break
            desde += 1
        #----------------------------------------------------------------------
        try:
            precio_hora = float(precio_hora)
        except ValueError:
            messagebox.showerror("Error","El precio por hora debe ser un flotante con máximo 2 decimales, mayor o igual a 0")
            return
            #----------------------------------------------------------------------#verificar que no sea negativo(ocurre un error si no se hace)
        if precio_hora < 0:
            messagebox.showerror("Error","El precio por hora debe ser un flotante con máximo 2 decimales, mayor o igual a 0")
            return
        #----------------------------------------------------------------------
        if verificar_entero(int(precio_hora), 0, "x") == False:
            messagebox.showerror("Error","El precio por hora debe ser un flotante con máximo 2 decimales, mayor o igual a 0")
            return
    
    # pago_min
    if pago_min == "":
        pass
    else:
        try:
            pago_min = int(pago_min)
        except ValueError:
            messagebox.showerror("Error","El pago mínimo debe ser un entero mayor o igual a 0")
            return
        if verificar_entero(pago_min, 0, "x") == False:
            messagebox.showerror("Error","El pago mínimo debe ser un entero mayor o igual a 0")
            return

    # redondeo
    if redondeo == "":
        pass
    else:
        try:
            redondeo = int(redondeo)
        except ValueError:
            messagebox.showerror("Error","El redondeo debe ser un entero entre 0 y 60")
            return
        if verificar_entero(redondeo, 0, 60) == False:
            messagebox.showerror("Error","El redondeo debe ser un entero entre 0 y 60")
            return
        
    # min_max
    if min_max == "":
        pass
    else:
        try:
            min_max = int(min_max)
        except ValueError:
            messagebox.showerror("Error","Los minutos máximos debe ser un entero mayor o igual a 0")
            return
        if verificar_entero(min_max, 0, "x") == False:
            messagebox.showerror("Error","Los minutos máximos debe ser un entero mayor o igual a 0")
            return


    # mon1
    if mon1 == "":
        pass
    else:
        try:
            mon1 = int(mon1)
        except ValueError:
            messagebox.showerror("Error","La moneda 1 debe ser un entero mayor o igual a 0")
            return
        if verificar_entero(mon1, 0, "x") == False:
            messagebox.showerror("Error","La moneda 1 debe ser un entero mayor o igual a 0")
            return
    

    # mon2 
    if mon2 == "":
        pass
    else:
        try:
            mon2 = int(mon2)
        except ValueError:
            messagebox.showerror("Error","La moneda 2 debe ser un entero mayor o igual a 0")
            return
        if verificar_entero(mon2, 0, "x") == False:
            messagebox.showerror("Error","La moneda 2 debe ser un entero mayor o igual a 0")
            return

    # mon3
    if mon3 == "":
        pass
    else:
        try:
            mon3 = int(mon3)
        except ValueError:
            messagebox.showerror("Error","La moneda 3 debe ser un entero mayor o igual a 0")
            return
        if verificar_entero(mon3, 0, "x") == False:
            messagebox.showerror("Error","La moneda 3 debe ser un entero mayor o igual a 0")
            return
    
    # bill1
    if bill1 == "":
        pass
    else:
        try:
            bill1 = int(bill1)
        except ValueError:
            messagebox.showerror("Error","El billete 1 debe ser un entero mayor o igual a 0")
            return
        if verificar_entero(bill1, 0, "x") == False:
            messagebox.showerror("Error","El billete 1 debe ser un entero mayor o igual a 0")
            return
        
    # bill2
    if bill2 == "":
        pass
    else:
        try:
            bill2 = int(bill2)
        except ValueError:
            messagebox.showerror("Error","El billete 2 debe ser un entero mayor o igual a 0")
            return
        if verificar_entero(bill2, 0, "x") == False:
            messagebox.showerror("Error","El billete 2 debe ser un entero mayor o igual a 0")
            return
        
    # bill3
    if bill3 == "":
        pass
    else:
        try:
            bill3 = int(bill3)
        except ValueError:
            messagebox.showerror("Error","El billete 3 debe ser un entero mayor o igual a 0")
            return
        if verificar_entero(bill3, 0, "x") == False:
            messagebox.showerror("Error","El billete 3 debe ser un entero mayor o igual a 0")
            return
    # bill4
    if bill4 == "":
        pass
    else:
        try:
            bill4 = int(bill4)
        except ValueError:
            messagebox.showerror("Error","El billete 4 debe ser un entero mayor o igual a 0")
            return
        if verificar_entero(bill4, 0, "x") == False:
            messagebox.showerror("Error","El billete 4 debe ser un entero mayor o igual a 0")
            return
    
    # bill5
    if bill5 == "":
        pass
    else:
        try:
            bill5 = int(bill5)
        except ValueError:
            messagebox.showerror("Error","El billete 5 debe ser un entero mayor o igual a 0")
            return
        if verificar_entero(bill5, 0, "x") == False:
            messagebox.showerror("Error","El billete 5 debe ser un entero mayor o igual a 0")
            return
    #agregar resultados
    #verificamos que si algun campo fue llenado, todos los demas deben de haberse llenado, si ninguno fue llenado, no se hace nada
    if no_espacios != "" or precio_hora != "" or pago_min != "" or redondeo != "" or min_max != "" or mon1 != "" or mon2 != "" or mon3 != "" or bill1 != "" or bill2 != "" or bill3 != "" or bill4 != "" or bill5 != "":
        if no_espacios == "":
            pass
        else:
            num_espacios = no_espacios
        if precio_hora == "":
            pass
        else:
            precio_x_hora = precio_hora
        if pago_min == "":
            pass
        else:
            pago_minimo = pago_min
        if redondeo == "":
            pass
        else:
            redondeo_tiempo = redondeo
        if min_max == "":
            pass
        else:
            minutos_max = min_max


        #revisamos monedas:
        lista_mon_escritas =[mon1, mon2, mon3]
        lista_monedas_anteriores = [moneda1, moneda2, moneda3]
        lista_revisar = []
        i = 0
        #hacemos una lista de como quedarían las monedas
        for cada_mon in lista_mon_escritas:
            if cada_mon == "":
                lista_revisar.append(lista_monedas_anteriores[i])
            else:
                lista_revisar.append(lista_mon_escritas[i])
            i += 1

        #revisamos que esa lista cumpla las restricciones
        #1. si el elemento es 0, todos los demás deben de ser 0
        if lista_revisar[0] == 0:
            try:
                if lista_revisar[1] != 0 and lista_revisar[1] != "":
                    messagebox.showerror("ERROR", "Si alguna moneda es 0, todas las demás apartir de ella deben de serlo")
                    return
            except:
                pass
            try:
                if lista_revisar[2] != 0 and lista_revisar[2] != "":
                    messagebox.showerror("ERROR", "Si alguna moneda es 0, todas las demás apartir de ella deben de serlo")
                    return
            except:
                pass

        if lista_revisar[1] == 0:
            try:
                if lista_revisar[2] != 0 and lista_revisar[2] != "":
                    messagebox.showerror("ERROR", "Si alguna moneda es 0, todas las demás apartir de ella deben de serlo")
                    return
            except:
                pass
            
        #2. si el elemento es un num diferente a 0, todos los demás deben de ser mayores a este o 0
        if lista_revisar[0] != 0:
            try:
                if lista_revisar[1] <= lista_revisar[0] and lista_revisar[1] != 0 and lista_revisar[1] != "":
                    messagebox.showerror("ERROR", "La moneda 2 debe de ser mayor a la moneda 1 o 0")
                    return
            except:
                pass
            try:
                if lista_revisar[2] <= lista_revisar[0] and lista_revisar[2] != 0 and lista_revisar[2] != "":
                    messagebox.showerror("ERROR", "La moneda 3 debe de ser mayor a la moneda 1 o 0")
                    return
            except:
                pass
        if lista_revisar[1] != 0:
            try:
                if lista_revisar[2] <= lista_revisar[1] and lista_revisar[2] != 0 and lista_revisar[2] != "":
                    messagebox.showerror("ERROR", "La moneda 3 debe de ser mayor a la moneda 2 o 0")
                    return
            except:
                pass
        
        #revisamos billetes
        lista_bill_escritas = [bill1, bill2, bill3, bill4, bill5]
        lista_billetes_anteriores = [billete1, billete2, billete3, billete4, billete5]
        lista_revisar_billetes = []
        i = 0
        #hacemos una lista de como quedarían los billetes
        for cada_bill in lista_bill_escritas:
            if cada_bill == "":
                lista_revisar_billetes.append(lista_billetes_anteriores[i])
            else:
                lista_revisar_billetes.append(lista_bill_escritas[i])
            i += 1

        #revisamos que esa lista cumpla las restricciones
        #1. si el elemento es 0, todos los demás deben de ser 0
        if lista_revisar_billetes[0] == 0:
            if lista_revisar_billetes[1] != 0 and lista_revisar_billetes[1] != "":
                messagebox.showerror("ERROR", "Si algun billete es 0, todas los demás apartir de él deben de serlo")
                return
            if lista_revisar_billetes[2] != 0 and lista_revisar_billetes[2] != "":
                messagebox.showerror("ERROR", "Si algun billete es 0, todas los demás apartir de él deben de serlo")
                return
            if lista_revisar_billetes[3] != 0 and lista_revisar_billetes[3] != "":
                messagebox.showerror("ERROR", "Si algun billete es 0, todas los demás apartir de él deben de serlo")
                return
            if lista_revisar_billetes[4] != 0 and lista_revisar_billetes[4] != "":
                messagebox.showerror("ERROR", "Si algun billete es 0, todas los demás apartir de él deben de serlo")
                return
            
        if lista_revisar_billetes[1] == 0:
            if lista_revisar_billetes[2] != 0 and lista_revisar_billetes[2] != "":
                messagebox.showerror("ERROR", "Si algun billete es 0, todas los demás apartir de él deben de serlo")
                return
            if lista_revisar_billetes[3] != 0 and lista_revisar_billetes[3] != "":
                messagebox.showerror("ERROR", "Si algun billete es 0, todas los demás apartir de él deben de serlo")
                return
            if lista_revisar_billetes[4] != 0 and lista_revisar_billetes[4] != "":
                messagebox.showerror("ERROR", "Si algun billete es 0, todas los demás apartir de él deben de serlo")
                return
            
        if lista_revisar_billetes[2] == 0:
            if lista_revisar_billetes[3] != 0 and lista_revisar_billetes[3] != "":
                messagebox.showerror("ERROR", "Si algun billete es 0, todas los demás apartir de él deben de serlo")
                return
            if lista_revisar_billetes[4] != 0 and lista_revisar_billetes[4] != "":
                messagebox.showerror("ERROR", "Si algun billete es 0, todas los demás apartir de él deben de serlo")
                return
        if lista_revisar_billetes[3] == 0:
            if lista_revisar_billetes[4] != 0 and lista_revisar_billetes[4] != "":
                messagebox.showerror("ERROR", "Si algun billete es 0, todas los demás apartir de él deben de serlo")
                return
        
        #2. si el elemento es un num diferente a 0, todos los demás deben de ser mayores a este o 0
        if lista_revisar_billetes[0] != 0:
            try:
                if lista_revisar_billetes[1] <= lista_revisar_billetes[0] and lista_revisar_billetes[1] != 0 and lista_revisar_billetes[1] != "":
                    messagebox.showerror("ERROR", "El billete 2 debe de ser mayor al billete 1 o 0")
                    return
            except:
                pass
            try:
                if lista_revisar_billetes[2] <= lista_revisar_billetes[0] and lista_revisar_billetes[2] != 0 and lista_revisar_billetes[2] != "":
                    messagebox.showerror("ERROR", "El billete 3 debe de ser mayor al billete 1 o 0")
                    return
            except:
                pass
            try:
                if lista_revisar_billetes[3] <= lista_revisar_billetes[0] and lista_revisar_billetes[3] != 0 and lista_revisar_billetes[3] != "":
                    messagebox.showerror("ERROR", "El billete 4 debe de ser mayor al billete 1 o 0")
                    return
            except:
                pass
            try:
                if lista_revisar_billetes[4] <= lista_revisar_billetes[0] and lista_revisar_billetes[4] != 0 and lista_revisar_billetes[4] != "":
                    messagebox.showerror("ERROR", "El billete 5 debe de ser mayor al billete 1 o 0")
                    return
            except:
                pass

        if lista_revisar_billetes[1] != 0:
            try:
                if lista_revisar_billetes[2] <= lista_revisar_billetes[1] and lista_revisar_billetes[2] != 0 and lista_revisar_billetes[2] != "":
                    messagebox.showerror("ERROR", "El billete 3 debe de ser mayor al billete 2 o 0")
                    return
            except:
                pass
            try:
                if lista_revisar_billetes[3] <= lista_revisar_billetes[1] and lista_revisar_billetes[3] != 0 and lista_revisar_billetes[3] != "":
                    messagebox.showerror("ERROR", "El billete 4 debe de ser mayor al billete 2 o 0")
                    return
            except:
                pass
            try:
                if lista_revisar_billetes[4] <= lista_revisar_billetes[1] and lista_revisar_billetes[4] != 0 and lista_revisar_billetes[4] != "":
                    messagebox.showerror("ERROR", "El billete 5 debe de ser mayor al billete 2 o 0")
                    return
            except:
                pass
        if lista_revisar_billetes[2] != 0:
            try:
                if lista_revisar_billetes[3] <= lista_revisar_billetes[2] and lista_revisar_billetes[3] != 0 and lista_revisar_billetes[3] != "":
                    messagebox.showerror("ERROR", "El billete 4 debe de ser mayor al billete 3 o 0")
                    return
            except:
                pass
            try:
                if lista_revisar_billetes[4] <= lista_revisar_billetes[2] and lista_revisar_billetes[4] != 0 and lista_revisar_billetes[4] != "":
                    messagebox.showerror("ERROR", "El billete 5 debe de ser mayor al billete 3 o 0")
                    return
            except:
                pass
        if lista_revisar_billetes[3] != 0:
            try:
                if lista_revisar_billetes[4] <= lista_revisar_billetes[3] and lista_revisar_billetes[4] != 0 and lista_revisar_billetes[4] != "":
                    messagebox.showerror("ERROR", "El billete 5 debe de ser mayor al billete 4 o 0")
                    return
            except:
                pass

        moneda1 = lista_revisar[0]
        moneda2 = lista_revisar[1]
        moneda3 = lista_revisar[2]
        billete1 = lista_revisar_billetes[0]
        billete2 = lista_revisar_billetes[1]
        billete3 = lista_revisar_billetes[2]
        billete4 = lista_revisar_billetes[3]
        billete5 = lista_revisar_billetes[4]
        #asignamos la cantidad de espacios en el parqueo
        if num_espacios != "":
            parqueo = []
            for i in range(num_espacios):
                parqueo += [[]]
        return True
    else:
        #ningun cambio fue aplicado
        return True
#------------------------------------------------
# OPCIÓN SALDO DEL CAJERO                                                          
#------------------------------------------------
def saldo_cajero():
    global moneda1, moneda2, moneda3, billete1, billete2, billete3, billete4, billete5, dic_moneda1, dic_moneda2, dic_moneda3, dic_total_monedas, dic_billete1, dic_billete2, dic_billete3, dic_billete4, dic_billete5, dic_total_billetes
    if verificar_datos_conf() == False:#validacion
        messagebox.showerror("Error","Primero debe de configurar todos los datos del estacionamiento en CONFIGURACION")
        return
    os.system("cls")
    vsaldo = Toplevel()#nueva ventana
    vsaldo.title("ESTACIONAMIENTO - SALDO DEL CAJERO")
    vsaldo.geometry("1200x600")#dimensiones de la ventana
    vsaldo.focus()#para que seleccione la ventana abierta
    vsaldo.grab_set()#evita usar la ventana principal a menos que se haya cerrado la ventana abierta
    frame = Frame(vsaldo)
    frame.place(relheight=1, relwidth=1)
    refrescar_diccionarios()

    titulo = Label(frame, text="ESTACIONAMIENTO - SALDO DEL CAJERO", borderwidth=10, relief="sunken").place(anchor="center", relx=0.5, rely=0.06)
    entradas_text = Label(frame, text="ENTRADAS").place(anchor="center", relx=0.25, rely=0.12)
    salidas_text = Label(frame, text="SALIDAS").place(anchor="center", relx=0.5, rely=0.12)
    saldo_text = Label(frame, text="SALDO").place(anchor="center", relx=0.8, rely=0.12)
    denominacion_text = Label(frame, text="DENOMINACIÓN").place(anchor="center", relx=0.05, rely=0.17)
    cantidad_entradas_text = Label(frame, text="CANTIDAD").place(anchor="center", relx=0.2, rely=0.17)
    total_entradas_text = Label(frame, text="TOTAL").place(anchor="center", relx=0.28, rely=0.17)
    cantidad_salidas_text = Label(frame, text="CANTIDAD").place(anchor="center", relx=0.45, rely=0.17)
    total_salidas_text = Label(frame, text="TOTAL").place(anchor="center", relx=0.55, rely=0.17)
    cantidad_saldo_text = Label(frame, text="CANTIDAD").place(anchor="center", relx=0.75, rely=0.17)
    total_saldo_text = Label(frame, text="TOTAL").place(anchor="center", relx=0.85, rely=0.17)
    moneda1_text = Label(frame, text="Monedas de " + str(moneda1)).place(anchor="center", relx=0.05, rely=0.22) 
    moneda2_text = Label(frame, text="Monedas de " + str(moneda2)).place(anchor="center", relx=0.05, rely=0.27)
    moneda3_text = Label(frame, text="Monedas de " + str(moneda3)).place(anchor="center", relx=0.05, rely=0.32)  
    monedas_total_text = Label(frame, text="TOTAL DE MONEDAS").place(anchor="center", relx=0.05, rely=0.37)  
    variable_check = IntVar()#determina si el check esta prendido o no
    check = Checkbutton(frame, text="Vaciar cajero", variable=variable_check).place(anchor="center", relx=0.05, rely=0.77)
    ok = Button(frame, text="Ok", borderwidth=5, command= lambda: (vaciar_cajero(), vsaldo.destroy()) if variable_check.get() == 1 else vsaldo.destroy()).place(anchor="center", relx=0.4, rely =0.93)
    cancelar = Button(frame, text="Cancelar", borderwidth=5, command=vsaldo.destroy).place(anchor="center", relx=0.55, rely =0.93)

    #los datos de los diccionarios se desplegaran
    e_c_moneda1_text = Label(frame, text=str(dic_moneda1["entrada"][0])).place(anchor="center", relx=0.2, rely=0.22) 
    e_t_moneda1_text = Label(frame, text=str(dic_moneda1["entrada"][1])).place(anchor="center", relx=0.28, rely=0.22) 
    salida_c_moneda1_text = Label(frame, text=str(dic_moneda1["salida"][0])).place(anchor="center", relx=0.45, rely=0.22) 
    salida_t_moneda1_text = Label(frame, text=str(dic_moneda1["salida"][1])).place(anchor="center", relx=0.55, rely=0.22) 
    saldo_c_moneda1_text = Label(frame, text=str(dic_moneda1["saldo"][0])).place(anchor="center", relx=0.75, rely=0.22) 
    saldo_t_moneda1_text = Label(frame, text=str(dic_moneda1["saldo"][1])).place(anchor="center", relx=0.85, rely=0.22) 

    e_c_moneda2_text = Label(frame, text=str(dic_moneda2["entrada"][0])).place(anchor="center", relx=0.2, rely=0.27) 
    e_t_moneda2_text = Label(frame, text=str(dic_moneda2["entrada"][1])).place(anchor="center", relx=0.28, rely=0.27) 
    salida_c_moneda2_text = Label(frame, text=str(dic_moneda2["salida"][0])).place(anchor="center", relx=0.45, rely=0.27) 
    salida_t_moneda2_text = Label(frame, text=str(dic_moneda2["salida"][1])).place(anchor="center", relx=0.55, rely=0.27) 
    saldo_c_moneda2_text = Label(frame, text=str(dic_moneda2["saldo"][0])).place(anchor="center", relx=0.75, rely=0.27) 
    saldo_t_moneda2_text = Label(frame, text=str(dic_moneda2["saldo"][1])).place(anchor="center", relx=0.85, rely=0.27) 

    e_c_moneda3_text = Label(frame, text=str(dic_moneda3["entrada"][0])).place(anchor="center", relx=0.2, rely=0.32) 
    e_t_moneda3_text = Label(frame, text=str(dic_moneda3["entrada"][1])).place(anchor="center", relx=0.28, rely=0.32) 
    salida_c_moneda3_text = Label(frame, text=str(dic_moneda3["salida"][0])).place(anchor="center", relx=0.45, rely=0.32) 
    salida_t_moneda3_text = Label(frame, text=str(dic_moneda3["salida"][1])).place(anchor="center", relx=0.55, rely=0.32) 
    saldo_c_moneda3_text = Label(frame, text=str(dic_moneda3["saldo"][0])).place(anchor="center", relx=0.75, rely=0.32) 
    saldo_t_moneda3_text = Label(frame, text=str(dic_moneda3["saldo"][1])).place(anchor="center", relx=0.85, rely=0.32) 

    e_c_total_moneda_text = Label(frame, text=str(dic_total_monedas["entrada"][0])).place(anchor="center", relx=0.2, rely=0.37) 
    e_t_total_moneda_text = Label(frame, text=str(dic_total_monedas["entrada"][1])).place(anchor="center", relx=0.28, rely=0.37) 
    salida_c_total_moneda_text = Label(frame, text=str(dic_total_monedas["salida"][0])).place(anchor="center", relx=0.45, rely=0.37) 
    salida_t_total_moneda_text = Label(frame, text=str(dic_total_monedas["salida"][1])).place(anchor="center", relx=0.55, rely=0.37) 
    saldo_c_total_moneda_text = Label(frame, text=str(dic_total_monedas["saldo"][0])).place(anchor="center", relx=0.75, rely=0.37) 
    saldo_t_total_moneda_text = Label(frame, text=str(dic_total_monedas["saldo"][1])).place(anchor="center", relx=0.85, rely=0.37) 

    linea = Label(frame, text="-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------").place(anchor="center", relx=0.05, rely=0.42)
    billete1_text = Label(frame, text="Billetes de " + str(billete1)).place(anchor="center", relx=0.05, rely=0.47) 
    billete2_text = Label(frame, text="Billetes de " + str(billete2)).place(anchor="center", relx=0.05, rely=0.52)
    billete3_text = Label(frame, text="Billetes de " + str(billete3)).place(anchor="center", relx=0.05, rely=0.57)
    billete4_text = Label(frame, text="Billetes de " + str(billete4)).place(anchor="center", relx=0.05, rely=0.62)
    billete5_text = Label(frame, text="Billetes de " + str(billete5)).place(anchor="center", relx=0.05, rely=0.67)
    total_billetes_text = Label(frame, text="TOTAL DE BILLETES").place(anchor="center", relx=0.05, rely=0.72)

    e_c_billete1_text = Label(frame, text=str(dic_billete1["entrada"][0])).place(anchor="center", relx=0.2, rely=0.47) 
    e_t_billete1_text = Label(frame, text=str(dic_billete1["entrada"][1])).place(anchor="center", relx=0.28, rely=0.47) 
    salida_c_billete1_text = Label(frame, text=str(dic_billete1["salida"][0])).place(anchor="center", relx=0.45, rely=0.47) 
    salida_t_billete1_text = Label(frame, text=str(dic_billete1["salida"][1])).place(anchor="center", relx=0.55, rely=0.47) 
    saldo_c_billete1_text = Label(frame, text=str(dic_billete1["saldo"][0])).place(anchor="center", relx=0.75, rely=0.47) 
    saldo_t_billete1_text = Label(frame, text=str(dic_billete1["saldo"][1])).place(anchor="center", relx=0.85, rely=0.47) 

    e_c_billete2_text = Label(frame, text=str(dic_billete2["entrada"][0])).place(anchor="center", relx=0.2, rely=0.52) 
    e_t_billete2_text = Label(frame, text=str(dic_billete2["entrada"][1])).place(anchor="center", relx=0.28, rely=0.52) 
    salida_c_billete2_text = Label(frame, text=str(dic_billete2["salida"][0])).place(anchor="center", relx=0.45, rely=0.52) 
    salida_t_billete2_text = Label(frame, text=str(dic_billete2["salida"][1])).place(anchor="center", relx=0.55, rely=0.52) 
    saldo_c_billete2_text = Label(frame, text=str(dic_billete2["saldo"][0])).place(anchor="center", relx=0.75, rely=0.52) 
    saldo_t_billete2_text = Label(frame, text=str(dic_billete2["saldo"][1])).place(anchor="center", relx=0.85, rely=0.52) 

    e_c_billete3_text = Label(frame, text=str(dic_billete3["entrada"][0])).place(anchor="center", relx=0.2, rely=0.57) 
    e_t_billete3_text = Label(frame, text=str(dic_billete3["entrada"][1])).place(anchor="center", relx=0.28, rely=0.57) 
    salida_c_billete3_text = Label(frame, text=str(dic_billete3["salida"][0])).place(anchor="center", relx=0.45, rely=0.57) 
    salida_t_billete3_text = Label(frame, text=str(dic_billete3["salida"][1])).place(anchor="center", relx=0.55, rely=0.57) 
    saldo_c_billete3_text = Label(frame, text=str(dic_billete3["saldo"][0])).place(anchor="center", relx=0.75, rely=0.57) 
    saldo_t_billete3_text = Label(frame, text=str(dic_billete3["saldo"][1])).place(anchor="center", relx=0.85, rely=0.57) 

    e_c_billete4_text = Label(frame, text=str(dic_billete4["entrada"][0])).place(anchor="center", relx=0.2, rely=0.62) 
    e_t_billete4_text = Label(frame, text=str(dic_billete4["entrada"][1])).place(anchor="center", relx=0.28, rely=0.62) 
    salida_c_billete4_text = Label(frame, text=str(dic_billete4["salida"][0])).place(anchor="center", relx=0.45, rely=0.62) 
    salida_t_billete4_text = Label(frame, text=str(dic_billete4["salida"][1])).place(anchor="center", relx=0.55, rely=0.62) 
    saldo_c_billete4_text = Label(frame, text=str(dic_billete4["saldo"][0])).place(anchor="center", relx=0.75, rely=0.62) 
    saldo_t_billete4_text = Label(frame, text=str(dic_billete4["saldo"][1])).place(anchor="center", relx=0.85, rely=0.62) 

    e_c_billete5_text = Label(frame, text=str(dic_billete5["entrada"][0])).place(anchor="center", relx=0.2, rely=0.67) 
    e_t_billete5_text = Label(frame, text=str(dic_billete5["entrada"][1])).place(anchor="center", relx=0.28, rely=0.67) 
    salida_c_billete5_text = Label(frame, text=str(dic_billete5["salida"][0])).place(anchor="center", relx=0.45, rely=0.67) 
    salida_t_billete5_text = Label(frame, text=str(dic_billete5["salida"][1])).place(anchor="center", relx=0.55, rely=0.67) 
    saldo_c_billete5_text = Label(frame, text=str(dic_billete5["saldo"][0])).place(anchor="center", relx=0.75, rely=0.67) 
    saldo_t_billete5_text = Label(frame, text=str(dic_billete5["saldo"][1])).place(anchor="center", relx=0.85, rely=0.67) 

    e_c_total_billete_text = Label(frame, text=str(dic_total_billetes["entrada"][0])).place(anchor="center", relx=0.2, rely=0.72) 
    e_t_total_billete_text = Label(frame, text=str(dic_total_billetes["entrada"][1])).place(anchor="center", relx=0.28, rely=0.72) 
    salida_c_total_billete_text = Label(frame, text=str(dic_total_billetes["salida"][0])).place(anchor="center", relx=0.45, rely=0.72) 
    salida_t_total_billete_text = Label(frame, text=str(dic_total_billetes["salida"][1])).place(anchor="center", relx=0.55, rely=0.72) 
    saldo_c_total_billete_text = Label(frame, text=str(dic_total_billetes["saldo"][0])).place(anchor="center", relx=0.75, rely=0.72) 
    saldo_t_total_billete_text = Label(frame, text=str(dic_total_billetes["saldo"][1])).place(anchor="center", relx=0.85, rely=0.72) 
#------------------------------------------------
# OPCIÓN CARGAR CAJERO                                                      
#------------------------------------------------
def cargar_cajero():
    global moneda1, moneda2, moneda3, billete1, billete2, billete3, billete4, billete5, dic_moneda1, dic_moneda2, dic_moneda3, dic_total_monedas, dic_billete1, dic_billete2, dic_billete3, dic_billete4, dic_billete5, dic_total_billetes
    if verificar_datos_conf() == False:#validacion
        messagebox.showerror("Error","Primero debe de configurar todos los datos del estacionamiento en CONFIGURACION")
        return
    os.system("cls")
    vcargar = Toplevel()#nueva ventana
    vcargar.title("ESTACIONAMIENTO - CARGAR CAJERO")
    vcargar.geometry("1200x600")#dimensiones de la ventana
    vcargar.focus()#para que seleccione la ventana abierta
    vcargar.grab_set()#evita usar la ventana principal a menos que se haya cerrado la ventana abierta
    frame = Frame(vcargar)
    frame.place(relheight=1, relwidth=1)

    titulo = Label(frame, text="ESTACIONAMIENTO - CARGAR CAJERO", borderwidth=10, relief="sunken").place(anchor="center", relx=0.5, rely=0.06)
    entradas_text = Label(frame, text="SALDO ANTES DE LA CARGA").place(anchor="center", relx=0.25, rely=0.12)
    salidas_text = Label(frame, text="CARGA").place(anchor="center", relx=0.5, rely=0.12)
    saldo_text = Label(frame, text="SALDO").place(anchor="center", relx=0.8, rely=0.12)
    denominacion_text = Label(frame, text="DENOMINACIÓN").place(anchor="center", relx=0.05, rely=0.17)
    cantidad_saldo_antes_text = Label(frame, text="CANTIDAD").place(anchor="center", relx=0.2, rely=0.17)
    total_saldo_antes_text = Label(frame, text="TOTAL").place(anchor="center", relx=0.28, rely=0.17)
    cantidad_carga_text = Label(frame, text="CANTIDAD").place(anchor="center", relx=0.45, rely=0.17)
    total_carga_text = Label(frame, text="TOTAL").place(anchor="center", relx=0.55, rely=0.17)
    cantidad_saldo_text = Label(frame, text="CANTIDAD").place(anchor="center", relx=0.75, rely=0.17)
    total_saldo_text = Label(frame, text="TOTAL").place(anchor="center", relx=0.85, rely=0.17)
    moneda1_text = Label(frame, text="Monedas de " + str(moneda1)).place(anchor="center", relx=0.05, rely=0.22) 
    moneda2_text = Label(frame, text="Monedas de " + str(moneda2)).place(anchor="center", relx=0.05, rely=0.27)
    moneda3_text = Label(frame, text="Monedas de " + str(moneda3)).place(anchor="center", relx=0.05, rely=0.32)  
    monedas_total_text = Label(frame, text="TOTAL DE MONEDAS").place(anchor="center", relx=0.05, rely=0.37)  

    saldo_antes_c_moneda1_text = Label(frame, text=str(dic_moneda1["saldo"][0]))
    saldo_antes_c_moneda1_text.place(anchor="center", relx=0.2, rely=0.22) 
    saldo_antes_t_moneda1_text = Label(frame, text=str(dic_moneda1["saldo"][1]))
    saldo_antes_t_moneda1_text.place(anchor="center", relx=0.28, rely=0.22) 
    saldo_antes_c_moneda2_text = Label(frame, text=str(dic_moneda2["saldo"][0]))
    saldo_antes_c_moneda2_text.place(anchor="center", relx=0.2, rely=0.27) 
    saldo_antes_t_moneda2_text = Label(frame, text=str(dic_moneda2["saldo"][1]))
    saldo_antes_t_moneda2_text.place(anchor="center", relx=0.28, rely=0.27) 
    saldo_antes_c_moneda3_text = Label(frame, text=str(dic_moneda3["saldo"][0])) 
    saldo_antes_c_moneda3_text.place(anchor="center", relx=0.2, rely=0.32)
    saldo_antes_t_moneda3_text = Label(frame, text=str(dic_moneda3["saldo"][1]))
    saldo_antes_t_moneda3_text.place(anchor="center", relx=0.28, rely=0.32) 
    saldo_c_total_moneda_text = Label(frame, text=str(dic_total_monedas["saldo"][0]))
    saldo_c_total_moneda_text.place(anchor="center", relx=0.2, rely=0.37) 
    saldo_t_total_moneda_text = Label(frame, text=str(dic_total_monedas["saldo"][1])) 
    saldo_t_total_moneda_text.place(anchor="center", relx=0.28, rely=0.37)
    

    linea = Label(frame, text="-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------").place(anchor="center", relx=0.05, rely=0.42)
    billete1_text = Label(frame, text="Billetes de " + str(billete1)).place(anchor="center", relx=0.05, rely=0.47) 
    billete2_text = Label(frame, text="Billetes de " + str(billete2)).place(anchor="center", relx=0.05, rely=0.52)
    billete3_text = Label(frame, text="Billetes de " + str(billete3)).place(anchor="center", relx=0.05, rely=0.57)
    billete4_text = Label(frame, text="Billetes de " + str(billete4)).place(anchor="center", relx=0.05, rely=0.62)
    billete5_text = Label(frame, text="Billetes de " + str(billete5)).place(anchor="center", relx=0.05, rely=0.67)
    total_billetes_text = Label(frame, text="TOTAL DE BILLETES").place(anchor="center", relx=0.05, rely=0.72)

    saldo_antes_c_billete1_text = Label(frame, text=str(dic_billete1["saldo"][0]))
    saldo_antes_c_billete1_text.place(anchor="center", relx=0.2, rely=0.47)
    saldo_antes_t_billete1_text = Label(frame, text=str(dic_billete1["saldo"][1]))
    saldo_antes_t_billete1_text.place(anchor="center", relx=0.28, rely=0.47) 
    saldo_antes_c_billete2_text = Label(frame, text=str(dic_billete2["saldo"][0]))
    saldo_antes_c_billete2_text.place(anchor="center", relx=0.2, rely=0.52) 
    saldo_antes_t_billete2_text = Label(frame, text=str(dic_billete2["saldo"][1]))
    saldo_antes_t_billete2_text.place(anchor="center", relx=0.28, rely=0.52)
    saldo_antes_c_billete3_text = Label(frame, text=str(dic_billete3["saldo"][0]))
    saldo_antes_c_billete3_text.place(anchor="center", relx=0.2, rely=0.57) 
    saldo_antes_t_billete3_text = Label(frame, text=str(dic_billete3["saldo"][1]))
    saldo_antes_t_billete3_text.place(anchor="center", relx=0.28, rely=0.57) 
    saldo_antes_c_billete4_text = Label(frame, text=str(dic_billete4["saldo"][0]))
    saldo_antes_c_billete4_text.place(anchor="center", relx=0.2, rely=0.62) 
    saldo_antes_t_billete4_text = Label(frame, text=str(dic_billete4["saldo"][1]))
    saldo_antes_t_billete4_text.place(anchor="center", relx=0.28, rely=0.62)
    saldo_antes_c_billete5_text = Label(frame, text=str(dic_billete5["saldo"][0]))
    saldo_antes_c_billete5_text.place(anchor="center", relx=0.2, rely=0.67) 
    saldo_antes_t_billete5_text = Label(frame, text=str(dic_billete5["saldo"][1]))
    saldo_antes_t_billete5_text.place(anchor="center", relx=0.28, rely=0.67)
    saldo_antes_c_total_billete_text = Label(frame, text=str(dic_total_billetes["saldo"][0]))
    saldo_antes_c_total_billete_text.place(anchor="center", relx=0.2, rely=0.72) 
    saldo_antes_t_total_billete_text = Label(frame, text=str(dic_total_billetes["saldo"][1]))
    saldo_antes_t_total_billete_text.place(anchor="center", relx=0.28, rely=0.72) 

    #configuracion de datos en tiempo real:
    #cuadros de texto
    carga_can_mon1 = Entry(frame)
    carga_can_mon1.place(anchor="center", relx=0.45, rely=0.22)
    carga_can_mon2 = Entry(frame)
    carga_can_mon2.place(anchor="center", relx=0.45, rely=0.27)
    carga_can_mon3 = Entry(frame)
    carga_can_mon3.place(anchor="center", relx=0.45, rely=0.32)
    carga_can_bill1 = Entry(frame)
    carga_can_bill1.place(anchor="center", relx=0.45, rely=0.47)
    carga_can_bill2 = Entry(frame)
    carga_can_bill2.place(anchor="center", relx=0.45, rely=0.52)
    carga_can_bill3 = Entry(frame)
    carga_can_bill3.place(anchor="center", relx=0.45, rely=0.57)
    carga_can_bill4 = Entry(frame)
    carga_can_bill4.place(anchor="center", relx=0.45, rely=0.62)
    carga_can_bill5 = Entry(frame)
    carga_can_bill5.place(anchor="center", relx=0.45, rely=0.67)

    #cambios en tiempo real:
    #monedas
    carga_cantidad_monedas = Label(frame, text="Resultado")
    carga_cantidad_monedas.place(anchor="center", relx=0.45, rely=0.37)
    carga_total_monedas = Label(frame, text="Resultado")
    carga_total_monedas.place(anchor="center", relx=0.55, rely=0.37)

    carga_total_mon1 = Label(frame, text="Resultado")
    carga_total_mon1.place(anchor="center", relx=0.55, rely=0.22)

#-------------------------------------

    #billetes
    carga_cantidad_billetes = Label(frame, text="Resultado")
    carga_cantidad_billetes.place(anchor="center", relx=0.45, rely=0.72)
    carga_total_billetes = Label(frame, text="Resultado")
    carga_total_billetes.place(anchor="center", relx=0.55, rely=0.72)

    carga_total_bill1 = Label(frame, text="Resultado")
    carga_total_bill1.place(anchor="center", relx=0.55, rely=0.47)

    carga_total_bill2 = Label(frame, text="Resultado")
    carga_total_bill2.place(anchor="center", relx=0.55, rely=0.52)

    carga_total_bill3 = Label(frame, text="Resultado")
    carga_total_bill3.place(anchor="center", relx=0.55, rely=0.57)

    carga_total_bill4 = Label(frame, text="Resultado")
    carga_total_bill4.place(anchor="center", relx=0.55, rely=0.62)

    carga_total_bill5 = Label(frame, text="Resultado")
    carga_total_bill5.place(anchor="center", relx=0.55, rely=0.67)

    #saldo monedas
    can_saldo_mon1 = Label(frame, text="Resultado")
    can_saldo_mon1.place(anchor="center", relx=0.75, rely=0.22)

    can_saldo_mon2 = Label(frame, text="Resultado")
    can_saldo_mon2.place(anchor="center", relx=0.75, rely=0.27)

    can_saldo_mon3 = Label(frame, text="Resultado")
    can_saldo_mon3.place(anchor="center", relx=0.75, rely=0.32)

    can_saldo_total_monedas = Label(frame, text="Resultado")
    can_saldo_total_monedas.place(anchor="center", relx=0.75, rely=0.37)

    total_saldo_mon1 = Label(frame, text="Resultado")
    total_saldo_mon1.place(anchor="center", relx=0.85, rely=0.22)

    total_saldo_mon2 = Label(frame, text="Resultado")
    total_saldo_mon2.place(anchor="center", relx=0.85, rely=0.27)

    total_saldo_mon3 = Label(frame, text="Resultado")
    total_saldo_mon3.place(anchor="center", relx=0.85, rely=0.32)

    total_saldo_total_monedas = Label(frame, text="Resultado")
    total_saldo_total_monedas.place(anchor="center", relx=0.85, rely=0.37)

    #saldo billetes
    can_saldo_bill1 = Label(frame, text="Resultado")
    can_saldo_bill1.place(anchor="center", relx=0.75, rely=0.47)

    can_saldo_bill2 = Label(frame, text="Resultado")
    can_saldo_bill2.place(anchor="center", relx=0.75, rely=0.52)

    can_saldo_bill3 = Label(frame, text="Resultado")
    can_saldo_bill3.place(anchor="center", relx=0.75, rely=0.57)

    can_saldo_bill4 = Label(frame, text="Resultado")
    can_saldo_bill4.place(anchor="center", relx=0.75, rely=0.62)

    can_saldo_bill5 = Label(frame, text="Resultado")
    can_saldo_bill5.place(anchor="center", relx=0.75, rely=0.67)

    can_saldo_total_billetes = Label(frame, text="Resultado")
    can_saldo_total_billetes.place(anchor="center", relx=0.75, rely=0.72)

    total_saldo_bill1 = Label(frame, text="Resultado")
    total_saldo_bill1.place(anchor="center", relx=0.85, rely=0.47)

    total_saldo_bill2 = Label(frame, text="Resultado")
    total_saldo_bill2.place(anchor="center", relx=0.85, rely=0.52)

    total_saldo_bill3 = Label(frame, text="Resultado")
    total_saldo_bill3.place(anchor="center", relx=0.85, rely=0.57)

    total_saldo_bill4 = Label(frame, text="Resultado")
    total_saldo_bill4.place(anchor="center", relx=0.85, rely=0.62)

    total_saldo_bill5 = Label(frame, text="Resultado")
    total_saldo_bill5.place(anchor="center", relx=0.85, rely=0.67)

    total_saldo_total_billetes = Label(frame, text="Resultado")
    total_saldo_total_billetes.place(anchor="center", relx=0.85, rely=0.72)

    total_cajero_text = Label(frame, text="TOTAL DEL CAJERO").place(anchor="center", relx=0.05, rely=0.82)
    saldo_t_total_cajero_text = Label(frame, text="Resultado")
    saldo_t_total_cajero_text.place(anchor="center", relx=0.85, rely=0.82)


    #binds
    #cada vez que se modifique un cuadro, se modificaran todos los demas(es lo que ocurre en el lambda)
    carga_can_mon1.bind("<KeyRelease>", lambda e: (sumar_tiempo_real("n", carga_can_mon1.get(), carga_total_mon1, 0, moneda1), sumar_num("n", carga_can_mon1.get(), carga_can_mon2.get(), carga_can_mon3.get(), carga_cantidad_monedas),
                                                   sumar_num("n", carga_total_mon1.cget("text"), carga_total_mon2.cget("text"), carga_total_mon3.cget("text"), carga_total_monedas), 
                                                   sumar_num("n", carga_can_mon1.get(), saldo_antes_c_moneda1_text.cget("text"), 0, can_saldo_mon1), 
                                                   sumar_num("n", can_saldo_mon1.cget("text"), can_saldo_mon2.cget("text"), can_saldo_mon3.cget("text"), can_saldo_total_monedas),
                                                   sumar_num("n", saldo_t_total_moneda_text.cget("text"), carga_total_monedas.cget("text"), 0, total_saldo_total_monedas),
                                                   sumar_num("n", saldo_antes_t_moneda1_text.cget("text"), carga_total_mon1.cget("text"), 0, total_saldo_mon1),
                                                   sumar_num("n", total_saldo_total_billetes.cget("text"), total_saldo_total_monedas.cget("text"), 0, saldo_t_total_cajero_text)))
    
    carga_total_mon2 = Label(frame, text="Resultado")
    carga_total_mon2.place(anchor="center", relx=0.55, rely=0.27)
    carga_can_mon2.bind("<KeyRelease>", lambda e: (sumar_tiempo_real("n", carga_can_mon2.get(), carga_total_mon2, 0, moneda2), sumar_num("n", carga_can_mon1.get(), carga_can_mon2.get(), carga_can_mon3.get(), carga_cantidad_monedas),
                                                   sumar_num("n", carga_total_mon1.cget("text"), carga_total_mon2.cget("text"), carga_total_mon3.cget("text"), carga_total_monedas),
                                                   sumar_num("n", carga_can_mon2.get(), saldo_antes_c_moneda2_text.cget("text"), 0, can_saldo_mon2),
                                                   sumar_num("n", can_saldo_mon1.cget("text"), can_saldo_mon2.cget("text"), can_saldo_mon3.cget("text"), can_saldo_total_monedas),
                                                   sumar_num("n", saldo_t_total_moneda_text.cget("text"), carga_total_monedas.cget("text"), 0, total_saldo_total_monedas),
                                                   sumar_num("n", saldo_antes_t_moneda2_text.cget("text"), carga_total_mon2.cget("text"), 0, total_saldo_mon2),
                                                   sumar_num("n", total_saldo_total_billetes.cget("text"), total_saldo_total_monedas.cget("text"), 0, saldo_t_total_cajero_text)))

    carga_total_mon3 = Label(frame, text="Resultado")
    carga_total_mon3.place(anchor="center", relx=0.55, rely=0.32)
    carga_can_mon3.bind("<KeyRelease>", lambda e: (sumar_tiempo_real("n", carga_can_mon3.get(), carga_total_mon3, 0, moneda3), sumar_num("n", carga_can_mon1.get(), carga_can_mon2.get(), carga_can_mon3.get(), carga_cantidad_monedas),
                                                   sumar_num("n", carga_total_mon1.cget("text"), carga_total_mon2.cget("text"), carga_total_mon3.cget("text"), carga_total_monedas),
                                                   sumar_num("n", carga_can_mon3.get(), saldo_antes_c_moneda3_text.cget("text"), 0, can_saldo_mon3),
                                                   sumar_num("n", can_saldo_mon1.cget("text"), can_saldo_mon2.cget("text"), can_saldo_mon3.cget("text"), can_saldo_total_monedas),
                                                   sumar_num("n", saldo_t_total_moneda_text.cget("text"), carga_total_monedas.cget("text"), 0, total_saldo_total_monedas),
                                                   sumar_num("n", saldo_antes_t_moneda3_text.cget("text"), carga_total_mon3.cget("text"), 0, total_saldo_mon3),
                                                   sumar_num("n", total_saldo_total_billetes.cget("text"), total_saldo_total_monedas.cget("text"), 0, saldo_t_total_cajero_text)))
    

    carga_can_bill1.bind("<KeyRelease>", lambda e: (sumar_tiempo_real("n", carga_can_bill1.get(), carga_total_bill1, 0, billete1), sumar_num_bill("n", carga_can_bill1.get(), carga_can_bill2.get(), carga_can_bill3.get(), carga_can_bill4.get(), carga_can_bill5.get(), carga_cantidad_billetes),
                                                    sumar_num_bill("n", carga_total_bill1.cget("text"), carga_total_bill2.cget("text"), carga_total_bill3.cget("text"), carga_total_bill4.cget("text"), carga_total_bill5.cget("text"), carga_total_billetes),
                                                    sumar_num("n", carga_can_bill1.get(), saldo_antes_c_billete1_text.cget("text"), 0, can_saldo_bill1),
                                                    sumar_num_bill("n", can_saldo_bill1.cget("text"), can_saldo_bill2.cget("text"), can_saldo_bill3.cget("text"), can_saldo_bill4.cget("text"), can_saldo_bill5.cget("text"), can_saldo_total_billetes),
                                                    sumar_num("n", saldo_antes_t_billete1_text.cget("text"), carga_total_bill1.cget("text"), 0, total_saldo_bill1),
                                                    sumar_num_bill("n", total_saldo_bill1.cget("text"), total_saldo_bill2.cget("text"), total_saldo_bill3.cget("text"), total_saldo_bill4.cget("text"), total_saldo_bill5.cget("text"), total_saldo_total_billetes),
                                                    sumar_num("n", total_saldo_total_billetes.cget("text"), total_saldo_total_monedas.cget("text"), 0, saldo_t_total_cajero_text)))
    

    carga_can_bill2.bind("<KeyRelease>", lambda e: (sumar_tiempo_real("n", carga_can_bill2.get(), carga_total_bill2, 0, billete2), sumar_num_bill("n", carga_can_bill1.get(), carga_can_bill2.get(), carga_can_bill3.get(), carga_can_bill4.get(), carga_can_bill5.get(), carga_cantidad_billetes),
                                                    sumar_num_bill("n", carga_total_bill1.cget("text"), carga_total_bill2.cget("text"), carga_total_bill3.cget("text"), carga_total_bill4.cget("text"), carga_total_bill5.cget("text"), carga_total_billetes),
                                                    sumar_num("n", carga_can_bill2.get(), saldo_antes_c_billete2_text.cget("text"), 0, can_saldo_bill2),
                                                    sumar_num_bill("n", can_saldo_bill1.cget("text"), can_saldo_bill2.cget("text"), can_saldo_bill3.cget("text"), can_saldo_bill4.cget("text"), can_saldo_bill5.cget("text"), can_saldo_total_billetes),
                                                    sumar_num("n", saldo_antes_t_billete2_text.cget("text"), carga_total_bill2.cget("text"), 0, total_saldo_bill2),
                                                    sumar_num_bill("n", total_saldo_bill1.cget("text"), total_saldo_bill2.cget("text"), total_saldo_bill3.cget("text"), total_saldo_bill4.cget("text"), total_saldo_bill5.cget("text"), total_saldo_total_billetes),
                                                    sumar_num("n", total_saldo_total_billetes.cget("text"), total_saldo_total_monedas.cget("text"), 0, saldo_t_total_cajero_text)))
    
    carga_can_bill3.bind("<KeyRelease>", lambda e: (sumar_tiempo_real("n", carga_can_bill3.get(), carga_total_bill3, 0, billete3), sumar_num_bill("n", carga_can_bill1.get(), carga_can_bill2.get(), carga_can_bill3.get(), carga_can_bill4.get(), carga_can_bill5.get(), carga_cantidad_billetes),
                                                    sumar_num_bill("n", carga_total_bill1.cget("text"), carga_total_bill2.cget("text"), carga_total_bill3.cget("text"), carga_total_bill4.cget("text"), carga_total_bill5.cget("text"), carga_total_billetes),
                                                    sumar_num("n", carga_can_bill3.get(), saldo_antes_c_billete3_text.cget("text"), 0, can_saldo_bill3),
                                                    sumar_num_bill("n", can_saldo_bill1.cget("text"), can_saldo_bill2.cget("text"), can_saldo_bill3.cget("text"), can_saldo_bill4.cget("text"), can_saldo_bill5.cget("text"), can_saldo_total_billetes),
                                                    sumar_num("n", saldo_antes_t_billete3_text.cget("text"), carga_total_bill3.cget("text"), 0, total_saldo_bill3),
                                                    sumar_num_bill("n", total_saldo_bill1.cget("text"), total_saldo_bill2.cget("text"), total_saldo_bill3.cget("text"), total_saldo_bill4.cget("text"), total_saldo_bill5.cget("text"), total_saldo_total_billetes),
                                                    sumar_num("n", total_saldo_total_billetes.cget("text"), total_saldo_total_monedas.cget("text"), 0, saldo_t_total_cajero_text)))
    
    carga_can_bill4.bind("<KeyRelease>", lambda e: (sumar_tiempo_real("n", carga_can_bill4.get(), carga_total_bill4, 0, billete4), sumar_num_bill("n", carga_can_bill1.get(), carga_can_bill2.get(), carga_can_bill3.get(), carga_can_bill4.get(), carga_can_bill5.get(), carga_cantidad_billetes),
                                                    sumar_num_bill("n", carga_total_bill1.cget("text"), carga_total_bill2.cget("text"), carga_total_bill3.cget("text"), carga_total_bill4.cget("text"), carga_total_bill5.cget("text"), carga_total_billetes),
                                                    sumar_num("n", carga_can_bill4.get(), saldo_antes_c_billete4_text.cget("text"), 0, can_saldo_bill4),
                                                    sumar_num_bill("n", can_saldo_bill1.cget("text"), can_saldo_bill2.cget("text"), can_saldo_bill3.cget("text"), can_saldo_bill4.cget("text"), can_saldo_bill5.cget("text"), can_saldo_total_billetes),
                                                    sumar_num("n", saldo_antes_t_billete4_text.cget("text"), carga_total_bill4.cget("text"), 0, total_saldo_bill4),
                                                    sumar_num_bill("n", total_saldo_bill1.cget("text"), total_saldo_bill2.cget("text"), total_saldo_bill3.cget("text"), total_saldo_bill4.cget("text"), total_saldo_bill5.cget("text"), total_saldo_total_billetes),
                                                    sumar_num("n", total_saldo_total_billetes.cget("text"), total_saldo_total_monedas.cget("text"), 0, saldo_t_total_cajero_text)))
    
    
    carga_can_bill5.bind("<KeyRelease>", lambda e: (sumar_tiempo_real("n", carga_can_bill5.get(), carga_total_bill5, 0, billete5), sumar_num_bill("n", carga_can_bill1.get(), carga_can_bill2.get(), carga_can_bill3.get(), carga_can_bill4.get(), carga_can_bill5.get(), carga_cantidad_billetes),
                                                    sumar_num_bill("n", carga_total_bill1.cget("text"), carga_total_bill2.cget("text"), carga_total_bill3.cget("text"), carga_total_bill4.cget("text"), carga_total_bill5.cget("text"), carga_total_billetes),
                                                    sumar_num("n", carga_can_bill5.get(), saldo_antes_c_billete5_text.cget("text"), 0, can_saldo_bill5),
                                                    sumar_num_bill("n", can_saldo_bill1.cget("text"), can_saldo_bill2.cget("text"), can_saldo_bill3.cget("text"), can_saldo_bill4.cget("text"), can_saldo_bill5.cget("text"), can_saldo_total_billetes),
                                                    sumar_num("n", saldo_antes_t_billete5_text.cget("text"), carga_total_bill5.cget("text"), 0, total_saldo_bill5),
                                                    sumar_num_bill("n", total_saldo_bill1.cget("text"), total_saldo_bill2.cget("text"), total_saldo_bill3.cget("text"), total_saldo_bill4.cget("text"), total_saldo_bill5.cget("text"), total_saldo_total_billetes),
                                                    sumar_num("n", total_saldo_total_billetes.cget("text"), total_saldo_total_monedas.cget("text"), 0, saldo_t_total_cajero_text)))
    
    ok = Button(frame, text="Ok", borderwidth=5, command=lambda: (actualizar_entradas(carga_can_mon1.get(), carga_can_mon2.get(), carga_can_mon3.get(), carga_can_bill1.get(), carga_can_bill2.get(), carga_can_bill3.get(), carga_can_bill4.get(), carga_can_bill5.get(),
                                                                                      carga_total_mon1.cget("text"), carga_total_mon2.cget("text"), carga_total_mon3.cget("text"), carga_total_bill1.cget("text"), carga_total_bill2.cget("text"), carga_total_bill3.cget("text"), carga_total_bill4.cget("text"), carga_total_bill5.cget("text"), carga_cantidad_monedas.cget("text"), carga_cantidad_billetes.cget("text"), carga_total_monedas.cget("text"), carga_total_billetes.cget("text")), vcargar.destroy()) if actualizar_saldo(can_saldo_mon1.cget("text"), can_saldo_mon2.cget("text"), can_saldo_mon3.cget("text"), can_saldo_bill1.cget("text"), can_saldo_bill2.cget("text"), can_saldo_bill3.cget("text"), can_saldo_bill4.cget("text"), can_saldo_bill5.cget("text"),
                                                                                    total_saldo_mon1.cget("text"), total_saldo_mon2.cget("text"), total_saldo_mon3.cget("text"), total_saldo_bill1.cget("text"), total_saldo_bill2.cget("text"), total_saldo_bill3.cget("text"), total_saldo_bill4.cget("text"), total_saldo_bill5.cget("text"), can_saldo_total_monedas.cget("text"), can_saldo_total_billetes.cget("text"), total_saldo_total_monedas.cget("text"), total_saldo_total_billetes.cget("text")) == True else None)
    ok.place(anchor="center", relx=0.4, rely =0.93)
    cancelar = Button(frame, text="Cancelar", borderwidth=5, command=vcargar.destroy).place(anchor="center", relx=0.55, rely =0.93)
#------------------------------------------------
# OPCIÓN ENTRADA DE VEHICULO                                                      
#------------------------------------------------
def entrada_vehiculo():
    global precio_x_hora, pago_minimo
    if verificar_datos_conf() == False:#validacion
        messagebox.showerror("Error","Primero debe de configurar todos los datos del estacionamiento en CONFIGURACION")
        return
    if num_espacios_parqueo() == 0:
        no_hay_espacio()
        return
    
    os.system("cls")
    ventrada = Toplevel()#nueva ventana
    ventrada.title("ESTACIONAMIENTO - ENTRADA DEL VEHÍCULO")
    ventrada.geometry("800x600")#dimensiones de la ventana
    ventrada.focus()#para que seleccione la ventana abierta
    ventrada.grab_set()#evita usar la ventana principal a menos que se haya cerrado la ventana abierta
    frame = Frame(ventrada)
    frame.place(relheight=1, relwidth=1)
    titulo = Label(frame, text="ESTACIONAMIENTO - ENTRADA DEL VEHÍCULO", borderwidth=10, relief="sunken").place(anchor="center", relx=0.5, rely=0.06)

    espacios_disponibles_text = Label(frame, text="Espacios disponibles").place(anchor="center", relx=0.3, rely=0.15)
    espacios_disponibles = Label(frame, text= str(num_espacios_parqueo())).place(anchor="center", relx=0.6, rely=0.15)

    placa_text = Label(frame, text="Su placa").place(anchor="center", relx=0.3, rely=0.25)
    placa = Entry(frame)
    placa.place(anchor="center", relx=0.6, rely=0.25)

    campo_asignado_text = Label(frame, text="Campo asignado").place(anchor="center", relx=0.3, rely=0.35)
    campo_asignado = Label(frame, text= str(buscar_parqueo() + 1))
    campo_asignado.place(anchor="center", relx=0.6, rely=0.35)

    precio_hora_text = Label(frame, text="Precio por hora").place(anchor="center", relx=0.3, rely=0.55)
    precio_hora = Label(frame, text=str(precio_x_hora)).place(anchor="center", relx=0.6, rely=0.55)

    pago_minimo_text = Label(frame, text="Pago mínimo").place(anchor="center", relx=0.3, rely=0.65)
    pago_minimo_mostrar = Label(frame, text=str(pago_minimo)).place(anchor="center", relx=0.6, rely=0.65)
    
    hora_de_entrada_text = Label(frame, text="Hora de entrada").place(anchor="center", relx=0.3, rely=0.45)
    hora_de_entrada = Label(frame, text=f"{datetime.now().strftime('%d/%m/%Y %H:%M')}")
    hora_de_entrada.place(anchor="center", relx=0.6, rely=0.45)
    refrescar_tiempo_boton = Button(frame, text="Refrescar tiempo", borderwidth=5, command=lambda: actualizar_tiempo(hora_de_entrada))
    refrescar_tiempo_boton.place(anchor="center", relx=0.8, rely=0.45)

    

    ok = Button(frame, text="Ok", borderwidth=5, command=lambda: ((ventrada.destroy(), entrada_vehiculo()) if reservar_espacio(placa.get(), campo_asignado.cget("text"), hora_de_entrada.cget("text")) == True else None) if verificar_placa(placa.get()) == True else None)
    ok.place(anchor="center", relx=0.4, rely =0.75)
    cancelar = Button(frame, text="Cancelar", borderwidth=5, command=ventrada.destroy).place(anchor="center", relx=0.55, rely =0.75)

#------------------------------------------------
# OPCIÓN CAJERO DEL PARQUEO                                                     
#------------------------------------------------
def cajero_parqueo():
    if verificar_datos_conf() == False:#validacion
        messagebox.showerror("Error","Primero debe de configurar todos los datos del estacionamiento en CONFIGURACION")
        return
    global moneda1, moneda2, moneda3, billete1, billete2, billete3, billete4, billete5
    os.system("cls")
    vcajero = Toplevel()#nueva ventana
    vcajero.title("ESTACIONAMIENTO - CAJERO DEL PARQUEO")
    vcajero.geometry("800x600")#dimensiones de la ventana
    vcajero.focus()#para que seleccione la ventana abierta
    vcajero.grab_set()#evita usar la ventana principal a menos que se haya cerrado la ventana abierta
    frame = Frame(vcajero)
    frame.place(relheight=1, relwidth=1)
    titulo = Label(frame, text="CAJERO", borderwidth=10, relief="sunken").place(anchor="center", relx=0.5, rely=0.06)
    xx_por_hora = Label(frame, text=f"{precio_x_hora} POR HORA").place(anchor="center", relx=0.7, rely=0.06)
    Paso1 = Label(frame, text="PASO 1: SU PLACA").place(anchor="center", relx=0.1, rely=0.12)
    insertar_placa = Entry(frame)
    insertar_placa.place(anchor="center", relx=0.3, rely=0.12)
    insertar_placa.bind("<KeyRelease>", lambda e: cajero_parqueo2(frame, insertar_placa.get(), vcajero))
    
def cajero_parqueo2(frame, placa, vcajero):
    global parqueo, precio_x_hora, moneda1, moneda2, moneda3, billete1, billete2, billete3, billete4, billete5
    existe = False
    if datos_placa(placa)[0] != False:
        existe = True

    #si no existe la placa, se reinicia la pagina
    if existe == False:
        destruir_widgets_cajero(frame)
        titulo = Label(frame, text="CAJERO", borderwidth=10, relief="sunken").place(anchor="center", relx=0.5, rely=0.06)
        xx_por_hora = Label(frame, text=f"{precio_x_hora} POR HORA").place(anchor="center", relx=0.7, rely=0.06)
        Paso1 = Label(frame, text="PASO 1: SU PLACA").place(anchor="center", relx=0.1, rely=0.12)
    #si existe la placa, se muestran los demas datos
    else:
        datos = datos_placa(placa)[0]
        datos2 = datos_placa(placa)[1]
        salida = datetime.now().strftime('%d/%m/%Y %H:%M')
        tiempo_dif = de_string_a_fecha_con_hora(salida) - de_string_a_fecha_con_hora(datos[1])  #vemos cuanto tiempo se a quedado
        horas_min_sec = (datetime.min + tiempo_dif).time() #pasamos de formato timedelta a datetime
        hora_de_entrada_text = Label(frame, text="Hora de entrada").place(anchor="center", relx=0.1, rely=0.17)
        hora_de_entrada = Label(frame, text=f"{datos[1]}").place(anchor="center", relx=0.3, rely=0.17)
        hora_de_salida_text = Label(frame, text="Hora de salida").place(anchor="center", relx=0.1, rely=0.22)
        hora_de_salida = Label(frame, text=f"{salida}").place(anchor="center", relx=0.3, rely=0.22)
        tiempo_cobrado_text = Label(frame, text="Tiempo cobrado").place(anchor="center", relx=0.1, rely=0.27)
        if datos_placa(placa)[1] == "x":
            tiempo_cobrado_d = Label(frame, text=f"{tiempo_dif.days}d").place(anchor="center", relx=0.26, rely=0.27)
            tiempo_cobrado_h = Label(frame, text=f"{horas_min_sec.hour}h").place(anchor="center", relx=0.3, rely=0.27)
            tiempo_cobrado_m = Label(frame, text=f"{horas_min_sec.minute}m").place(anchor="center", relx=0.33, rely=0.27)
        else:
            tiempo_cobrado_d = Label(frame, text=f"{datos2[0]}d").place(anchor="center", relx=0.26, rely=0.27)
            tiempo_cobrado_h = Label(frame, text=f"{datos2[1]}h").place(anchor="center", relx=0.3, rely=0.27)
            tiempo_cobrado_m = Label(frame, text=f"{datos2[2]}m").place(anchor="center", relx=0.33, rely=0.27)
        a_pagar_text = Label(frame, text="A PAGAR:").place(anchor="center", relx=0.5, rely=0.12)
        cuadro_a_pagar = Frame(frame)
        cuadro_a_pagar.config(background="red", width=150, height=100)
        cuadro_a_pagar.place(anchor="center", relx= 0.5, rely=0.22)
        if datos_placa(placa)[1] == "x":
            monto_a_pagar = Label(cuadro_a_pagar, text=f"{multiplo_de_cercano(moneda_menos_valor(moneda1, moneda2, moneda3, billete1, billete2, billete3, billete4, billete5), calcular_cobro(tiempo_dif.days, horas_min_sec.hour, horas_min_sec.minute))}", background="red")
        else: 
            monto_a_pagar = Label(cuadro_a_pagar, text=f"{multiplo_de_cercano(moneda_menos_valor(moneda1, moneda2, moneda3, billete1, billete2, billete3, billete4, billete5), calcular_cobro(datos2[0], datos2[1], datos2[2]))}", background="red")
        monto_a_pagar.place(anchor="center", relx=0.5, rely=0.5)
        monto_a_pagar.config(font= ("Verdana", 24))

        pago = 0
        pago_texto = Label(frame, text="PAGO").place(anchor="center", relx=0.67, rely=0.17)
        cuadro_pago = Frame(frame)
        cuadro_pago.config(background="green", width=75, height=25)
        cuadro_pago.place(anchor="center", relx=0.77, rely=0.17)
        monto_pago = Label(cuadro_pago, background="green")
        monto_pago.place(anchor="center", relx=0.5, rely=0.5)
        monto_pago.config(font= ("Verdana", 13), text=f"{pago}")

        mon1_usadas = IntVar()
        mon2_usadas = IntVar()
        mon3_usadas = IntVar()
        bill1_usadas = IntVar()
        bill2_usadas = IntVar()
        bill3_usadas = IntVar()
        bill4_usadas = IntVar()
        bill5_usadas = IntVar()

        suma = IntVar(value=1)

        #paso2
        Paso2_text = Label(frame, text="PASO 2: SU PAGO EN:").place(anchor="center", relx=0.1, rely=0.37)
        monedas_text = Label(frame, text="MONEDAS").place(anchor="center", relx=0.27, rely=0.37)
        billetes_text = Label(frame, text="BILLETES").place(anchor="center", relx=0.42, rely=0.37)
        tarjeta_text = Label(frame, text="TARJETA DE CREDITO").place(anchor="center", relx=0.62, rely=0.37)
        ingresar_tarjeta = Entry(frame)
        ingresar_tarjeta.place(anchor="center", relx=0.62, rely=0.42)
        ingresar_tarjeta.bind("<KeyRelease>", lambda e: ver_tarjeta(ingresar_tarjeta.get(), frame, int(monto_pago.cget("text")), int(monto_a_pagar.cget("text")), [0, 0, 0, 0, 0, 0, 0, 0], vcajero, monto_pago, placa))
        boton_anular = Button(frame)
        boton_anular.config(text="ANULAR EL PAGO", command=lambda: (frame.destroy(), refrescar_cajero(vcajero)))
        boton_anular.place(anchor="center", relx=0.2, rely=0.94)

        boton_mon1 = Button(frame)  
        boton_mon1.config(text=f"{moneda1}", command=lambda: ((sumar_mon(mon1_usadas, int(monto_a_pagar.cget("text")), int(monto_pago.cget("text"))), aumentar_pago(monto_pago, moneda1, int(monto_a_pagar.cget("text")), int(monto_pago.cget("text"))))
                                                              , cajero_parqueo3(frame, int(monto_pago.cget("text")), int(monto_a_pagar.cget("text")), [bill5_usadas.get(), bill4_usadas.get(), bill3_usadas.get(), bill2_usadas.get(), bill1_usadas.get(), mon3_usadas.get(), mon2_usadas.get(), mon1_usadas.get()], vcajero, placa, False)
                                                              if int(monto_pago.cget("text")) >= int(monto_a_pagar.cget("text")) else None))
        boton_mon1.place(anchor="center", relx=0.27, rely=0.42)
        boton_mon2 = Button(frame)
        boton_mon2.config(text=f"{moneda2}", command=lambda: ((sumar_mon(mon2_usadas, int(monto_a_pagar.cget("text")), int(monto_pago.cget("text"))), aumentar_pago(monto_pago, moneda2, int(monto_a_pagar.cget("text")), int(monto_pago.cget("text"))))
                                                              , cajero_parqueo3(frame, int(monto_pago.cget("text")), int(monto_a_pagar.cget("text")), [bill5_usadas.get(), bill4_usadas.get(), bill3_usadas.get(), bill2_usadas.get(), bill1_usadas.get(), mon3_usadas.get(), mon2_usadas.get(), mon1_usadas.get()], vcajero, placa, False) 
                                                              if int(monto_pago.cget("text")) >= int(monto_a_pagar.cget("text")) else None))
        boton_mon2.place(anchor="center", relx=0.27, rely=0.47)
        boton_mon3 = Button(frame)
        boton_mon3.config(text=f"{moneda3}", command=lambda: ((sumar_mon(mon3_usadas, int(monto_a_pagar.cget("text")), int(monto_pago.cget("text"))), aumentar_pago(monto_pago, moneda3, int(monto_a_pagar.cget("text")), int(monto_pago.cget("text"))))
                                                              , cajero_parqueo3(frame, int(monto_pago.cget("text")), int(monto_a_pagar.cget("text")), [bill5_usadas.get(), bill4_usadas.get(), bill3_usadas.get(), bill2_usadas.get(), bill1_usadas.get(), mon3_usadas.get(), mon2_usadas.get(), mon1_usadas.get()], vcajero, placa, False) 
                                                              if int(monto_pago.cget("text")) >= int(monto_a_pagar.cget("text")) else None))
        boton_mon3.place(anchor="center", relx=0.27, rely=0.52)
        boton_bill1 = Button(frame)
        boton_bill1.config(text=f"{billete1}", command=lambda: ((sumar_mon(bill1_usadas, int(monto_a_pagar.cget("text")), int(monto_pago.cget("text"))), aumentar_pago(monto_pago, billete1, int(monto_a_pagar.cget("text")), int(monto_pago.cget("text"))))
                                                                , cajero_parqueo3(frame, int(monto_pago.cget("text")), int(monto_a_pagar.cget("text")), [bill5_usadas.get(), bill4_usadas.get(), bill3_usadas.get(), bill2_usadas.get(), bill1_usadas.get(), mon3_usadas.get(), mon2_usadas.get(), mon1_usadas.get()], vcajero, placa, False) 
                                                                if int(monto_pago.cget("text")) >= int(monto_a_pagar.cget("text")) else None))
        boton_bill1.place(anchor="center", relx=0.42, rely=0.42)
        boton_bill2 = Button(frame)
        boton_bill2.config(text=f"{billete2}", command=lambda: ((sumar_mon(bill2_usadas, int(monto_a_pagar.cget("text")), int(monto_pago.cget("text"))), aumentar_pago(monto_pago, billete2, int(monto_a_pagar.cget("text")), int(monto_pago.cget("text"))))
                                                                , cajero_parqueo3(frame, int(monto_pago.cget("text")), int(monto_a_pagar.cget("text")), [bill5_usadas.get(), bill4_usadas.get(), bill3_usadas.get(), bill2_usadas.get(), bill1_usadas.get(), mon3_usadas.get(), mon2_usadas.get(), mon1_usadas.get()], vcajero, placa, False) 
                                                                if int(monto_pago.cget("text")) >= int(monto_a_pagar.cget("text")) else None))
        boton_bill2.place(anchor="center", relx=0.42, rely=0.47)
        boton_bill3 = Button(frame)
        boton_bill3.config(text=f"{billete3}", command=lambda: ((sumar_mon(bill3_usadas, int(monto_a_pagar.cget("text")), int(monto_pago.cget("text"))), aumentar_pago(monto_pago, billete3, int(monto_a_pagar.cget("text")), int(monto_pago.cget("text"))))
                                                                , cajero_parqueo3(frame, int(monto_pago.cget("text")), int(monto_a_pagar.cget("text")), [bill5_usadas.get(), bill4_usadas.get(), bill3_usadas.get(), bill2_usadas.get(), bill1_usadas.get(), mon3_usadas.get(), mon2_usadas.get(), mon1_usadas.get()], vcajero, placa, False) 
                                                                if int(monto_pago.cget("text")) >= int(monto_a_pagar.cget("text")) else None))
        boton_bill3.place(anchor="center", relx=0.42, rely=0.52)
        boton_bill4 = Button(frame)
        boton_bill4.config(text=f"{billete4}", command=lambda: ((sumar_mon(bill4_usadas, int(monto_a_pagar.cget("text")), int(monto_pago.cget("text"))), aumentar_pago(monto_pago, billete4, int(monto_a_pagar.cget("text")), int(monto_pago.cget("text"))))
                                                                , cajero_parqueo3(frame, int(monto_pago.cget("text")), int(monto_a_pagar.cget("text")), [bill5_usadas.get(), bill4_usadas.get(), bill3_usadas.get(), bill2_usadas.get(), bill1_usadas.get(), mon3_usadas.get(), mon2_usadas.get(), mon1_usadas.get()], vcajero, placa, False) 
                                                                if int(monto_pago.cget("text")) >= int(monto_a_pagar.cget("text")) else None))
        boton_bill4.place(anchor="center", relx=0.42, rely=0.57)
        boton_bill5 = Button(frame)
        boton_bill5.config(text=f"{billete5}", command=lambda: ((sumar_mon(bill5_usadas, int(monto_a_pagar.cget("text")), int(monto_pago.cget("text"))), aumentar_pago(monto_pago, billete5, int(monto_a_pagar.cget("text")), int(monto_pago.cget("text"))))
                                                                , cajero_parqueo3(frame, int(monto_pago.cget("text")), int(monto_a_pagar.cget("text")), [bill5_usadas.get(), bill4_usadas.get(), bill3_usadas.get(), bill2_usadas.get(), bill1_usadas.get(), mon3_usadas.get(), mon2_usadas.get(), mon1_usadas.get()], vcajero, placa, False) 
                                                                if int(monto_pago.cget("text")) >= int(monto_a_pagar.cget("text")) else None))
        boton_bill5.place(anchor="center", relx=0.42, rely=0.62)

def cajero_parqueo3(frame, pago, a_pagar, lista_plata_ingresada, vcajero, placa, tarjeta): 
    global dic_moneda1, dic_moneda2, dic_moneda3, dic_billete1, dic_billete2, dic_billete3, dic_billete4, dic_billete5, billete5, billete4, billete3, billete2, billete1, moneda3, moneda2, moneda1
    
    #paso3
    cambio = pago - a_pagar
    if tarjeta == False:
        devolver = hay_monedas(cambio_calculo(moneda1, moneda2, moneda3, billete1, billete2, billete3, billete4, billete5, cambio), lista_plata_ingresada, [dic_billete5, dic_billete4, dic_billete3, dic_billete2, dic_billete1, dic_moneda3, dic_moneda2, dic_moneda1], [billete5, billete4, billete3, billete2, billete1, moneda3, moneda2, moneda1])
        if devolver == False:
            return
    #este frame oculta el boton anular
    tapar_anular = Frame(frame)
    tapar_anular.config(width=150, height=40)
    tapar_anular.place(anchor="center", relx=0.2, rely=0.94)
    tapar_placa = Frame(frame)
    tapar_placa.config(width=150, height=40)
    tapar_placa.place(anchor="center", relx=0.3, rely=0.12)
    tapar_botones = Frame(frame)
    tapar_botones.config(width=560, height=200)
    tapar_botones.place(anchor="center", relx=0.37, rely=0.48)

    Paso2_text = Label(frame, text="PASO 3: SU CAMBIO EN:").place(anchor="center", relx=0.1, rely=0.7)
    monedas_paso3_text = Label(frame, text="MONEDAS").place(anchor="center", relx=0.27, rely=0.7)
    billetes_paso3_text = Label(frame, text="BILLETES").place(anchor="center", relx=0.42, rely=0.7)
    if tarjeta == False:
        mostrar_mon1 =Label(frame, text=f"{int(devolver[7])} de {moneda1}").place(anchor="center", relx=0.27, rely=0.75)
        mostrar_mon2 =Label(frame, text=f"{int(devolver[6])} de {moneda2}").place(anchor="center", relx=0.27, rely=0.8)
        mostrar_mon3 =Label(frame, text=f"{int(devolver[5])} de {moneda3}").place(anchor="center", relx=0.27, rely=0.85)
        mostrar_bill1 =Label(frame, text=f"{int(devolver[4])} de {billete1}").place(anchor="center", relx=0.42, rely=0.75)
        mostrar_bill2 =Label(frame, text=f"{int(devolver[3])} de {billete2}").place(anchor="center", relx=0.42, rely=0.8)
        mostrar_bill3 =Label(frame, text=f"{int(devolver[2])} de {billete3}").place(anchor="center", relx=0.42, rely=0.85)
        mostrar_bill4 =Label(frame, text=f"{int(devolver[1])} de {billete4}").place(anchor="center", relx=0.42, rely=0.9)
        mostrar_bill5 =Label(frame, text=f"{int(devolver[0])} de {billete5}").place(anchor="center", relx=0.42, rely=0.95)
    else:
        mostrar_mon1 =Label(frame, text=f"0 de {moneda1}").place(anchor="center", relx=0.27, rely=0.75)
        mostrar_mon2 =Label(frame, text=f"0 de {moneda2}").place(anchor="center", relx=0.27, rely=0.8)
        mostrar_mon3 =Label(frame, text=f"0 de {moneda3}").place(anchor="center", relx=0.27, rely=0.85)
        mostrar_bill1 =Label(frame, text=f"0 de {billete1}").place(anchor="center", relx=0.42, rely=0.75)
        mostrar_bill2 =Label(frame, text=f"0 de {billete2}").place(anchor="center", relx=0.42, rely=0.8)
        mostrar_bill3 =Label(frame, text=f"0 de {billete3}").place(anchor="center", relx=0.42, rely=0.85)
        mostrar_bill4 =Label(frame, text=f"0 de {billete4}").place(anchor="center", relx=0.42, rely=0.9)
        mostrar_bill5 =Label(frame, text=f"0 de {billete5}").place(anchor="center", relx=0.42, rely=0.95)

    cambio_texto = Label(frame, text="CAMBIO").place(anchor="center", relx=0.67, rely=0.22)
    cuadro_cambio = Frame(frame)
    cuadro_cambio.config(background="green", width=75, height=25)
    cuadro_cambio.place(anchor="center", relx=0.77, rely=0.22)
    monto_cambio = Label(cuadro_cambio, text=f"{cambio}", background="green")
    monto_cambio.place(anchor="center", relx=0.5, rely=0.5)
    monto_cambio.config(font=("Verdana", 13))
    vcajero.after(7000, lambda: (frame.destroy(), refrescar_cajero(vcajero), actualizar_datos_placa(placa, a_pagar)))
#------------------------------------------------
# OPCIÓN SALIDA DEL VEHICULO                                                      
#------------------------------------------------
def salida_vehiculo():
    if verificar_datos_conf() == False:#validacion
        messagebox.showerror("Error","Primero debe de configurar todos los datos del estacionamiento en CONFIGURACION")
        return
    os.system("cls")
    vsalidav = Toplevel()#nueva ventana
    vsalidav.title("ESTACIONAMIENTO - SALIDA DE VEHÍCULO")
    vsalidav.geometry("500x200")#dimensiones de la ventana
    vsalidav.focus()#para que seleccione la ventana abierta
    vsalidav.grab_set()#evita usar la ventana principal a menos que se haya cerrado la ventana abierta
    frame = Frame(vsalidav)
    frame.place(relheight=1, relwidth=1)
    titulo = Label(frame, text="SALIDA DEL VEHÍCULO", borderwidth=10, relief="sunken").place(anchor="center", relx=0.5, rely=0.09)

    su_placa_text = Label(frame, text="SU PLACA").place(anchor="center", relx=0.2, rely=0.4)
    ingresar_placa = Entry(frame)
    ingresar_placa.place(anchor="center", relx=0.5, rely=0.4)
    ok = Button(frame, text="Ok", borderwidth=5, command=lambda: verificar_salida(ingresar_placa.get())).place(anchor="center", relx=0.4, rely =0.7)
    cancelar = Button(frame, text="Cancelar", borderwidth=5, command=lambda: (vsalidav.destroy())).place(anchor="center", relx=0.6, rely =0.7)

#------------------------------------------------
# OPCIÓN REPORTE DE INGRESOS DE DINERO                                                     
#------------------------------------------------
def reporte_ingresos():
    if verificar_datos_conf() == False:#validacion
        messagebox.showerror("Error","Primero debe de configurar todos los datos del estacionamiento en CONFIGURACION")
        return
    os.system("cls")
    vreporte = Toplevel()#nueva ventana
    vreporte.title("ESTACIONAMIENTO - REPORTE DE INGRESOS DE DINERO")
    vreporte.geometry("800x600")#dimensiones de la ventana
    vreporte.focus()#para que seleccione la ventana abierta
    vreporte.grab_set()#evita usar la ventana principal a menos que se haya cerrado la ventana abierta
    frame = Frame(vreporte)
    frame.place(relheight=1, relwidth=1)
    titulo = Label(frame, text="REPORTE DE INGRESOS DE DINERO", borderwidth=10, relief="sunken").place(anchor="center", relx=0.5, rely=0.09)

    ingresos_desde_text = Label(frame, text="Ingresos desde el día:").place(anchor="center", relx=0.3, rely=0.17)
    ingresos_desde = Entry(frame)
    ingresos_desde.place(anchor="center", relx=0.57, rely=0.17)
    ingresos_desde.bind("<Key>", lambda e: escribir_fechas(e, ingresos_desde))
    ingresos_desde.bind("<BackSpace>", lambda: None)

    ingresos_hasta_text = Label(frame, text="Hasta el día:").place(anchor="center", relx=0.3, rely=0.22)
    ingresos_hasta = Entry(frame)
    ingresos_hasta.place(anchor="center", relx=0.57, rely=0.22)
    ingresos_hasta.bind("<Key>", lambda e: escribir_fechas(e, ingresos_hasta))
    ingresos_hasta.bind("<BackSpace>", lambda: None)

    total_ingresos_text = Label(frame, text=f"TOTAL DE INGRESOS:").place(anchor="center", relx=0.3, rely=0.33)
    total_ingresos = Label(frame, text="")
    total_ingresos.place(anchor="center", relx=0.57, rely=0.3)


    estimacion_text = Label(frame, text="Para hacer una estimación de ingresos digite la fecha y hora hasta la cual ocupa la estimación:").place(anchor="center", relx=0.5, rely= 0.47)
    fecha_estimacion_text = Label(frame, text="Fecha para la estimación:").place(anchor="center", relx=0.3, rely=0.52)
    fecha_estimacion = Entry(frame)
    fecha_estimacion.place(anchor="center", relx=0.57, rely=0.52)
    fecha_estimacion.bind("<Key>", lambda e: escribir_fechas(e, fecha_estimacion))
    fecha_estimacion.bind("<BackSpace>", lambda: None)

    hora_estimacion_text = Label(frame, text="Hora para la estimación: (formato 24h)").place(anchor="center", relx=0.3, rely=0.57)
    hora_estimacion = Entry(frame)
    hora_estimacion.place(anchor="center", relx=0.57, rely=0.57)
    hora_estimacion.bind("<Key>", lambda e: escribir_horas(e, hora_estimacion))
    hora_estimacion.bind("<BackSpace>", lambda: None)

    estimados_x_recibir_text = Label(frame, text="ESTIMADO DE INGRESOS POR RECIBIR:").place(anchor="center", relx=0.3, rely=0.72)
    estimados_x_recibir = Label(frame, text="")
    estimados_x_recibir.place(anchor="center", relx=0.57, rely=0.72)

    ok = Button(frame, text="Ok", borderwidth=5, command=0)
    ok.config(command=lambda: (ingresos_desde_hasta(ingresos_desde.get(), ingresos_hasta.get(), frame, total_ingresos) if ingresos_desde.get() != "" or ingresos_hasta.get() != "" else estimacion_ingresos(fecha_estimacion.get(), hora_estimacion.get(), frame, estimados_x_recibir) if fecha_estimacion.get() != "" or hora_estimacion.get() != "" else None))
    ok.place(anchor="center", relx=0.34, rely =0.85)
    cancelar = Button(frame, text="Cancelar", borderwidth=5, command=vreporte.destroy).place(anchor="center", relx=0.55, rely =0.85)

    #esta funcion se encarga de agregar / cuando se escribe para dar el formato de fecha
    #la funcion se crea aqui, pues si no da error
    def escribir_fechas(event, cuadro):
        if event.char.isdigit():    #lo ingresado es un digito
            texto = cuadro.get()
            no_letras = 0
            for i in texto:
                no_letras +=1
            if no_letras == 2:
                cuadro.insert(2,"/")
            elif no_letras == 5:
                cuadro.insert(5,"/")
            elif no_letras == 10:
                return "break"
        else:
            return "break"
    
    #esta funcion se encarga de agregar : cuando se escribe para dar el formato a la hora
    def escribir_horas(event, cuadro):
        if event.char.isdigit():    #lo ingresado es un digito
            texto = cuadro.get()
            no_letras = 0
            for i in texto:
                no_letras +=1
            if no_letras == 2:
                cuadro.insert(2,":")
            elif no_letras == 5:
                return "break"
        else:
            return "break"
        
    #esta funcion permite obtener los ingresos del estacionamiento totales desde "x" fecha hasta "x" fecha
    def ingresos_desde_hasta(desde, hasta, frame, total_ingresos):
        global historial_parqueo
        total = 0
        try:
            #si la fecha desde es mayor a la fecha hasta
            if datetime.strptime(desde, '%d/%m/%Y') > datetime.strptime(hasta, '%d/%m/%Y'):
                messagebox.showerror("ERROR", "La fecha 'ingresos desde el día' debe de ser antes que la fecha 'hasta el dia'")
                total_ingresos = Label(frame, text="")
                total_ingresos.place(anchor="center", relx=0.57, rely=0.33)
                return False
        except:
            #ingreso una fecha invalida
            messagebox.showerror("ERROR", "Por favor ingrese una fecha válida")
            total_ingresos.config(text="")
            return False
        for cada_parqueo in historial_parqueo:
            #si la fecha está entre las fechas dadas
            if datetime.strptime((cada_parqueo[3][:10]), '%d/%m/%Y')  >= datetime.strptime(desde, '%d/%m/%Y') and datetime.strptime((cada_parqueo[3][:10]), '%d/%m/%Y') <= ( datetime.strptime(hasta, '%d/%m/%Y') + timedelta(days = 1)): #le sumamos un dia ya que si no, contaria desde el la fecha hasta a partir de las 12 de la media noche.
                total += cada_parqueo[4]
        
        total_ingresos.config(text=f"{total}")
    
    #esta funcion realiza todos los calculos para obtener la estimacion de los ingresos
    def estimacion_ingresos(fecha, hora, frame, estimados_x_recibir):
        global moneda1, moneda2, moneda3, billete1, billete2, billete3, billete4, billete5
        total = 0
        try:
            fecha_final = fecha + " " + hora
            fecha_final = de_string_a_fecha_con_hora(fecha_final)
        except:
            messagebox.showerror("ERROR", "Por favor ingrese una fecha y hora válida")
            estimados_x_recibir.config(text="")
        for cada_parqueo in parqueo:
            #evitamos los parqueos vacios
            if cada_parqueo != []:

                #vemos si la hora de entrada es menor o igual a la hora dada 
                if de_string_a_fecha_con_hora(cada_parqueo[1]) <= fecha_final:

                    tiempo_dif = fecha_final - de_string_a_fecha_con_hora(cada_parqueo[1])  #dias
                    horas_min_sec = (datetime.min + tiempo_dif).time() #pasamos de formato timedelta a datetime
                    #tomamos la ganancia si hubiera salido a hora final
                    total += multiplo_de_cercano(moneda_menos_valor(moneda1, moneda2, moneda3, billete1, billete2, billete3, billete4, billete5), calcular_cobro(tiempo_dif.days, horas_min_sec.hour, horas_min_sec.minute))
        
        estimados_x_recibir.config(text=f"{total}")

#------------------------------------------------
# OPCIÓN AYUDA                                                     
#------------------------------------------------
def ayuda():
    path = "Dilan_Manual_de_usuario_Estacionamiento_de_vehiculos.pdf"
    os.system(path)

#------------------------------------------------
# OPCIÓN ACERCA DE                                                      
#------------------------------------------------
def acerca_de():
    os.system("cls")
    vacerca = Toplevel()#nueva ventana
    vacerca.title("ESTACIONAMIENTO - ACERCA DE")
    vacerca.geometry("600x300")#dimensiones de la ventana
    vacerca.focus()#para que seleccione la ventana abierta
    vacerca.grab_set()#evita usar la ventana principal a menos que se haya cerrado la ventana abierta
    frame = Frame(vacerca)
    frame.place(relheight=1, relwidth=1)

    nombre_text = Label(frame, text="NOMBRE DEL PROGRAMA: ESTACIONAMIENTO DE VEHÍCULOS").place(anchor="center", relx=0.5, rely=0.2)
    version_text = Label(frame, text="VERSION DEL PROGRAMA: 1.0").place(anchor="center", relx=0.5, rely=0.4)
    fecha_text = Label(frame, text="FECHA DE CREACIÓN DEL PROGRAMA: 17/06/2024").place(anchor="center", relx=0.5, rely=0.6)
    autor_text = Label(frame, text="AUTOR DEL PROGRAMA: DILAN HERNÁNDEZ SÁNCHEZ").place(anchor="center", relx=0.5, rely=0.8)


#------------------------------------------------------------------------
# FUNCIÓN PRINCIPAL                                                     
#------------------------------------------------------------------------

#------------------------------------------------------------------------
#DATOS CONFIGURADOS
#------------------------------------------------------------------------
#leer datos:
num_espacios, precio_x_hora, pago_minimo, redondeo_tiempo, minutos_max, parqueo, historial_parqueo, moneda1, moneda2, moneda3, billete1, billete2, billete3, billete4, billete5, dic_moneda1, dic_moneda2, dic_moneda3, dic_billete1, dic_billete2, dic_billete3, dic_billete4, dic_billete5 = leer_archivos()

refrescar_diccionarios()
#------------------------------------------------------------------------

#ventana-------------------------------------------------------------------------------------------------------------------
ventana = Tk()#creamos la ventana
ventana.geometry("800x600")#dimensiones de la ventana
ventana.title("Estacionamiento de vehiculos")#titulo de la ventana

#MENU-------------------------------------------------------------------------------------------------------------------
os.system("cls")
menubar = Menu(ventana)#creamos la barra de menu
filemenu = Menu(menubar, tearoff=0)#creamos el menu
sub_dinero = Menu(menubar, tearoff=0)
menubar.add_command(label="Configuración", command=configuracion)#creamos la opcion del menu
menubar.add_cascade(label="Dinero en el cajero", menu=filemenu)#submenu de la opción
filemenu.add_command(label="Saldo del cajero", command=saldo_cajero) 
filemenu.add_command(label="Cargar cajero", command=cargar_cajero) 
menubar.add_command(label="Entrada del vehículo", command=entrada_vehiculo)
menubar.add_command(label="Cajero", command=cajero_parqueo)
menubar.add_command(label="Salida del vehículo", command=salida_vehiculo)
menubar.add_command(label="Reporte de ingresos de dinero", command=reporte_ingresos)
menubar.add_command(label="Ayuda", command=ayuda)
menubar.add_command(label="Acerca de", command=acerca_de)
menubar.add_command(label="Salir", command=lambda: (grabar_archivos(num_espacios, precio_x_hora, pago_minimo, redondeo_tiempo, minutos_max, parqueo, historial_parqueo, moneda1, moneda2, moneda3, billete1, billete2, billete3, billete4, billete5, dic_moneda1, dic_moneda2, dic_moneda3, dic_billete1, dic_billete2, dic_billete3, dic_billete4, dic_billete5), ventana.quit()))
ventana.config(menu=menubar)#muestra la barra de menu
titulo = Label(ventana, text="Bienvenido al estacionamiento de vehículos, seleccione una opción.", borderwidth=10, relief="sunken").place(anchor="center", relx=0.5, rely=0.06)
#si toca la x de salir de la ventana, se guardan los archivos
ventana.protocol("WM_DELETE_WINDOW", lambda: (grabar_archivos(num_espacios, precio_x_hora, pago_minimo, redondeo_tiempo, minutos_max, parqueo, historial_parqueo, moneda1, moneda2, moneda3, billete1, billete2, billete3, billete4, billete5, dic_moneda1, dic_moneda2, dic_moneda3, dic_billete1, dic_billete2, dic_billete3, dic_billete4, dic_billete5), ventana.destroy()))
ventana.mainloop()
