# -*- coding: utf-8 -*-
"""Despliegue predicción de estrato con árbol"""

import numpy as np
import pandas as pd
import streamlit as st
import pickle

# =========================
# CARGAMOS EL MODELO
# =========================
filename = 'modelo_arbol.pkl'

with open(filename, 'rb') as f:
    modelo, variables = pickle.load(f)

# =========================
# PARÁMETRO DE EXACTITUD
# =========================
exactitud_modelo = 0.70

# =========================
# DICCIONARIO DE TIPOS DE CONSTRUCCIÓN
# =========================
tipos_construccion = {
    'AL': 'Almacén',
    'B': 'Bodega',
    'BQ': 'Barraca o quiosco',
    'C': 'Casa',
    'CA': 'Casa apartamento',
    'CD': 'Cuarto o depósito',
    'E': 'Edificio',
    'FI': 'Finca',
    'M': 'Mejora',
    'N': 'Normal',
    'P': 'Propiedad horizontal / Apartamento',
    'PQ': 'Parqueadero',
    'Q': 'Quiosco',
    'TB': 'Teatro o bodega especial',
    'TO': 'Torre',
    'ZC': 'Zona común'
}

opciones_mostradas = [
    f"{sigla} - {descripcion}"
    for sigla, descripcion in tipos_construccion.items()
]

# =========================
# INTERFAZ
# =========================
st.title('Predicción de estrato socioeconómico')
st.write(
    'Ingrese los datos del predio o construcción para estimar el estrato '
    'con el modelo de árbol de decisión.'
)

numero_pis = st.number_input(
    'Número de pisos',
    min_value=1.0,
    max_value=100.0,
    value=1.0,
    step=1.0
)

area_const = st.number_input(
    'Área construida',
    min_value=1.0,
    max_value=100000.0,
    value=50.0,
    step=1.0
)

valor_m2 = st.number_input(
    'Valor por m²',
    min_value=0.0,
    max_value=100000000.0,
    value=1500000.0,
    step=1000.0
)

tipo_const_mostrado = st.selectbox(
    'Tipo de construcción',
    opciones_mostradas
)

# Extraer sigla para el modelo
tipo_const = tipo_const_mostrado.split(' - ')[0]
descripcion_tipo = tipos_construccion[tipo_const]

# =========================
# DATAFRAME DE ENTRADA
# =========================
datos = [[numero_pis, area_const, valor_m2, tipo_const]]

data = pd.DataFrame(
    datos,
    columns=['numero_pis', 'area_const', 'valor_m2', 'tipo_const']
)

# =========================
# PREPARACIÓN DE LOS DATOS
# =========================
data_preparada = data.copy()

data_preparada = pd.get_dummies(
    data_preparada,
    columns=['tipo_const'],
    drop_first=False,
    dtype=int
)

data_preparada = data_preparada.reindex(columns=variables, fill_value=0)

# =========================
# PREDICCIÓN
# =========================
if st.button('Predecir estrato'):
    Y_pred = modelo.predict(data_preparada)

    resultado = pd.DataFrame({
        'numero_pis': [int(numero_pis)],
        'area_const': [area_const],
        'valor_m2': [valor_m2],
        'tipo_const': [tipo_const],
        'descripcion_tipo_const': [descripcion_tipo],
        'Estrato': [int(Y_pred[0])]
    })

    st.header('PREDICCIONES')
    st.dataframe(resultado, use_container_width=True, hide_index=True)
    st.warning(f'El modelo tiene una exactitud de {exactitud_modelo*100:.0f}%')
