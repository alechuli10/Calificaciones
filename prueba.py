from calificaciones import *

def probar ():
  lista= leerFichero("./calificaciones.csv")
  calcularNotaFinal(lista)
  aprobados,suspensos= clasificarAlumnos(lista)
  print (lista)
  print ("----------------------------------------")
  print (aprobados)
  print ("----------------------------------------")
  print (suspensos)