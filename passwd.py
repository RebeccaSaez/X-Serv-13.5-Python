#!/usr/bin/python

fich = open("/etc/passwd", "r")
lineas = fich.readlines()
fich.close()

dicc = {}

for linea in lineas:
    conf = linea.split(":")
    dicc[conf[0]] = conf[-1][:-1]
    
print "Numero de usuarios de la maquina: ", len(dicc)
print "root", ": ", dicc["root"]

try:
    print "imaginario", ": ", dicc["imaginario"]
except KeyError:
    print "No es un usuario real"
