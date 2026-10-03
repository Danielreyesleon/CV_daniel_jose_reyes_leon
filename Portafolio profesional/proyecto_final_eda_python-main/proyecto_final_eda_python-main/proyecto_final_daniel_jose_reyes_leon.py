import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Global DataFrame
# DataFrame global
df = None

# List for new records
# Lista para nuevos registros
registros_nuevos = []

def cargar_csv():
    # Load CSV file using file dialog
    # Cargar archivo CSV usando ventana de seleccion
    global df
    Tk().withdraw()
    archivo = askopenfilename(title="Seleccione el archivo CSV",
                              filetypes=[("Archivo CSV", "*.csv")])
    if archivo == "":
        print("No selecciono ningun archivo.")
        return
    try:
        df = pd.read_csv(archivo)
        print("Archivo cargado correctamente.")
        print("El conjunto de datos tiene", df.shape[0], "filas y", df.shape[1], "columnas.")
    except Exception as e:
        print("Ocurrio un error al cargar el archivo:", e)
        
        
def info_general():
    # Show DataFrame info
    # Mostrar informacion general del DataFrame
    if df is None:
        print("Primero debe cargar el archivo CSV (opcion 1).")
        return
    print(df.info())
    print("\nNombre de las columnas:")
    print(list(df.columns))
    
    
def mostrar_filas():
    # Show first and last rows
    # Mostrar primeras y ultimas filas
    if df is None:
        print("Primero debe cargar el archivo CSV (opcion 1).")
        return
    print("\nPrimeras 5 filas:")
    print(df.head())
    print("\nUltimas 5 filas:")
    print(df.tail())
    
    
def tipos_datos():
    # Show column data types
    # Mostrar tipos de datos
    if df is None:
        print("Primero debe cargar el archivo CSV (opcion 1).")
        return
    print(df.dtypes)
    
    
def valores_nulos():
    # Show and optionally fill null values
    # Mostrar y rellenar valores nulos
    if df is None:
        print("Primero debe cargar el archivo CSV (opcion 1).")
        return
    
    print(df.isnull().sum())
    resp = input("Desea rellenar los valores nulos numericos con la media? (s/n): ").lower()
    
    if resp == "s":
        if "precio_unitario" in df.columns:
            media = df["precio_unitario"].mean()
            df["precio_unitario"].fillna(media, inplace=True)
            print("precio_unitario rellenado con la media:", round(media, 2))
        if "region" in df.columns:
            df["region"].fillna("Sin dato", inplace=True)
            print("region rellenada con 'Sin dato'.")
            
            
def datos_duplicados():
    # Detect and remove duplicates
    # Detectar y eliminar duplicados
    if df is None:
        print("Primero debe cargar el archivo CSV (opcion 1).")
        return
    
    cantidad = df.duplicated().sum()
    print("Cantidad de filas duplicadas:", cantidad)
    
    if cantidad > 0:
        resp = input("Desea eliminar los duplicados? (s/n): ").lower()
        if resp == "s":
            df.drop_duplicates(inplace=True)
            print("Duplicados eliminados. Nuevas dimensiones:", df.shape)
            
            
def estadisticas():
    # Show descriptive statistics
    # Mostrar estadisticas descriptivas
    if df is None:
        print("Primero debe cargar el archivo CSV (opcion 1).")
        return
    
    print("\nEstadisticas descriptivas (numericas):")
    print(df.describe())
    print("\nEstadisticas descriptivas (texto):")
    print(df.describe(include="object"))
    
    
def filtros():
    # Filter dataset by category, region, seller or quantity
    # Filtrar dataset por categoria, region, vendedor o cantidad
    if df is None:
        print("Primero debe cargar el archivo CSV (opcion 1).")
        return
    
    print("\na. Filtrar por categoria")
    print("b. Filtrar por region")
    print("c. Filtrar por vendedor")
    print("d. Ventas con cantidad mayor a un numero")
    
    sub = input("Elija una opcion (a/b/c/d): ").lower()
    
    if sub == "a":
        valor = input("Categoria: ")
        print(df[df["categoria"].str.lower() == valor.lower()])
    elif sub == "b":
        valor = input("Region: ")
        print(df[df["region"] == valor])
    elif sub == "c":
        valor = input("Vendedor: ")
        print(df[df["vendedor"].str.lower() == valor.lower()])
    elif sub == "d":
        try:
            valor = int(input("Cantidad minima: "))
            print(df[df["cantidad"] > valor])
        except:
            print("Debe ingresar un numero valido.")
    else:
        print("Opcion no valida.")
        
        
