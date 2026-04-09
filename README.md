# Predicción de Estrato Socioeconómico – Medellín

Este repositorio contiene el desarrollo, evaluación y despliegue de un modelo de Machine Learning para la predicción del estrato socioeconómico (1–6) en la ciudad de Medellín, a partir de variables físicas, económicas y espaciales asociadas a construcciones.

---

## 1. Planteamiento del problema

El objetivo del proyecto es estimar el estrato socioeconómico de un inmueble utilizando un enfoque de clasificación multiclase supervisada. Este problema presenta complejidad debido a:

- La alta similitud entre clases contiguas (estratos cercanos).
- La presencia de múltiples variables categóricas transformadas en variables dummy.
- El gran volumen de datos (más de un millón de registros).

---

## 2. Variables del modelo

Las variables utilizadas incluyen:

- Área construida (m2)
- Número de pisos  
- Valor por metro cuadrado (Pesos colombianos)
- Identificador del barrio (codificado mediante variables dummy)

La transformación del identificador de barrio generó una alta dimensionalidad (más de 300 variables), lo cual influyó en el comportamiento de los modelos evaluados.

---

## 3. Metodología

El flujo metodológico del proyecto se estructuró de la siguiente manera:

1. Preparación y limpieza de datos  
2. Transformación de variables (codificación y normalización cuando fue necesario)  
3. División del dataset (70% entrenamiento y 30% prueba)  
4. Entrenamiento de múltiples modelos de clasificación  
5. Evaluación mediante métricas de desempeño  
6. Selección del modelo óptimo  
7. Despliegue en aplicación web  

---

## 4. Modelos evaluados

### 4.1 K-Nearest Neighbors (KNN)

- Requiere normalización de variables  
- Sensible a la escala de los datos  
- Presentó dispersión en los errores y menor estabilidad  

---

### 4.2 Regresión Logística

- Modelo lineal base para clasificación multiclase  
- Requirió ajuste de hiperparámetros como `C` y `max_iter`  
- Limitado para capturar relaciones no lineales  

---

### 4.3 Red Neuronal (MLPClassifier)

Configuración:

- Una capa oculta de 100 neuronas  
- Función de activación ReLU  
- Tasa de aprendizaje adaptativa  
- `learning_rate_init = 0.01`  
- `momentum = 0.9`  
- `max_iter = 1000`  

Resultados:

- Exactitud aproximada: 0.67  
- Mejor desempeño en estratos intermedios  
- Confusión significativa entre clases contiguas  

---

### 4.4 Árbol de Decisión (Modelo seleccionado)

El modelo final corresponde a un clasificador basado en árboles de decisión.

Hiperparámetros ajustados:

- `max_depth`  
- `min_samples_leaf`  
- `criterion` (gini / entropy)  

Justificación de selección:

- Mejor equilibrio entre métricas de desempeño  
- Capacidad para modelar relaciones no lineales  
- Mayor interpretabilidad frente a otros modelos  

---

## 5. Evaluación del modelo

El modelo fue evaluado mediante:

- Matriz de confusión  
- Precisión (Precision)  
- Sensibilidad (Recall)  
- F1-score  
- Exactitud (Accuracy)  

Hallazgos principales:

- Mejor desempeño en estratos intermedios  
- Confusión frecuente entre clases cercanas  
- Comportamiento consistente con la estructura del problema  

---

## 6. Análisis exploratorio mediante clustering

Se aplicaron técnicas de clustering (K-Means) con el fin de analizar la estructura interna de los datos:

- Método del codo (inercia)  
- Coeficiente de silueta  

Debido al tamaño del dataset, el coeficiente de silueta se estimó mediante muestreo aleatorio, considerando la complejidad computacional cuadrática del cálculo.

---

## 7. Despliegue

El modelo fue integrado en una aplicación web desarrollada con Streamlit, permitiendo la predicción del estrato a partir de variables de entrada.

Funcionalidades:

- Ingreso de variables del inmueble  
- Predicción automática del estrato  
- Interfaz interactiva  

