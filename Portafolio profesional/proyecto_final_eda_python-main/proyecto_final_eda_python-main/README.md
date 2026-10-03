
1. Descripcion del proyecto
Este proyecto es un sistema interactivo desarrollado en Python para realizar un Analisis Exploratorio de Datos (EDA) sobre un archivo CSV proporcionado por el docente.
El programa permite cargar, explorar, analizar, graficar y modificar un conjunto de datos relacionado con ventas de una tienda de tecnologia.
El objetivo principal es aplicar las herramientas vistas en el modulo de Manejo de Datos, incluyendo:
===============================================================================================
Lectura de archivos CSV
Exploracion de datos
Estadisticas descriptivas
Deteccion de valores nulos
Deteccion de duplicados
Filtros y consultas
Agrupaciones
Graficos con seaborn y matplotlib
Ingreso manual de nuevos registros
*****************************************************************************************

2. Estructura del dataset
El archivo CSV contiene las siguientes columnas:
=============================================================================================
id_venta
fecha
producto
categoria
cantidad
precio_unitario
vendedor
region
metodo_pago
cliente_frecuente
Estas columnas representan informacion de ventas realizadas en una tienda de tecnologia.

**********************************************************************************************

3. Funcionalidades del programa
El programa cuenta con un menu principal interactivo con las siguientes opciones:
==========================================================================================
1. Cargar archivo CSV
Permite seleccionar un archivo CSV desde el explorador de archivos y cargarlo en un DataFrame.
---------------------------------------------------------



2. Mostrar informacion del conjunto de datos
Muestra la estructura del DataFrame, tipos de datos y nombres de columnas.
---------------------------------------------------------



3. Mostrar primeras y ultimas filas
Presenta las primeras 5 y ultimas 5 filas del dataset.
---------------------------------------------------------



4. Analizar tipos de datos
Muestra los tipos de datos de cada columna.
---------------------------------------------------------



5. Analizar valores nulos
Detecta valores nulos y permite rellenarlos con la media o texto.
---------------------------------------------------------



6. Analizar datos duplicados
Detecta filas duplicadas y permite eliminarlas.
---------------------------------------------------------



7. Obtener estadisticas descriptivas
Muestra estadisticas numericas y de texto.
---------------------------------------------------------



8. Filtrar o consultar datos
Permite filtrar por categoria, region, vendedor o cantidad.
---------------------------------------------------------



9. Realizar agrupacion y operaciones
Incluye agrupaciones por categoria, region y vendedor.
---------------------------------------------------------

10. Generar representacion grafica
Genera graficos modernos usando seaborn:
Barras
Pastel
Histograma
Dispersion
------------------------------------------------------------
11. Realizar analisis adicional
Crea la columna total_vendido, muestra top ventas y detecta valores inconsistentes.
-----------------------------------------------------------------------


12. Ingresar nuevos datos
Submenu para agregar registros manualmente y guardarlos en el DataFrame.


---------------------------------------------------------
13. Ver resumen del proyecto
Muestra informacion general del proyecto.



----------------------------------------------------
14. Salir
Finaliza el programa.


-----------------------------------------------------------
4. Librerias utilizadas
El proyecto utiliza las siguientes librerias:
pandas
seaborn
matplotlib
tkinter
Estas librerias permiten realizar analisis de datos, graficos y seleccionar archivos desde una ventana.


********************************************************************************************************************
5. Objetivo del proyecto
El objetivo es demostrar el dominio de las herramientas de analisis de datos vistas en el modulo, aplicando:
Carga de datos
Exploracion
Limpieza
Analisis
Graficacion
Interpretacion
Presentacion de resultados


================================================================================================================
6. Conclusiones generales
El dataset permite analizar ventas por categoria, region y vendedor.
Se detectaron valores nulos y duplicados, los cuales pueden ser corregidos desde el programa.
Los graficos permiten visualizar tendencias importantes como categorias mas vendidas o metodos de pago mas usados.
El analisis adicional ayuda a identificar ventas con mayor total_vendido y posibles inconsistencias.
El programa cumple con todos los requisitos del proyecto final del modulo.



************************************************************************************
7. Notas finales
Este proyecto fue desarrollado con fines academicos para el modulo Manejo de Datos - EDA.
El codigo esta organizado en funciones para mejorar su claridad, mantenimiento y reutilizacion.

====================================================================================================