import sqlite3

# Crea la base de datos
def crear_base_datos():
    """Crea la base de datos y la tabla si no existen"""
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
    ''')
    
    conexion.commit()
    conexion.close()
    print(" Base de datos 'inventario.db' inicializada")
    
# Muestra el menú
def mostrar_menu():
    print("\n" + "="*60)
    print("           SISTEMA DE GESTIÓN DE INVENTARIO")
    print("="*60)
    print("1. Agregar producto")
    print("2. Mostrar todos los productos")
    print("3. Buscar producto")
    print("4. Modificar producto")
    print("5. Eliminar producto")
    print("6. Estadísticas del inventario")
    print("7. Salir")
    print("="*60)

def agregar_producto():
    print("\n--- AGREGAR PRODUCTO ---")
    
    nombre = input("Ingrese el nombre del producto: ").strip()
    if not nombre:
        print(" El nombre no puede estar vacío")
        return
    
    descripcion = input("Ingrese la descripción: ").strip()
    if not descripcion:
        descripcion = "Sin descripción"
    
    categoria = input("Ingrese la categoría: ").strip()
    if not categoria:
        categoria = "Sin categoría"
    
    try:
        cantidad = int(input("Ingrese la cantidad disponible: "))
        if cantidad < 0:
            print(" La cantidad no puede ser negativa")
            return
    except ValueError:
        print(" La cantidad debe ser un número entero")
        return
    
    try:
        precio = float(input("Ingrese el precio: "))
        if precio < 0:
            print(" El precio no puede ser negativo")
            return
    except ValueError:
        print(" El precio debe ser un número válido")
        return
    
    # Insertar en la base de datos
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    
    try:
        cursor.execute('''
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)
        ''', (nombre, descripcion, cantidad, precio, categoria))
        
        conexion.commit()
        producto_id = cursor.lastrowid
        print(f" Producto '{nombre}' agregado exitosamente! (ID: {producto_id})")
        
    except sqlite3.Error as e:
        print(f" Error al agregar producto: {e}")
    finally:
        conexion.close()

def mostrar_productos():
    print("\n--- LISTA DE PRODUCTOS ---")
    
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    
    try:
        cursor.execute('SELECT * FROM productos')
        productos = cursor.fetchall()
        
        if not productos:
            print("No hay productos registrados")
            return
        
        for producto in productos:
            id_prod, nombre, descripcion, cantidad, precio, categoria = producto
            print(f"ID: {id_prod}")
            print(f"  Nombre: {nombre}")
            print(f"  Descripción: {descripcion}")
            print(f"  Cantidad: {cantidad}")
            print(f"  Precio: ${precio:.2f}")
            print(f"  Categoría: {categoria}")
            print("-" * 40)
            
    except sqlite3.Error as e:
        print(f" Error al mostrar productos: {e}")
    finally:
        conexion.close()

def buscar_producto():
    print("\n--- BUSCAR PRODUCTO ---")
    
    criterio = input("Buscar por (1) Nombre, (2) Categoría, (3) ID: ").strip()
    
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    
    try:
        if criterio == "1":
            nombre_buscar = input("Ingrese el nombre a buscar: ").strip()
            cursor.execute('SELECT * FROM productos WHERE nombre LIKE ?', (f'%{nombre_buscar}%',))
            
        elif criterio == "2":
            categoria_buscar = input("Ingrese la categoría a buscar: ").strip()
            cursor.execute('SELECT * FROM productos WHERE categoria LIKE ?', (f'%{categoria_buscar}%',))
            
        elif criterio == "3":
            try:
                id_buscar = int(input("Ingrese el ID a buscar: "))
                cursor.execute('SELECT * FROM productos WHERE id = ?', (id_buscar,))
            except ValueError:
                print(" El ID debe ser un número entero")
                return
        else:
            print(" Opción inválida")
            return
        
        productos = cursor.fetchall()
        
        if productos:
            print(f"\n Se encontraron {len(productos)} producto(s):")  
            for producto in productos:
                id_prod, nombre, cantidad, precio, categoria = producto 
                print(f"ID: {id_prod} | {nombre} | {categoria} | Cant: {cantidad} | Precio: ${precio:.2f}")
        else:
            print(" No se encontraron productos")
            
    except sqlite3.Error as e:
        print(f" Error en la búsqueda: {e}")
    finally:
        conexion.close()

def modificar_producto():
    print("\n--- MODIFICAR PRODUCTO ---")
    
    mostrar_productos()
    
    try:
        id_modificar = int(input("\nIngrese el ID del producto a modificar: "))
    except ValueError:
        print(" El ID debe ser un número entero")
        return
    
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    
    try:
        # Verificar si el producto existe
        cursor.execute('SELECT * FROM productos WHERE id = ?', (id_modificar,))
        producto = cursor.fetchone()
        
        if not producto:
            print(" No existe un producto con ese ID")
            return
        
        id_prod, nombre_actual, desc_actual, cant_actual, precio_actual, cat_actual = producto
        
        print(f"\nProducto seleccionado:")
        print(f"Nombre actual: {nombre_actual}")
        print(f"Descripción actual: {desc_actual}")
        print(f"Cantidad actual: {cant_actual}")
        print(f"Precio actual: ${precio_actual:.2f}")
        print(f"Categoría actual: {cat_actual}")
        
        print("\nIngrese los nuevos datos (deje vacío para mantener el actual):")
        
        # Solicitar nuevos datos
        nuevo_nombre = input(f"Nuevo nombre [{nombre_actual}]: ").strip()
        nueva_descripcion = input(f"Nueva descripción [{desc_actual}]: ").strip()
        nueva_categoria = input(f"Nueva categoría [{cat_actual}]: ").strip()
        
        nueva_cantidad = input(f"Nueva cantidad [{cant_actual}]: ").strip()
        nuevo_precio = input(f"Nuevo precio [${precio_actual:.2f}]: ").strip()
        
        # Actualizar en la base de datos
        nombre_final = nuevo_nombre if nuevo_nombre else nombre_actual
        desc_final = nueva_descripcion if nueva_descripcion else desc_actual
        categoria_final = nueva_categoria if nueva_categoria else cat_actual
        
        try:
            cantidad_final = int(nueva_cantidad) if nueva_cantidad else cant_actual
            if cantidad_final < 0:
                print(" La cantidad no puede ser negativa")
                return
        except ValueError:
            print(" Cantidad inválida. Se mantiene la cantidad actual.")
            cantidad_final = cant_actual
        
        try:
            precio_final = float(nuevo_precio) if nuevo_precio else precio_actual
            if precio_final < 0:
                print(" El precio no puede ser negativo")
                return
        except ValueError:
            print(" Precio inválido. Se mantiene el precio actual.")
            precio_final = precio_actual
        
        cursor.execute('''
            UPDATE productos 
            SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
            WHERE id = ?
        ''', (nombre_final, desc_final, cantidad_final, precio_final, categoria_final, id_modificar))
        
        conexion.commit()
        print(" Producto modificado exitosamente!")
        
    except sqlite3.Error as e:
        print(f" Error al modificar producto: {e}")
    finally:
        conexion.close()

def eliminar_producto():
    print("\n--- ELIMINAR PRODUCTO ---")
    
    mostrar_productos()
    
    try:
        id_eliminar = int(input("\nIngrese el ID del producto a eliminar: "))
    except ValueError:
        print(" El ID debe ser un número entero")
        return
    
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    
    try:
        # Verificar si el producto existe
        cursor.execute('SELECT nombre FROM productos WHERE id = ?', (id_eliminar,))
        producto = cursor.fetchone()
        
        if not producto:
            print(" No existe un producto con ese ID")
            return
        
        # Confirmar eliminación
        confirmar = input(f"¿Está seguro de eliminar el producto '{producto[0]}'? (s/n): ").strip().lower()
        
        if confirmar == 's':
            cursor.execute('DELETE FROM productos WHERE id = ?', (id_eliminar,))
            conexion.commit()
            print(" Producto eliminado exitosamente!")
        else:
            print(" Eliminación cancelada")
            
    except sqlite3.Error as e:
        print(f" Error al eliminar producto: {e}")
    finally:
        conexion.close()

def mostrar_estadisticas():
    print("\n--- ESTADÍSTICAS DEL INVENTARIO ---")
    
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    
    try:
        # Total de productos
        cursor.execute('SELECT COUNT(*) FROM productos')
        total_productos = cursor.fetchone()[0]
        
        if total_productos == 0:
            print("No hay productos registrados")
            return
        
        # Valor total del inventario
        cursor.execute('SELECT SUM(cantidad * precio) FROM productos')
        valor_inventario = cursor.fetchone()[0] or 0
        
        # Producto más caro
        cursor.execute('SELECT nombre, precio FROM productos ORDER BY precio DESC LIMIT 1')
        producto_caro = cursor.fetchone()
        
        # Producto más barato
        cursor.execute('SELECT nombre, precio FROM productos ORDER BY precio ASC LIMIT 1')
        producto_barato = cursor.fetchone()
        
        # Productos por categoría
        cursor.execute('SELECT categoria, COUNT(*) FROM productos GROUP BY categoria')
        categorias = cursor.fetchall()
        
        # Productos con stock bajo (menos de 10 unidades)
        cursor.execute('SELECT nombre, cantidad FROM productos WHERE cantidad < 10') 
        stock_bajo = cursor.fetchall()
        
        print(f" Total de productos: {total_productos}")
        print(f" Valor total del inventario: ${valor_inventario:.2f}")
        print(f" Producto más caro: {producto_caro[0]} - ${producto_caro[1]:.2f}")
        print(f" Producto más barato: {producto_barato[0]} - ${producto_barato[1]:.2f}")
        print(f"  Productos con stock bajo (<10): {stock_bajo}")
        
        
        print("\n Productos por categoría:")
        for categoria, cantidad in categorias:
            print(f"   {categoria}: {cantidad} producto(s)")
           
            
    except sqlite3.Error as e:
        print(f" Error al calcular estadísticas: {e}")
    finally:
        conexion.close()

def main():
    # Crear la base de datos al iniciar
    crear_base_datos()
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-7): ").strip()
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            modificar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            mostrar_estadisticas()
        elif opcion == "7":
            print("\n¡Gracias por usar el sistema de inventario! ")
            break
        else:
            print(" Opción inválida. Por favor, seleccione 1-7")
        
        input("\nPresione Enter para continuar...")

# Ejecutar el sistema
if __name__ == "__main__":
    main()
