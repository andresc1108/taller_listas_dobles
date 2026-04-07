# Monitoreo de Signos Vitales - Listas Dobles 

Este es un proyecto que hice para aplicar el concepto de **Listas Doblemente Enlazadas** en un caso de uso real. Elegí el monitoreo de signos vitales porque es una forma clara de ver cómo los punteros `next` y `prev` nos permiten movernos por el historial de un paciente de forma eficiente.

La idea es que cada registro médico sea un nodo que se conecta con el anterior y el siguiente, permitiendo navegar cronológicamente por la evolución del paciente.

## Lo que hace el programa
El sistema permite gestionar los signos vitales (Pulso, Oxigenación y Presión Arterial) con las siguientes funciones:
* **Agregar registros:** Se pueden meter datos al inicio, al final o en una posición específica de la lista.
* **Eliminación dinámica:** Si un dato quedó mal registrado, se puede borrar por índice y el programa se encarga de re-enganchar los punteros automáticamente para no romper la cadena.
* **Recorrido Bidireccional:** Se puede ver el historial en orden normal (del más viejo al más nuevo) o en orden inverso (del más reciente atrás), usando puramente la lógica de las listas dobles.
* **Dashboard visual:** Usé Streamlit para que no fuera solo consola y se viera más como una app de verdad con iconos SVG y estados de alerta.

## Estructura del código
Dividí el código en varios archivos para que sea más fácil de leer y mantener:
* `vital_sign.py`: El modelo de los datos y la lógica de alertas.
* `node.py`: La estructura básica del nodo con sus dos punteros.
* `vital_history.py`: Aquí está todo el "cerebro" de la lista doble (los métodos de insertar y borrar).
* `app.py`: Toda la interfaz visual y la interacción con el usuario.

## Cómo correrlo
1. Tener instalado Python.
2. Instalar la librería para la interfaz:
   ```bash
   pip install streamlit

## Correr la app con: 
    streamlit run app.py


    Andrés David Criollo Rosero. 