def agrupaciones():
    # Group dataset by different columns
    # Agrupar dataset por diferentes columnas
    if df is None:
        print("Primero debe cargar el archivo CSV (opcion 1).")
        return
    
    print("\na. Total vendido por categoria")
    print("b. Promedio de precio_unitario por categoria")
    print("c. Total de ventas por region")
    print("d. Total de ventas por vendedor")
    
    sub = input("Elija una opcion (a/b/c/d): ").lower()
    
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
        
        
def graficos():
    # Generate charts using seaborn
    # Generar graficos usando seaborn
    if df is None:
        print("Primero debe cargar el archivo CSV (opcion 1).")
        return
    
    sns.set(style="whitegrid")
    
    print("\na. Barras")
    print("b. Pastel")
    print("c. Histograma")
    print("d. Dispersion")
    
    sub = input("Elija una opcion (a/b/c/d): ").lower()
    
    if sub == "a":
        datos = df.groupby("categoria")["cantidad"].sum().sort_values()
        sns.barplot(x=datos.index, y=datos.values, palette="viridis")
        plt.xticks(rotation=45)
        plt.title("Cantidad total vendida por categoria")
        plt.show()
    
    elif sub == "b":
        df["metodo_pago"].value_counts().plot(kind="pie",
                                              autopct="%1.1f%%",
                                              colors=sns.color_palette("pastel"))
        plt.title("Ventas por metodo de pago")
        plt.show()
    
    elif sub == "c":
        sns.histplot(df["precio_unitario"], bins=20, kde=True, color="orange")
        plt.title("Distribucion de precio_unitario")
        plt.show()
    
    elif sub == "d":
        sns.scatterplot(x=df["cantidad"], y=df["precio_unitario"], color="red")
        plt.title("Cantidad vs Precio unitario")
        plt.show()
    
    else:
        print("Opcion no valida.")
        
        
def analisis_adicional():
    # Additional analysis: total sold, top sales, negative values
    # Analisis adicional: total vendido, top ventas, valores negativos
    if df is None:
        print("Primero debe cargar el archivo CSV (opcion 1).")
        return
    
    df["total_vendido"] = df["cantidad"] * df["precio_unitario"]
    print("Se creo la columna total_vendido.")
    print("\nTop 5 ventas con mayor total_vendido:")
    print(df.sort_values("total_vendido", ascending=False).head())
    print("\nCantidad de ventas negativas:", (df["cantidad"] < 0).sum())
    print("\nCategorias unicas encontradas:")
    print(df["categoria"].unique())
    
    
def submenu_ingreso():
    # Submenu for manual data entry
    # Submenu para ingreso manual de datos
    global df
    
    while True:
        print("\n--- SUBMENU: INGRESO DE DATOS ---")
        print("1. Ingresar un nuevo registro")
        print("2. Mostrar registros ingresados")
        print("3. Guardar los nuevos datos en el DataFrame")
        print("4. Regresar al menu principal")
        
        sub = input("Elija una opcion: ")
        
        if sub == "1":
            try:
                nuevo = {
                    "id_venta": int(input("id_venta: ")),
                    "fecha": input("fecha (AAAA-MM-DD): "),
                    "producto": input("producto: "),
                    "categoria": input("categoria: "),
                    "cantidad": int(input("cantidad: ")),
                    "precio_unitario": float(input("precio_unitario: ")),
                    "vendedor": input("vendedor: "),
                    "region": input("region: "),
                    "metodo_pago": input("metodo_pago: "),
                    "cliente_frecuente": input("cliente_frecuente (Si/No): ")
                }
                registros_nuevos.append(nuevo)
                print("Registro agregado correctamente.")
            except:
                print("Error: verifique los datos ingresados.")
        
        elif sub == "2":
            print("\nRegistros ingresados:")
            print(registros_nuevos)
        
        elif sub == "3":
            if df is None:
                print("Primero debe cargar el archivo CSV.")
            elif len(registros_nuevos) == 0:
                print("No hay registros nuevos para guardar.")
            else:
                df_nuevos = pd.DataFrame(registros_nuevos)
                df = pd.concat([df, df_nuevos], ignore_index=True)
                print("Registros agregados al DataFrame principal.")
        
        elif sub == "4":
            print("Regresando al menu principal...")
            break
        
        else:
            print("Opcion no valida.")
            
            
            
def menu():
    # Main program loop
    # Ciclo principal del programa
    while True:
        print("\n<>======= MENU PRINCIPAL ======<>")
        print("1. Cargar archivo CSV")
        print("2. Mostrar informacion del conjunto de datos")
        print("3. Mostrar primeras y ultimas filas")
        print("4. Analizar tipos de datos")
        print("5. Analizar valores nulos")
        print("6. Analizar datos duplicados")
        print("7. Obtener estadisticas descriptivas")
        print("8. Filtrar o consultar datos")
        print("9. Realizar agrupacion y operaciones")
        print("10. Generar representacion grafica")
        print("11. Realizar analisis adicional")
        print("12. Ingresar nuevos datos (Submenu)")
        print("13. Ver resumen del proyecto")
        print("14. Salir")
        op = input("Elija una opcion: ")
        
        
        if op == "1": cargar_csv()
        elif op == "2": info_general()
        elif op == "3": mostrar_filas()
        elif op == "4": tipos_datos()
        elif op == "5": valores_nulos()
        elif op == "6": datos_duplicados()
        elif op == "7": estadisticas()
        elif op == "8": filtros()
        elif op == "9": agrupaciones()
        elif op == "10": graficos()
        elif op == "11": analisis_adicional()
        elif op == "12": submenu_ingreso()
        elif op == "13":
            print("\n===== README RESUMIDO DEL PROYECTO =====")
            print("Proyecto: EDA Tienda de Tecnologia")
            print("Modulo: Manejo de Datos - EDA")
            print("Estructura del CSV utilizado:")
            print("id_venta, fecha, producto, categoria, cantidad,")
            print("precio_unitario, vendedor, region, metodo_pago, cliente_frecuente")
            print("\nPara datos mas exactos consulte el README.md")
        elif op == "14":
            print("Saliendo del programa. Hasta luego.")
            break
        else:
            print("Opcion no valida, por favor elija una opcion del 1 al 14.")
            
            
menu()
