#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 00:31:39 2023

@author: pichardo
"""

def calcular_IMC(peso:float,altura:float)->float:
    return peso/(altura**2)

def calcular_porcentaje_grasa(peso:float,altura:float,edad:float,valor_genero:float)->float:
    return 1.2 * (peso/(altura**2)) + 0.23 * edad - 5.4 - valor_genero

def calcular_calorias_en_reposo(peso:float,altura:float,edad:float,valor_genero:float)->float:
    return (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero

def calcular_calorias_en_actividad(peso: float, altura: float, edad: float, valor_genero: float, valor_actividad: float) -> float:
    tasa_metabolica_basal = (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero
    return tasa_metabolica_basal * valor_actividad



def consumo_calorias_recomendado_para_adelgazar(peso: float, altura: float, edad: float, valor_genero: float) -> str:
    tasa_metabolica_basal = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    rango_inferior = int(tasa_metabolica_basal * 0.8)
    rango_superior = int(tasa_metabolica_basal * 0.85)
    return f"Para adelgazar es recomendado que consumas entre: {rango_inferior} y {rango_superior} calorías al día."