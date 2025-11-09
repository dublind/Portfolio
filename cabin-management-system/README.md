# Sistema de Gestión de Cabañas Rupert

Sistema completo de gestión de reservas para cabañas, implementado en Python con base de datos MySQL.

## Características

### Funcionalidades para Clientes
- Registro de nuevos clientes con validaciones completas
- Inicio de sesión seguro
- Gestión de perfil personal
- Búsqueda de cabañas disponibles por fecha y capacidad
- Creación de reservas con cálculo automático de precios
- Procesamiento de pagos con múltiples métodos
- Visualización de historial de reservas
- Cancelación de reservas

### Funcionalidades para Colaboradores
- Inicio de sesión seguro
- Gestión completa de reservas (crear, modificar, cancelar)
- Gestión de estados de cabañas (Disponible, Ocupada, Mantenimiento, Limpieza)
- Creación de reservas presenciales
- Procesamiento de pagos
- Generación y consulta de boletas
- Reportes del sistema

## Requisitos del Sistema

### Software Necesario
- Python 3.7 o superior
- MySQL 5.7 o superior
- pip (gestor de paquetes de Python)

### Dependencias de Python
```bash
pip install pymysql
```

## Configuración de Base de Datos

### 1. Crear la base de datos

```sql
CREATE DATABASE rupert CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE rupert;
```

### 2. Crear las tablas

