"""
PROYECTO FINAL - MANEJO DE DATOS (EDA)
Tienda de Tecnología
------------------------------------------------
Script basico de Analisis Exploratorio de Datos (EDA)
usando pandas y matplotlib, con menu interactivo.

Columnas del CSV:
id_venta, fecha, producto, categoria, cantidad,
precio_unitario, vendedor, region, metodo_pago, cliente_frecuente
"""

import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Variable global para guardar el DataFrame cargado
df = None

# Lista para guardar los registros que el usuario ingrese a mano
registros_nuevos = []

opcion = ""

while opcion != "14":

    print("\n===== MENU PRINCIPAL =====")
    print("1. Cargar archivo CSV")
    print("2. Mostrar informacion del conjunto de datos")
    print("3. Mostrar primeras y ultimas filas")
    print("4. Analizar tipos de datos")
    print("5. Analizar valores nulos")
    print("6. Analizar datos duplicados")
    print("7. Obtener estadisticas descriptivas")
    print("8. Filtrar o consultar datos")
    print("9. Realizar agrupaciones y operaciones")
    print("10. Generar representaciones graficas")
    print("11. Realizar analisis adicional")
    print("12. Ingresar nuevos datos (submenu)")
    print("13. Ver Readme del proyecto")
    print("14. Salir")

    opcion = input("Elija una opcion: ")

    # ----------------------------------------------------
    # OPCION 1: CARGAR CSV
    # ----------------------------------------------------
    if opcion == "1":
        print("Se va a abrir una ventana para que seleccione el archivo CSV...")

        # Abrir ventana de seleccion de archivo (como el "Elegir archivo" de Colab)
        Tk().withdraw()
        nombre_archivo = askopenfilename(
            title="Seleccione el archivo CSV",
            filetypes=[("Archivos CSV", "*.csv")]
        )

        if nombre_archivo == "":
            print("No selecciono ningun archivo.")
        else:
            try:
                df = pd.read_csv(nombre_archivo)
                print("Archivo cargado correctamente.")
                print("El conjunto de datos tiene", df.shape[0], "filas y", df.shape[1], "columnas.")
            except FileNotFoundError:
                print("Error: no se encontro el archivo. Verifique el nombre y la ruta.")
            except Exception as error:
                print("Ocurrio un error al cargar el archivo:", error)

    # ----------------------------------------------------
    # OPCION 2: INFORMACION GENERAL
    # ----------------------------------------------------
    elif opcion == "2":
        if df is None:
            print("Primero debe cargar el archivo CSV (opcion 1).")
        else:
            print("\nInformacion general del DataFrame:")
            print(df.info())
            print("\nNombre de las columnas:")
            print(list(df.columns))

    # ----------------------------------------------------
    # OPCION 3: PRIMERAS Y ULTIMAS FILAS
    # ----------------------------------------------------
    elif opcion == "3":
        if df is None:
            print("Primero debe cargar el archivo CSV (opcion 1).")
        else:
            print("\nPrimeras 5 filas:")
            print(df.head())
            print("\nUltimas 5 filas:")
            print(df.tail())

    # ----------------------------------------------------
    # OPCION 4: TIPOS DE DATOS
    # ----------------------------------------------------
    elif opcion == "4":
        if df is None:
            print("Primero debe cargar el archivo CSV (opcion 1).")
        else:
            print("\nTipos de datos de cada columna:")
            print(df.dtypes)

    # ----------------------------------------------------
    # OPCION 5: VALORES NULOS
    # ----------------------------------------------------
    elif opcion == "5":
        if df is None:
            print("Primero debe cargar el archivo CSV (opcion 1).")
        else:
            print("\nCantidad de valores nulos por columna:")
            print(df.isnull().sum())

            respuesta = input("\nDesea rellenar los valores nulos numericos con la media? (s/n): ")
            if respuesta.lower() == "s":
                # Rellenamos solo la columna precio_unitario si tiene nulos
                if "precio_unitario" in df.columns:
                    media_precio = df["precio_unitario"].mean()
                    df["precio_unitario"] = df["precio_unitario"].fillna(media_precio)
                    print("Se rellenaron los valores nulos de precio_unitario con la media:", round(media_precio, 2))
                if "region" in df.columns:
                    df["region"] = df["region"].fillna("Sin dato")
                    print("Se rellenaron los valores nulos de region con 'Sin dato'.")
            else:
                print("No se modificaron los datos.")

    # ----------------------------------------------------
    # OPCION 6: DATOS DUPLICADOS
    # ----------------------------------------------------
    elif opcion == "6":
        if df is None:
            print("Primero debe cargar el archivo CSV (opcion 1).")
        else:
            cantidad_duplicados = df.duplicated().sum()
            print("\nCantidad de filas duplicadas:", cantidad_duplicados)

            if cantidad_duplicados > 0:
                respuesta = input("Desea eliminar los duplicados? (s/n): ")
                if respuesta.lower() == "s":
                    df = df.drop_duplicates()
                    print("Duplicados eliminados. Nuevas dimensiones:", df.shape)
                else:
                    print("No se eliminaron los duplicados.")

    # ----------------------------------------------------
    # OPCION 7: ESTADISTICAS DESCRIPTIVAS
    # ----------------------------------------------------
    elif opcion == "7":
        if df is None:
            print("Primero debe cargar el archivo CSV (opcion 1).")
        else:
            print("\nEstadisticas descriptivas (columnas numericas):")
            print(df.describe())
            print("\nEstadisticas descriptivas (columnas de texto):")
            print(df.describe(include="object"))

    # ----------------------------------------------------
    # OPCION 8: FILTRAR O CONSULTAR DATOS
    # ----------------------------------------------------
    elif opcion == "8":
        if df is None:
            print("Primero debe cargar el archivo CSV (opcion 1).")
        else:
            print("\nOpciones de filtro:")
            print("a. Filtrar por categoria")
            print("b. Filtrar por region")
            print("c. Filtrar por vendedor")
            print("d. Ventas con cantidad mayor a un numero")

            sub = input("Elija una opcion (a/b/c/d): ")

            if sub == "a":
                valor = input("Escriba la categoria a buscar: ")
                resultado = df[df["categoria"].str.lower() == valor.lower()]
                print(resultado)
            elif sub == "b":
                valor = input("Escriba la region a buscar: ")
                resultado = df[df["region"] == valor]
                print(resultado)
            elif sub == "c":
                valor = input("Escriba el nombre del vendedor: ")
                resultado = df[df["vendedor"].str.lower() == valor.lower()]
                print(resultado)
            elif sub == "d":
                valor = input("Escriba la cantidad minima: ")
                try:
                    valor = int(valor)
                    resultado = df[df["cantidad"] > valor]
                    print(resultado)
                except ValueError:
                    print("Debe ingresar un numero valido.")
            else:
                print("Opcion no valida.")

    # ----------------------------------------------------
    # OPCION 9: AGRUPACIONES
    # ----------------------------------------------------
    elif opcion == "9":
        if df is None:
            print("Primero debe cargar el archivo CSV (opcion 1).")
        else:
            

            sub = input("Elija una opcion (a/b/c/d): ")

            if sub == "a":
                print(df.groupby("categoria")["cantidad"].sum())
            elif sub == "b":
                print(df.groupby("categoria")["precio_unitario"].mean())
            elif sub == "c":
                print(df.groupby("region")["cantidad"].sum())
            elif sub == "d":
                print(df.groupby("vendedor")["cantidad"].sum())
            else:
                print("Opcion no valida.")

    # ----------------------------------------------------
    # OPCION 10: GRAFICOS
    # ----------------------------------------------------
    elif opcion == "10":
        if df is None:
            print("Primero debe cargar el archivo CSV (opcion 1).")
        else:
            print("\nTipos de grafico disponibles:")
            print("a. Barras: cantidad total por categoria")
            print("b. Pastel: ventas por metodo de pago")
            print("c. Histograma: distribucion de precio_unitario")
            print("d. Dispersion: cantidad vs precio_unitario")

            sub = input("Elija una opcion (a/b/c/d): ")

            if sub == "a":
                df.groupby("categoria")["cantidad"].sum().plot(kind="bar", color="skyblue")
                plt.title("Cantidad total vendida por categoria")
                plt.xlabel("Categoria")
                plt.ylabel("Cantidad")
                plt.tight_layout()
                plt.show()
            elif sub == "b":
                df["metodo_pago"].value_counts().plot(kind="pie", autopct="%1.1f%%")
                plt.title("Ventas por metodo de pago")
                plt.ylabel("")
                plt.tight_layout()
                plt.show()
            elif sub == "c":
                df["precio_unitario"].plot(kind="hist", bins=20, color="orange")
                plt.title("Distribucion de precio unitario")
                plt.xlabel("Precio unitario")
                plt.tight_layout()
                plt.show()
            elif sub == "d":
                plt.scatter(df["cantidad"], df["precio_unitario"])
                plt.title("Cantidad vs Precio unitario")
                plt.xlabel("Cantidad")
                plt.ylabel("Precio unitario")
                plt.tight_layout()
                plt.show()
            else:
                print("Opcion no valida.")

    # ----------------------------------------------------
    # OPCION 11: ANALISIS ADICIONAL
    # ----------------------------------------------------
    elif opcion == "11":
        if df is None:
            print("Primero debe cargar el archivo CSV (opcion 1).")
        else:
            print("\nAnalisis adicional:")


            # Crear columna de total de venta (cantidad * precio_unitario)
            df["total_venta"] = df["cantidad"] * df["precio_unitario"]
            print("Se creo la columna 'total_venta' (cantidad x precio_unitario).")

            print("\nTop 5 ventas con mayor total_venta:")
            print(df.sort_values("total_venta", ascending=False).head())

            print("\nCantidad de ventas negativas (dato inconsistente) en columna cantidad:")
            print((df["cantidad"] < 0).sum())

            print("\nCategorias unicas encontradas (revisar mayusculas/espacios):")
            print(df["categoria"].unique())

    # ----------------------------------------------------
    # OPCION 12: SUBMENU - INGRESO DE DATOS
    # ----------------------------------------------------
    elif opcion == "12":
        # (submenu de ingreso de datos, no se toca)
        subopcion = ""
        while subopcion != "4":
            print("\n--- SUBMENU: INGRESO DE DATOS ---")
            print("1. Ingresar un nuevo registro")
            print("2. Mostrar registros ingresados")
            print("3. Guardar los nuevos datos en el DataFrame")
            print("4. Regresar al menu principal")

            subopcion = input("Elija una opcion: ")

            if subopcion == "1":
                try:
                    nuevo_id = int(input("id_venta: "))
                    nueva_fecha = input("fecha (AAAA-MM-DD): ")
                    nuevo_producto = input("producto: ")
                    nueva_categoria = input("categoria: ")
                    nueva_cantidad = int(input("cantidad: "))
                    nuevo_precio = float(input("precio_unitario: "))
                    nuevo_vendedor = input("vendedor: ")
                    nueva_region = input("region: ")
                    nuevo_metodo_pago = input("metodo_pago: ")
                    nuevo_cliente_frec = input("cliente_frecuente (Si/No): ")

                    registro = {
                        "id_venta": nuevo_id,
                        "fecha": nueva_fecha,
                        "producto": nuevo_producto,
                        "categoria": nueva_categoria,
                        "cantidad": nueva_cantidad,
                        "precio_unitario": nuevo_precio,
                        "vendedor": nuevo_vendedor,
                        "region": nueva_region,
                        "metodo_pago": nuevo_metodo_pago,
                        "cliente_frecuente": nuevo_cliente_frec
                    }

                    registros_nuevos.append(registro)
                    print("Registro agregado correctamente.")

                except ValueError:
                    print("Error: verifique que cantidad, precio y id sean numeros validos.")

            elif subopcion == "2":
                if len(registros_nuevos) == 0:
                    print("Aun no ha ingresado registros nuevos.")
                else:
                    print("\nRegistros ingresados en esta sesion:")
                    for i in range(len(registros_nuevos)):
                        print(i + 1, "->", registros_nuevos[i])

            elif subopcion == "3":
                if df is None:
                    print("Primero debe cargar el archivo CSV (opcion 1 del menu principal).")
                elif len(registros_nuevos) == 0:
                    print("No hay registros nuevos para guardar.")
                else:
                    df_nuevos = pd.DataFrame(registros_nuevos)
                    df = pd.concat([df, df_nuevos], ignore_index=True)
                    print("Registros agregados al DataFrame principal.")
                    print("Nuevas dimensiones del DataFrame:", df.shape)

            elif subopcion == "4":
                print("Regresando al menu principal...")

            else:
                print("Opcion no valida, intente de nuevo.")

    # ----------------------------------------------------
    # OPCION 13: README DEL PROYECTO
    # ----------------------------------------------------
    elif opcion == "13":
        print("\n===== README DEL PROYECTO =====")
        print("Proyecto: EDA Tienda de Tecnologia")
        print("Modulo: Manejo de Datos - EDA")
        print("Estructura del CSV utilizado:")
        print("id_venta, fecha, producto, categoria, cantidad,")
        print("precio_unitario, vendedor, region, metodo_pago, cliente_frecuente")
        print("\nEste programa permite cargar el CSV, explorar la estructura,")
        print("revisar nulos y duplicados, calcular estadisticas, filtrar,")
        print("agrupar, graficar y agregar nuevos registros manualmente.")

    # ----------------------------------------------------
    # OPCION 14: SALIR
    # ----------------------------------------------------
    elif opcion == "14":
        print("Saliendo del programa. Hasta luego.")

    else:
        print("Opcion no valida, por favor elija una opcion del 1 al 14.")