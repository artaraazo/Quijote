#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 23:27:43 2022

@author: artutaraperegmail.com
"""
import random

archivo_entrada = open('quijote.txt', 'r')
archivo_salida = open('quijote_s05.txt', 'w')
p = random.random()
for linea in archivo_entrada:
    d = random.random()
    if d <= p:
        archivo_salida.write(linea)
archivo_entrada.close()
archivo_salida.close()