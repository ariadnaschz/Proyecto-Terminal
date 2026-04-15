# Proyecto Terminal: Dinámica de la infección por VIH en los ganglios linfáticos

Este repositorio contiene la implementación computacional utilizada en el proyecto terminal (tesis) titulado: **“Dinámica de la infección por VIH en los ganglios linfáticos: un enfoque de teoría de gráficas”**.

El objetivo principal es simular el modelo propuesto por Simon Mukwembi para estudiar la propagación del VIH en estructuras de tipo grafo y calcular el número $VIH(G)$, definido como el mínimo valor del parámetro de reemplazo $R$ para el cual toda configuración inicial conduce a la curación del sistema.

## Documentación del Proyecto
Para una comprensión profunda de la metodología, el marco teórico y el análisis de resultados, puedes consultar el reporte final de investigación:

* [**Descargar Proyecto Terminal (PDF)**](..\docs\Proyecto-Terminal.pdf) *(Asegúrate de subir el PDF y poner la ruta correcta aquí)*

## Contenido del Repositorio
El código está desarrollado en **Python / SageMath 9.8** e incluye:

* **Simulación del Modelo:** Implementación de las reglas R1, R2 y R3 en pasos de tiempo discretos.
* **Generación de Gráficas:** Familias de gráficas ($P_n, C_n, K_n, W_n, S_n, K_{n,m}, R_{n,m}$).
* **Cálculo Experimental:** Determinación del número $VIH(G)$.
* **Visualización:** Herramientas para observar la dinámica temporal de la infección.
* **Resultados:** Tablas y datos incluidos en el cuerpo del proyecto terminal.

Este repositorio busca ser una herramienta reproducible y abierta para estudiantes e investigadores interesados en dinámica en redes y modelos matemáticos de propagación.

## Créditos y Autoría
* **Institución Academica:** Universidad Autónoma Metropolitana - Unidad Cuajimalpa
* **Autor Principal:** Lizzeth Ariadna Sánchez Solis – Responsable de la investigación académica, desarrollo del algoritmo, análisis de resultados y redacción del proyecto terminal.
* **Asesor de Tesis:** Julian Alberto Fresán Figueroa – Dirección académica, supervisión metodológica y revisión del proyecto.
* **Soporte de DevOps:** Kevin Uriel Dulche Jaime – Colaboró exclusivamente en la verificación de la compilación y la configuración del entorno en GitHub para asegurar que el código sea ejecutable por terceros.