#### Tabla de Clientes
```sql
CREATE TABLE CLIENTES (
    ID_CLIENTE INT AUTO_INCREMENT PRIMARY KEY,
    NOMBRE VARCHAR(100) NOT NULL,
    APELLIDO_P VARCHAR(100) NOT NULL,
    APELLIDO_M VARCHAR(100) NOT NULL,
    RUT VARCHAR(12) UNIQUE NOT NULL,
    EMAIL VARCHAR(150) UNIQUE NOT NULL,
    TELEFONO VARCHAR(15) NOT NULL,
    DIRECCION VARCHAR(200),
    USUARIO VARCHAR(50) UNIQUE NOT NULL,
    CONTRASENA VARCHAR(255) NOT NULL,
    ACTIVO TINYINT(1) DEFAULT 1,
    FECHA_REGISTRO TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Tabla de Colaboradores
```sql
CREATE TABLE COLABORADORES (
    ID_COLABORADOR INT AUTO_INCREMENT PRIMARY KEY,
    NOMBRE VARCHAR(100) NOT NULL,
    APELLIDO_P VARCHAR(100) NOT NULL,
    APELLIDO_M VARCHAR(100) NOT NULL,
    RUT VARCHAR(12) UNIQUE NOT NULL,
    EMAIL VARCHAR(150) UNIQUE NOT NULL,
    TELEFONO VARCHAR(15) NOT NULL,
    USUARIO VARCHAR(50) UNIQUE NOT NULL,
    CONTRASENA VARCHAR(255) NOT NULL,
    ACTIVO TINYINT(1) DEFAULT 1,
    FECHA_REGISTRO TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Tabla de Cabañas
```sql
CREATE TABLE CABANAS (
    ID_CABANA INT PRIMARY KEY,
    NOMBRE VARCHAR(100) NOT NULL,
    CAPACIDAD INT NOT NULL,
    PRECIO_NOCHE DECIMAL(10,2) NOT NULL,
    ESTADO ENUM('DISPONIBLE', 'OCUPADA', 'MANTENIMIENTO', 'LIMPIEZA') DEFAULT 'DISPONIBLE',
    DESCRIPCION TEXT
);
```

#### Tabla de Reservas
```sql
CREATE TABLE RESERVAS (
    ID_RESERVA INT AUTO_INCREMENT PRIMARY KEY,
    ID_CLIENTE INT NOT NULL,
    ID_CABANA INT NOT NULL,
    ID_COLABORADOR INT,
    FECHA_INGRESO DATE NOT NULL,
    FECHA_SALIDA DATE NOT NULL,
    NUM_HUESPEDES INT NOT NULL,
    PRECIO_TOTAL DECIMAL(10,2) NOT NULL,
    ESTADO ENUM('PENDIENTE', 'CONFIRMADA', 'CANCELADA', 'COMPLETADA') DEFAULT 'PENDIENTE',
    FECHA_RESERVA TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ID_CLIENTE) REFERENCES CLIENTES(ID_CLIENTE),
    FOREIGN KEY (ID_CABANA) REFERENCES CABANAS(ID_CABANA),
    FOREIGN KEY (ID_COLABORADOR) REFERENCES COLABORADORES(ID_COLABORADOR)
);
```

#### Tabla de Boletas
```sql
CREATE TABLE BOLETAS (
    ID_BOLETA INT AUTO_INCREMENT PRIMARY KEY,
    ID_RESERVA INT NOT NULL,
    RAZON_SOCIAL VARCHAR(200) NOT NULL,
    METODO_PAGO ENUM('EFECTIVO', 'TARJETA_DEBITO', 'TARJETA_CREDITO', 'TRANSFERENCIA', 'CHEQUE') NOT NULL,
    SUBTOTAL DECIMAL(10,2) NOT NULL,
    IVA DECIMAL(10,2) NOT NULL,
    TOTAL DECIMAL(10,2) NOT NULL,
    FECHA_EMISION TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ID_RESERVA) REFERENCES RESERVAS(ID_RESERVA)
);
```

### 3. Insertar datos de prueba

#### Cabañas
```sql
INSERT INTO CABANAS (ID_CABANA, NOMBRE, CAPACIDAD, PRECIO_NOCHE, ESTADO, DESCRIPCION) VALUES
(1, 'Cabaña Romántica', 2, 50000.00, 'DISPONIBLE', 'Cabaña ideal para parejas'),
(2, 'Cabaña Familiar 1', 4, 80000.00, 'DISPONIBLE', 'Cabaña para familia pequeña'),
(3, 'Cabaña Familiar 2', 6, 120000.00, 'DISPONIBLE', 'Cabaña espaciosa para familia'),
(4, 'Cabaña Premium', 8, 150000.00, 'DISPONIBLE', 'Cabaña de lujo con todas las comodidades'),
(5, 'Cabaña Estándar 1', 4, 80000.00, 'DISPONIBLE', 'Cabaña cómoda y económica'),
(6, 'Cabaña Estándar 2', 4, 80000.00, 'DISPONIBLE', 'Cabaña cómoda y económica'),
(7, 'Cabaña Estándar 3', 4, 80000.00, 'DISPONIBLE', 'Cabaña cómoda y económica'),
(8, 'Cabaña Superior', 6, 120000.00, 'DISPONIBLE', 'Cabaña con vista panorámica');
```

#### Cliente de prueba
```sql
INSERT INTO CLIENTES (NOMBRE, APELLIDO_P, APELLIDO_M, RUT, EMAIL, TELEFONO, DIRECCION, USUARIO, CONTRASENA, ACTIVO)
VALUES ('Juan', 'Pérez', 'González', '12345678-9', 'juan.perez@email.com', '987654321', 'Calle Principal 123', 'jperez', '123456', 1);
```

#### Colaborador de prueba
```sql
INSERT INTO COLABORADORES (NOMBRE, APELLIDO_P, APELLIDO_M, RUT, EMAIL, TELEFONO, USUARIO, CONTRASENA, ACTIVO)
VALUES ('María', 'González', 'Silva', '98765432-1', 'maria.gonzalez@rupert.com', '912345678', 'mgonzalez', 'admin123', 1);
```

## Configuración de Conexión

Edite las credenciales de la base de datos en el archivo `main.py`:

```python
def get_mysql_connection():
    return pymysql.connect(
        host="127.0.0.1",      # Dirección del servidor MySQL
        user="root",            # Usuario de MySQL
        password="tu_password", # Contraseña de MySQL
        database="rupert"       # Nombre de la base de datos
    )
```

## Instalación y Ejecución

### 1. Clonar o descargar el proyecto
```bash
git clone [URL_DEL_REPOSITORIO]
cd cabin-management-system
```

### 2. Instalar dependencias
```bash
pip install pymysql
```

### 3. Configurar la base de datos
- Ejecutar los scripts SQL proporcionados en la sección "Configuración de Base de Datos"
- Actualizar las credenciales de conexión en `main.py`

### 4. Ejecutar el sistema
```bash
python main.py
```

## Uso del Sistema

### Menú Principal

Al iniciar el sistema, verá el menú principal con las siguientes opciones:

```
1 - Acceso como Cliente
2 - Acceso como Colaborador
3 - Registrar nuevo cliente
4 - Salir del sistema
```

### Credenciales de Prueba

**Cliente:**
- Usuario: `jperez`
- Contraseña: `123456`

**Colaborador:**
- Usuario: `mgonzalez`
- Contraseña: `admin123`

## Validaciones Implementadas

### Validación de RUT Chileno
- Formato: 12345678-9
- Verifica dígito verificador según algoritmo oficial

### Validación de Email
- Formato estándar: usuario@dominio.com
- Expresión regular RFC 5322 simplificada

### Validación de Teléfono
- Formato chileno: 9XXXXXXXX (9 dígitos)
- Acepta también formato internacional: 569XXXXXXXX

### Validación de Fechas
- Formato: DD/MM/YYYY
- Verificación de fechas futuras para reservas
- Validación de rangos de fechas coherentes

## Estructura del Código

### Módulos Principales

#### Validaciones y Utilidades
- `validate_rut()`: Validación de RUT chileno
- `validate_email()`: Validación de email
- `validate_phone()`: Validación de teléfono
- `validate_date_format()`: Validación de formato de fecha
- `validate_future_date()`: Verificación de fecha futura
- `calculate_days_difference()`: Cálculo de diferencia entre fechas

#### Funciones de Base de Datos
- `validate_client_credentials()`: Autenticación de clientes
- `validate_collaborator_credentials()`: Autenticación de colaboradores
- `get_client_data()`: Obtener datos del cliente
- `get_collaborator_data()`: Obtener datos del colaborador
- `check_cabin_availability()`: Verificar disponibilidad de cabañas
- `get_cabin_price()`: Obtener precio de cabaña

#### Clases Principales

**Person**
- Gestión de datos personales
- Métodos factory para crear clientes y colaboradores
- Actualización de datos con validaciones

**Cabin**
- Gestión de cabañas
- Control de estados (Disponible, Ocupada, Mantenimiento, Limpieza)
- Consulta de disponibilidad
- Verificación de capacidad

**Reservation**
- Creación de reservas
- Validaciones de fechas y disponibilidad
- Cálculo automático de precios con IVA

**Payment**
- Procesamiento de pagos
- Múltiples métodos de pago
- Generación de boletas
- Registro de transacciones

## Características de Seguridad

- Autenticación de usuarios con máximo de intentos
- Validación exhaustiva de datos de entrada
- Sanitización de consultas SQL (uso de prepared statements)
- Verificación de permisos por rol (Cliente/Colaborador)
- Manejo de excepciones y errores

## Métodos de Pago Soportados

1. Efectivo
2. Tarjeta de Débito
3. Tarjeta de Crédito
4. Transferencia Bancaria
5. Cheque

## Cálculo de Precios

El sistema calcula automáticamente:
- Subtotal = Precio por noche × Número de noches
- IVA = Subtotal × 19%
- Total = Subtotal + IVA

## Mantenimiento y Soporte

### Logs
El sistema muestra mensajes informativos en consola para:
- Autenticaciones exitosas y fallidas
- Errores de base de datos
- Validaciones fallidas
- Operaciones completadas

### Solución de Problemas Comunes

**Error de conexión a MySQL**
- Verificar que MySQL esté ejecutándose
- Comprobar credenciales en `get_mysql_connection()`
- Verificar que la base de datos 'rupert' exista

**Error de módulo pymysql no encontrado**
```bash
pip install pymysql
```

**Error de autenticación**
- Verificar que el usuario exista en la tabla correspondiente
- Comprobar que el campo ACTIVO esté en 1
- Verificar contraseña (sensible a mayúsculas/minúsculas)

## Desarrollo Futuro

Posibles mejoras:
- Encriptación de contraseñas (bcrypt, argon2)
- API REST para integración con frontend
- Sistema de notificaciones por email
- Dashboard con estadísticas
- Integración con pasarelas de pago reales
- Sistema de descuentos y promociones
- Gestión de servicios adicionales
- Calificaciones y comentarios de clientes
- Reportes avanzados con gráficos

## Licencia

Este proyecto es de código abierto y está disponible para uso educativo y comercial.

## Autor

Desarrollado para Cabañas Rupert

## Contacto

Para soporte y consultas, contactar a través del repositorio del proyecto.
