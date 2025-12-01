# 📦 Sistema de Gestión de Inventario con SQLite
## Un sistema completo de gestión de inventario desarrollado en Python con interfaz de consola, que utiliza SQLite como base de datos para almacenar y administrar productos de manera eficiente.

### 🚀 Características
* CRUD completo (Crear, Leer, Actualizar, Eliminar) de productos

* Búsqueda flexible por nombre, categoría o ID

* Estadísticas detalladas del inventario

* Validación de datos en todas las entradas

* Base de datos persistente con SQLite

* Interfaz intuitiva por menú en consola

### 📊 Funcionalidades Principales
1. Agregar Productos
Nombre del producto

Descripción detallada

Cantidad disponible

Precio unitario

Categoría de clasificación

2. Visualización de Inventario
Listado completo de productos

Formato claro y organizado

Información detallada por producto

3. Búsqueda Avanzada
Por nombre (búsqueda parcial)

Por categoría

Por ID único

4. Modificación de Productos
Actualización parcial o total

Mantiene valores anteriores si no se especifican nuevos

Validación de datos numéricos

5. Eliminación Segura
Confirmación antes de eliminar

Verificación de existencia del producto

6. Estadísticas
Valor total del inventario

Producto más caro y más barato

Conteo por categorías

Alertas de stock bajo (<10 unidades)

### 🛠️ Tecnologías Utilizadas
Python 3.x

SQLite3 (incluido en Python)

Sin dependencias externas

### 📁 Estructura de la Base de Datos
La base de datos inventario.db contiene una tabla productos con:

Columna	Tipo	Descripción
id	INTEGER PRIMARY KEY AUTOINCREMENT	Identificador único
nombre	TEXT NOT NULL	Nombre del producto
descripcion	TEXT	Descripción detallada
cantidad	INTEGER NOT NULL	Stock disponible
precio	REAL NOT NULL	Precio unitario
categoria	TEXT	Categoría de clasificación
▶️ Cómo Ejecutar
Clonar o descargar el archivo Gestion de productos con DB TalentoTech.py

Ejecutar el script Python:

bash
python "Gestion de productos con DB TalentoTech.py"
Seguir las instrucciones del menú interactivo

### 📋 Requisitos del Sistema
Python 3.x instalado

Permisos de escritura en el directorio de ejecución

Terminal/consola compatible

### 🎯 Beneficios
Portable: Solo requiere Python, sin instalación adicional

Liviano: Base de datos SQLite sin configuración

Robusto: Validación completa de entradas

Persistente: Los datos se mantienen entre ejecuciones

Educativo: Código claro y bien documentado


### 📝 Notas
La base de datos se crea automáticamente en la primera ejecución

Todos los precios se manejan en la misma moneda

El programa es autocontenido y no modifica archivos del sistema

### 👨‍💻 Desarrollo
Este proyecto fue desarrollado como parte del programa Talento Tech, demostrando:

Manejo de bases de datos con SQLite

Programación estructurada en Python

Validación y manejo de errores

Interfaz de usuario por consola

¡Gestione su inventario de manera eficiente y sin complicaciones!

