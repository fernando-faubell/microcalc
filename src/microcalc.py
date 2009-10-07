#!/usr/bin/python

from sintactico import *
import sys

if __name__ == '__main__':

  
  linea = sys.stdin.readline()

  print linea
  
  lexico = Lexico(linea)
  while True:
    componente= lexico.siguiente()
    print componente
    if componente.cat== 'eof':
      break



#  sintactico = Sintactico(lexico)
#  sintactico.analizaLinea()
