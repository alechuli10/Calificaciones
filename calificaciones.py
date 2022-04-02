def ordenarLista (listaDiccionarios):
    for i in range(len(listaDiccionarios)):
        for j in range(1,len(listaDiccionarios)):
            if listaDiccionarios[j]["Apellidos"]<listaDiccionarios[j-1]["Apellidos"]:
                aux= listaDiccionarios[j]
                listaDiccionarios[j]= listaDiccionarios[j-1]
                listaDiccionarios[j-1]= aux 

def leerFichero (nombreFichero):
    fichero= open(nombreFichero,"r")
    lineas= fichero.readlines()
    linea= lineas[0]
    lineas.remove(linea)
    linea= linea.replace("\n", "")
    campos= linea.split(";")
    resultado= []
    for linea in lineas:
        diccionario= {}
        for i in range(len(campos)):
            linea= linea.replace("\n", "")
            l= linea.split(";")
            diccionario[campos[i]]= l[i]
        resultado.append(diccionario)
    ordenarLista(resultado)
    return resultado

def transformarDato (cadena):
    if not cadena:
        dato= 0.0
    else:
        dato= float(cadena.replace(",","."))
    return dato

def calcularNotaFinal (listaDiccionarios):
    for diccionario in listaDiccionarios:
        nota1=transformarDato (diccionario["Parcial1"])
        nota2=transformarDato (diccionario["Parcial2"])
        practica=transformarDato (diccionario["Practicas"])
        notaFinal= nota1*0.3+nota2*0.3+practica*0.4
        diccionario["NotaFinal"]= notaFinal
        
def clasificarAlumnos (listaDiccionarios):
    aprobados= []
    suspensos= []
    for diccionario in listaDiccionarios:
        aprobado= True
        asistencia= diccionario["Asistencia"].replace("%","")
        if transformarDato (asistencia)<75:
            aprobado= False
        if transformarDato(diccionario["Parcial1"])<4:
            aprobado= False
        if transformarDato(diccionario["Parcial2"])<4:
            aprobado= False
        if transformarDato(diccionario["Practicas"])<4:
            aprobado= False
        if diccionario["NotaFinal"]<5:
            aprobado= False
        if aprobado:
            aprobados.append(diccionario)
        else:
            suspensos.append(diccionario)
    return aprobados,suspensos