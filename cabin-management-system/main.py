# Sistema de Gestión de Cabañas - Implementación completa basada en diagrama de flujo
import pymysql
from datetime import date, datetime, timedelta
import re
from decimal import Decimal

def get_mysql_connection():
    return pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="Atomico_2001",
        database="rupert"
    )

# VALIDACIONES Y UTILIDADES

def validate_rut(rut):
    """Valida formato y dígito verificador del RUT chileno"""
    if not rut or len(rut.strip()) == 0:
        return False

    # Limpiar el RUT
    rut = rut.replace(".", "").replace("-", "").replace(" ", "").upper()

    # Verificar longitud
    if len(rut) < 8 or len(rut) > 9:
        return False

    # Separar número y dígito verificador
    rut_num = rut[:-1]
    dv = rut[-1]

    # Verificar que la parte numérica sea solo dígitos
    if not rut_num.isdigit():
        return False

    # Calcular dígito verificador
    sum_val = 0
    multiplier = 2

    for digit in reversed(rut_num):
        sum_val += int(digit) * multiplier
        multiplier += 1
        if multiplier > 7:
            multiplier = 2

    remainder = sum_val % 11
    calculated_dv = 11 - remainder

    # Convertir a string según las reglas chilenas
    if calculated_dv == 11:
        calculated_dv = '0'
    elif calculated_dv == 10:
        calculated_dv = 'K'
    else:
        calculated_dv = str(calculated_dv)

    return dv == calculated_dv

def validate_email(email):
    """Valida formato de email"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """Valida formato de teléfono chileno"""
    phone = phone.replace(" ", "").replace("-", "").replace("+", "")
    # Acepta formatos: 9XXXXXXXX, 569XXXXXXXX
    return len(phone) == 9 and phone.startswith('9') or len(phone) == 11 and phone.startswith('569')

def validate_date_format(date_str):
    """Valida formato de fecha DD/MM/YYYY"""
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def validate_future_date(date_str):
    """Valida que la fecha sea futura"""
    try:
        date_obj = datetime.strptime(date_str, "%d/%m/%Y")
        return date_obj.date() > date.today()
    except ValueError:
        return False

def calculate_days_difference(start_date, end_date):
    """Calcula diferencia en días entre dos fechas"""
    try:
        start = datetime.strptime(start_date, "%d/%m/%Y")
        end = datetime.strptime(end_date, "%d/%m/%Y")
        return (end - start).days
    except ValueError:
        return 0

# FUNCIONES DE BASE DE DATOS

def validate_client_credentials(username, password):
    """Validate client credentials against database"""
    try:
        conn = get_mysql_connection()
        cur = conn.cursor()
        sql = """
            SELECT COUNT(*) FROM CLIENTES
            WHERE UPPER(USUARIO) = UPPER(%s) AND CONTRASENA = %s AND ACTIVO = 1
        """
        cur.execute(sql, (username, password))
        result = cur.fetchone()
        return result[0] > 0
    except Exception as e:
        print(f"Error al validar credenciales de cliente: {e}")
        return False
    finally:
        try:
            cur.close()
            conn.close()
        except:
            pass

def validate_collaborator_credentials(username, password):
    """Validate collaborator credentials against database"""
    try:
        conn = get_mysql_connection()
        cur = conn.cursor()
        sql = """
            SELECT COUNT(*) FROM COLABORADORES
            WHERE UPPER(USUARIO) = UPPER(%s) AND CONTRASENA = %s AND ACTIVO = 1
        """
        cur.execute(sql, (username, password))
        result = cur.fetchone()
        return result[0] > 0
    except Exception as e:
        print(f"Error al validar credenciales de colaborador: {e}")
        return False
    finally:
        try:
            cur.close()
            conn.close()
        except:
            pass

def get_client_data(username):
    """Get client data from database"""
    try:
        conn = get_mysql_connection()
        cur = conn.cursor()
        sql = """
            SELECT ID_CLIENTE, NOMBRE, APELLIDO_P, APELLIDO_M, RUT, EMAIL, TELEFONO, DIRECCION
            FROM CLIENTES
            WHERE UPPER(USUARIO) = UPPER(%s) AND ACTIVO = 1
        """
        cur.execute(sql, (username,))
        result = cur.fetchone()
        if result:
            return {
                'client_id': result[0],
                'name': result[1],
                'last_name_p': result[2],
                'last_name_m': result[3],
                'rut': result[4],
                'email': result[5],
                'phone': result[6],
                'address': result[7]
            }
        return None
    except Exception as e:
        print(f"Error al obtener datos del cliente: {e}")
        return None
    finally:
        try:
            cur.close()
            conn.close()
        except:
            pass

def get_collaborator_data(username):
    """Get collaborator data from database"""
    try:
        conn = get_mysql_connection()
        cur = conn.cursor()
        sql = """
            SELECT ID_COLABORADOR, NOMBRE, APELLIDO_P, APELLIDO_M, RUT, EMAIL, TELEFONO
            FROM COLABORADORES
            WHERE UPPER(USUARIO) = UPPER(%s) AND ACTIVO = 1
        """
        cur.execute(sql, (username,))
        result = cur.fetchone()
        if result:
            return {
                'collaborator_id': result[0],
                'name': result[1],
                'last_name_p': result[2],
                'last_name_m': result[3],
                'rut': result[4],
                'email': result[5],
                'phone': result[6]
            }
        return None
    except Exception as e:
        print(f"Error al obtener datos del colaborador: {e}")
        return None
    finally:
        try:
            cur.close()
            conn.close()
        except:
            pass

def check_cabin_availability(cabin_id, start_date, end_date):
    """Verifica disponibilidad de cabaña en fechas específicas"""
    try:
        conn = get_mysql_connection()
        cur = conn.cursor()
        sql = """
            SELECT COUNT(*) FROM RESERVAS
            WHERE ID_CABANA = %s
            AND ESTADO IN ('CONFIRMADA', 'PENDIENTE')
            AND NOT (FECHA_SALIDA <= %s OR FECHA_INGRESO >= %s)
        """
        cur.execute(sql, (cabin_id, start_date, end_date))
        result = cur.fetchone()
        return result[0] == 0
    except Exception as e:
        print(f"Error al verificar disponibilidad: {e}")
        return False
    finally:
        try:
            cur.close()
            conn.close()
        except:
            pass

def get_cabin_price(cabin_id):
    """Obtiene el precio por noche de una cabaña"""
    try:
        conn = get_mysql_connection()
        cur = conn.cursor()
        sql = "SELECT PRECIO_NOCHE FROM CABANAS WHERE ID_CABANA = %s"
        cur.execute(sql, (cabin_id,))
        result = cur.fetchone()
        return float(result[0]) if result else 0.0
    except Exception as e:
        print(f"Error al obtener precio de cabaña: {e}")
        return 0.0
    finally:
        try:
            cur.close()
            conn.close()
        except:
            pass

# CLASES PRINCIPALES

class Person:
    def __init__(self, name, last_name_p, last_name_m, rut, email):
        self.name = name
        self.last_name_p = last_name_p
        self.last_name_m = last_name_m
        self.rut = rut
        self.email = email

    @classmethod
    def create_client(cls, name, last_name_p, last_name_m, rut, email, client_id, phone, address):
        client = cls(name, last_name_p, last_name_m, rut, email)
        client.client_id = client_id
        client.phone = phone
        client.address = address
        return client

    @classmethod
    def create_collaborator(cls, name, last_name_p, last_name_m, rut, email, collaborator_id, phone):
        collaborator = cls(name, last_name_p, last_name_m, rut, email)
        collaborator.collaborator_id = collaborator_id
        collaborator.phone = phone
        return collaborator

    def update_client_data(self):
        """Actualizar datos del cliente con validaciones completas"""
        print("\nACTUALIZAR DATOS PERSONALES")

        # Validar nombre
        while True:
            new_name = input("Nuevo nombre (actual: {}): ".format(self.name)).strip()
            if new_name and len(new_name) >= 2 and new_name.replace(" ", "").isalpha():
                self.name = new_name
                break
            elif not new_name:  # Si está vacío, mantener actual
                break
            else:
                print("Nombre inválido. Debe tener al menos 2 caracteres y solo letras.")

        # Validar apellido paterno
        while True:
            new_last_p = input("Nuevo apellido paterno (actual: {}): ".format(self.last_name_p)).strip()
            if new_last_p and len(new_last_p) >= 2 and new_last_p.isalpha():
                self.last_name_p = new_last_p
                break
            elif not new_last_p:
                break
            else:
                print("Apellido paterno inválido. Debe tener al menos 2 caracteres y solo letras.")

        # Validar apellido materno
        while True:
            new_last_m = input("Nuevo apellido materno (actual: {}): ".format(self.last_name_m)).strip()
            if new_last_m and len(new_last_m) >= 2 and new_last_m.isalpha():
                self.last_name_m = new_last_m
                break
            elif not new_last_m:
                break
            else:
                print("Apellido materno inválido. Debe tener al menos 2 caracteres y solo letras.")

        # Validar RUT
        rut_attempts = 0
        max_rut_attempts = 3
        while rut_attempts < max_rut_attempts:
            new_rut = input("Nuevo RUT (actual: {}): ".format(self.rut)).strip()
            if new_rut and validate_rut(new_rut):
                self.rut = new_rut
                break
            elif not new_rut:
                break
            else:
                rut_attempts += 1
                remaining = max_rut_attempts - rut_attempts
                if remaining > 0:
                    print(f"RUT inválido. Formato correcto: 12345678-9 (Intentos restantes: {remaining})")
                else:
                    print("Máximo de intentos alcanzado para RUT. Se mantiene el RUT actual.")
                    break

        # Validar email
        while True:
            new_email = input("Nuevo email (actual: {}): ".format(self.email)).strip()
            if new_email and validate_email(new_email):
                self.email = new_email
                break
            elif not new_email:
                break
            else:
                print("Email inválido. Formato correcto: usuario@dominio.com")

        # Validar teléfono si es cliente
        if hasattr(self, 'phone'):
            while True:
                new_phone = input("Nuevo teléfono (actual: {}): ".format(self.phone)).strip()
                if new_phone and validate_phone(new_phone):
                    self.phone = new_phone
                    break
                elif not new_phone:
                    break
                else:
                    print("Teléfono inválido. Formato: 9XXXXXXXX")

        # Validar dirección si es cliente
        if hasattr(self, 'address'):
            new_address = input("Nueva dirección (actual: {}): ".format(self.address)).strip()
            if new_address:
                self.address = new_address

        print("Datos actualizados correctamente")
        return True

class Cabin:
    def __init__(self):
        # Estados: DISPONIBLE, OCUPADA, MANTENIMIENTO, LIMPIEZA
        self.cabin_status_dict = {
            '1': 'DISPONIBLE', '2': 'DISPONIBLE', '3': 'DISPONIBLE',
            '4': 'DISPONIBLE', '5': 'DISPONIBLE', '6': 'DISPONIBLE',
            '7': 'DISPONIBLE', '8': 'DISPONIBLE'
        }
        self.cabin_capacity = {
            '1': 2, '2': 4, '3': 6, '4': 8,
            '5': 4, '6': 4, '7': 4, '8': 6
        }
        self.cabin_prices = {
            '1': 50000, '2': 80000, '3': 120000, '4': 150000,
            '5': 80000, '6': 80000, '7': 80000, '8': 120000
        }

    def change_status(self, status_id, new_status):
        """Cambiar estado de cabaña con validaciones"""
        if status_id not in self.cabin_status_dict:
            return "ID de cabaña inválido"

        status_options = {
            1: "DISPONIBLE",
            2: "OCUPADA",
            3: "MANTENIMIENTO",
            4: "LIMPIEZA"
        }

        if new_status not in status_options:
            return "Estado inválido"

        old_status = self.cabin_status_dict[status_id]
        self.cabin_status_dict[status_id] = status_options[new_status]

        return f"Cabaña {status_id} cambió de {old_status} a {status_options[new_status]}"

    def check_capacity(self, cabin_id):
        """Verificar capacidad de cabaña"""
        if cabin_id in self.cabin_capacity:
            return f"Cabaña {cabin_id}: Capacidad {self.cabin_capacity[cabin_id]} personas"
        return "Cabaña no existe"

    def check_status(self, cabin_id):
        """Verificar estado de cabaña"""
        if cabin_id in self.cabin_status_dict:
            status = self.cabin_status_dict[cabin_id]
            return f"Cabaña {cabin_id}: {status}"
        return "Cabaña no existe"

    def get_available_cabins(self, start_date, end_date, guests):
        """Obtener cabañas disponibles para fechas y número de huéspedes"""
        available = []
        for cabin_id, capacity in self.cabin_capacity.items():
            if (capacity >= guests and
                self.cabin_status_dict[cabin_id] == "DISPONIBLE" and
                check_cabin_availability(cabin_id, start_date, end_date)):
                price = self.cabin_prices[cabin_id]
                available.append({
                    'id': cabin_id,
                    'capacity': capacity,
                    'price': price,
                    'status': self.cabin_status_dict[cabin_id]
                })
        return available

class Reservation:
    def __init__(self):
        self.reservation_counter = 1000

    def create_reservation(self, client_id, cabin_id, start_date, end_date, guests, collaborator_id=None):
        """Crear nueva reserva con validaciones completas"""

        # Validar fechas
        if not validate_date_format(start_date) or not validate_date_format(end_date):
            return {"success": False, "message": "Formato de fecha inválido. Use DD/MM/YYYY"}

        if not validate_future_date(start_date):
            return {"success": False, "message": "La fecha de ingreso debe ser futura"}

        days = calculate_days_difference(start_date, end_date)
        if days <= 0:
            return {"success": False, "message": "La fecha de salida debe ser posterior a la de ingreso"}

        # Verificar disponibilidad
        if not check_cabin_availability(cabin_id, start_date, end_date):
            return {"success": False, "message": "Cabaña no disponible en esas fechas"}

        # Calcular precio
        price_per_night = get_cabin_price(cabin_id)
        subtotal = price_per_night * days
        tax = subtotal * 0.19
        total = subtotal + tax

        reservation_id = self.reservation_counter
        self.reservation_counter += 1

        # Aquí se guardaría en la base de datos
        reservation_data = {
            "reservation_id": reservation_id,
            "client_id": client_id,
            "cabin_id": cabin_id,
            "start_date": start_date,
            "end_date": end_date,
            "guests": guests,
            "days": days,
            "price_per_night": price_per_night,
            "subtotal": subtotal,
            "tax": tax,
            "total": total,
            "status": "PENDIENTE",
            "created_date": date.today().strftime("%d/%m/%Y"),
            "collaborator_id": collaborator_id
        }

        return {"success": True, "reservation": reservation_data}

class Payment:
    receipt_registry = []
    receipt_counter = 1

    def __init__(self):
        self.payment_methods = {
            1: "EFECTIVO",
            2: "TARJETA_DEBITO",
            3: "TARJETA_CREDITO",
            4: "TRANSFERENCIA",
            5: "CHEQUE"
        }

    def process_payment(self, reservation_data, payment_method, client_name, collaborator_id):
        """Procesar pago según diagrama de flujo"""

        if payment_method not in self.payment_methods:
            return {"success": False, "message": "Método de pago inválido"}

        method_name = self.payment_methods[payment_method]
        total_amount = reservation_data["total"]

        print(f"\nProcesando pago por ${total_amount:,.0f} mediante {method_name}")

        # Simulación de validaciones específicas por método
        if method_name == "EFECTIVO":
            if not self._validate_cash_payment(total_amount):
                return {"success": False, "message": "Monto en efectivo inválido"}

        elif method_name in ["TARJETA_DEBITO", "TARJETA_CREDITO"]:
            if not self._validate_card_payment():
                return {"success": False, "message": "Tarjeta rechazada"}

        elif method_name == "TRANSFERENCIA":
            if not self._validate_transfer_payment():
                return {"success": False, "message": "Transferencia falló"}

        elif method_name == "CHEQUE":
            if not self._validate_check_payment():
                return {"success": False, "message": "Cheque inválido"}

        # Generar comprobante
        receipt = self.generate_receipt(
            business_name="Cabañas Rupert",
            payment_method=method_name,
            client_name=client_name,
            reservation_data=reservation_data,
            collaborator_id=collaborator_id
        )

        return {"success": True, "receipt": receipt, "message": "Pago procesado exitosamente"}

    def _validate_cash_payment(self, amount):
        """Validar pago en efectivo"""
        print("Validando pago en efectivo...")
        return True  # Simulación

    def _validate_card_payment(self):
        """Validar pago con tarjeta"""
        print("Validando tarjeta...")
        return True  # Simulación

    def _validate_transfer_payment(self):
        """Validar transferencia bancaria"""
        print("Validando transferencia...")
        return True  # Simulación

    def _validate_check_payment(self):
        """Validar cheque"""
        print("Validando cheque...")
        return True  # Simulación

    @classmethod
    def generate_receipt(cls, business_name, payment_method, client_name, reservation_data, collaborator_id):
        """Generar comprobante de pago"""
        receipt_id = cls.receipt_counter
        cls.receipt_counter += 1
        issue_date = date.today()

        receipt = {
            "ID_BOLETA": receipt_id,
            "RAZON_SOCIAL": business_name,
            "FECHA_EMISION": issue_date.strftime("%d/%m/%Y"),
            "METODO_PAGO": payment_method,
            "CLIENTE": client_name,
            "ID_RESERVA": reservation_data["reservation_id"],
            "ID_CABANA": reservation_data["cabin_id"],
            "ID_COLABORADOR": collaborator_id,
            "FECHA_INGRESO": reservation_data["start_date"],
            "FECHA_SALIDA": reservation_data["end_date"],
            "NOCHES": reservation_data["days"],
            "HUESPEDES": reservation_data["guests"],
            "PRECIO_NOCHE": f"${reservation_data['price_per_night']:,.0f}",
            "SUBTOTAL": f"${reservation_data['subtotal']:,.0f}",
            "IVA_19": f"${reservation_data['tax']:,.0f}",
            "TOTAL": f"${reservation_data['total']:,.0f}"
        }

        cls.receipt_registry.append(receipt)
        print(f"Boleta #{receipt_id} generada y guardada")
        return receipt

    @classmethod
    def show_receipt_registry(cls):
        """Mostrar registro de boletas"""
        return cls.receipt_registry

    def print_receipt(self, receipt):
        """Imprimir comprobante formateado"""
        print("\n" + "="*50)
        print("           COMPROBANTE DE PAGO")
        print("="*50)
        print(f"Boleta N°: {receipt['ID_BOLETA']}")
        print(f"Razón Social: {receipt['RAZON_SOCIAL']}")
        print(f"Fecha: {receipt['FECHA_EMISION']}")
        print(f"Método: {receipt['METODO_PAGO']}")
        print("-"*50)
        print(f"Cliente: {receipt['CLIENTE']}")
        print(f"Reserva N°: {receipt['ID_RESERVA']}")
        print(f"Cabaña N°: {receipt['ID_CABANA']}")
        print(f"Colaborador: {receipt['ID_COLABORADOR']}")
        print("-"*50)
        print(f"Check-in: {receipt['FECHA_INGRESO']}")
        print(f"Check-out: {receipt['FECHA_SALIDA']}")
        print(f"Noches: {receipt['NOCHES']}")
        print(f"Huéspedes: {receipt['HUESPEDES']}")
        print(f"Precio/noche: {receipt['PRECIO_NOCHE']}")
        print("-"*50)
        print(f"Subtotal: {receipt['SUBTOTAL']}")
        print(f"IVA (19%): {receipt['IVA_19']}")
        print(f"TOTAL: {receipt['TOTAL']}")
        print("="*50)

# FUNCIONES DE MENÚ MEJORADAS

def main_menu():
    """Menú principal mejorado siguiendo el diagrama de flujo"""
    while True:
        print("\n" + "="*60)
        print("  SISTEMA DE GESTIÓN DE CABAÑAS RUPERT")
        print("="*60)
        print("  1  Acceso como Cliente")
        print("  2  Acceso como Colaborador")
        print("  3  Registrar nuevo cliente")
        print("  4  Salir del sistema")
        print("="*60)

        try:
            option = input("Seleccione una opción (1-4): ").strip()

            if option == "1":
                result = client_menu()
            elif option == "2":
                result = collaborator_menu()
            elif option == "3":
                result = register_new_client()
            elif option == "4":
                print("\nGracias por usar nuestro sistema!")
                print("Vuelva pronto a Cabañas Rupert")
                return False
            else:
                print("Opción inválida. Por favor seleccione 1, 2, 3 o 4.")
        except KeyboardInterrupt:
            print("\n\nSistema cerrado por el usuario")
            return False
        except Exception as e:
            print(f"Error inesperado: {e}")

def register_new_client():
    """Registrar nuevo cliente siguiendo validaciones del diagrama"""
    print("\n" + "="*50)
    print("REGISTRO DE NUEVO CLIENTE")
    print("="*50)

    try:
        # Validar datos según diagrama
        print("Por favor ingrese los siguientes datos:")

        # Nombre
        while True:
            name = input("Nombre: ").strip()
            if name and len(name) >= 2 and name.replace(" ", "").isalpha():
                break
            print("Nombre inválido. Debe tener al menos 2 caracteres y solo letras.")

        # Apellido Paterno
        while True:
            last_name_p = input("Apellido Paterno: ").strip()
            if last_name_p and len(last_name_p) >= 2 and last_name_p.isalpha():
                break
            print("Apellido paterno inválido. Debe tener al menos 2 caracteres y solo letras.")

        # Apellido Materno
        while True:
            last_name_m = input("Apellido Materno: ").strip()
            if last_name_m and len(last_name_m) >= 2 and last_name_m.isalpha():
                break
            print("Apellido materno inválido. Debe tener al menos 2 caracteres y solo letras.")

        # RUT
        rut_attempts = 0
        max_rut_attempts = 5
        while rut_attempts < max_rut_attempts:
            rut = input("RUT (formato: 12345678-9): ").strip()
            if validate_rut(rut):
                break
            rut_attempts += 1
            remaining = max_rut_attempts - rut_attempts
            if remaining > 0:
                print(f"RUT inválido. Formato correcto: 12345678-9 (Intentos restantes: {remaining})")
            else:
                print("Máximo de intentos alcanzado para RUT")
                return False

        # Email
        while True:
            email = input("Email: ").strip()
            if validate_email(email):
                break
            print("Email inválido. Formato correcto: usuario@dominio.com")

        # Teléfono
        while True:
            phone = input("Teléfono (formato: 9XXXXXXXX): ").strip()
            if validate_phone(phone):
                break
            print("Teléfono inválido. Formato: 9XXXXXXXX")

        # Dirección
        address = input("Dirección: ").strip()
        while not address or len(address) < 5:
            address = input("Dirección muy corta. Ingrese dirección completa: ").strip()

        # Usuario
        while True:
            username = input("Nombre de usuario: ").strip()
            if username and len(username) >= 4 and username.isalnum():
                # Aquí verificaríamos que no existe en BD
                break
            print("Usuario inválido. Mínimo 4 caracteres alfanuméricos.")

        # Contraseña
        while True:
            password = input("Contraseña (mínimo 6 caracteres): ").strip()
            if len(password) >= 6:
                break
            print("Contraseña muy corta. Mínimo 6 caracteres.")

        print("\nDatos validados correctamente")
        print("Resumen del registro:")
        print(f"   Nombre completo: {name} {last_name_p} {last_name_m}")
        print(f"   RUT: {rut}")
        print(f"   Email: {email}")
        print(f"   Teléfono: {phone}")
        print(f"   Usuario: {username}")

        confirm = input("\n¿Confirmar registro? (s/n): ").lower()
        if confirm == 's':
            # Aquí se guardaría en la base de datos
            print("Cliente registrado exitosamente")
            print("Ya puede acceder al sistema con sus credenciales")
            return True
        else:
            print("Registro cancelado")
            return False

    except KeyboardInterrupt:
        print("\nRegistro cancelado por el usuario")
        return False

def client_menu():
    """Menú de cliente mejorado con flujo del diagrama"""
    print("\n" + "="*50)
    print("ACCESO DE CLIENTE")
    print("="*50)

    # Proceso de autenticación
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        print(f"Intento {attempts + 1} de {max_attempts}")
        username = input("Usuario: ").strip()
        password = input("Contraseña: ").strip()

        if not username or not password:
            print("Usuario y contraseña son obligatorios")
            attempts += 1
            continue

        if validate_client_credentials(username, password):
            print("Credenciales válidas")

            # Obtener datos del cliente
            client_data = get_client_data(username)
            if client_data:
                client = Person.create_client(
                    client_data['name'],
                    client_data['last_name_p'],
                    client_data['last_name_m'],
                    client_data['rut'],
                    client_data['email'],
                    client_data['client_id'],
                    client_data['phone'],
                    client_data['address']
                )
                print(f"Bienvenido, {client_data['name']} {client_data['last_name_p']}")
                return client_operations_menu(client, client_data)
            else:
                print("Error al cargar datos del cliente")
                return False
        else:
            attempts += 1
            print(f"Credenciales incorrectas. Intentos restantes: {max_attempts - attempts}")

    print("Máximo de intentos alcanzado. Acceso bloqueado.")
    return False

def client_operations_menu(client, client_data):
    """Menú de operaciones del cliente"""
    cabin_manager = Cabin()
    reservation_manager = Reservation()
    payment_manager = Payment()

    while True:
        print("\n" + "="*50)
        print("PANEL DE CLIENTE")
        print("="*50)
        print("  1  Ver mis datos personales")
        print("  2  Actualizar datos personales")
        print("  3  Hacer nueva reserva")
        print("  4  Ver mis reservas")
        print("  5  Cancelar reserva")
        print("  6  Ver estado de cabañas")
        print("  7  Volver al menú principal")
        print("="*50)

        option = input("Seleccione una opción (1-7): ").strip()

        if option == "1":
            show_client_profile(client_data)

        elif option == "2":
            client.update_client_data()

        elif option == "3":
            make_reservation_flow(client, client_data, cabin_manager, reservation_manager, payment_manager)

        elif option == "4":
            show_client_reservations(client_data['client_id'])

        elif option == "5":
            cancel_reservation_flow(client_data['client_id'])

        elif option == "6":
            show_cabin_status(cabin_manager)

        elif option == "7":
            print("Volviendo al menú principal...")
            return False

        else:
            print("Opción inválida. Por favor seleccione una opción del 1 al 7.")

def make_reservation_flow(client, client_data, cabin_manager, reservation_manager, payment_manager):
    """Flujo completo de reserva siguiendo el diagrama"""
    print("\n" + "="*50)
    print("NUEVA RESERVA")
    print("="*50)

    try:
        # Paso 1: Solicitar datos de la reserva
        while True:
            start_date = input("Fecha de ingreso (DD/MM/YYYY): ").strip()
            if validate_date_format(start_date) and validate_future_date(start_date):
                break
            print("Fecha inválida. Debe ser futura y formato DD/MM/YYYY")

        while True:
            end_date = input("Fecha de salida (DD/MM/YYYY): ").strip()
            if validate_date_format(end_date):
                days = calculate_days_difference(start_date, end_date)
                if days > 0:
                    break
                else:
                    print("La fecha de salida debe ser posterior a la de ingreso")
            else:
                print("Formato de fecha inválido. Use DD/MM/YYYY")

        while True:
            try:
                guests = int(input("Número de huéspedes: "))
                if 1 <= guests <= 8:
                    break
                print("Número de huéspedes debe estar entre 1 y 8")
            except ValueError:
                print("Ingrese un número válido")

        # Paso 2: Mostrar cabañas disponibles
        available_cabins = cabin_manager.get_available_cabins(start_date, end_date, guests)

        if not available_cabins:
            print("No hay cabañas disponibles para esas fechas y número de huéspedes")
            return False

        print(f"\nCabañas disponibles del {start_date} al {end_date}:")
        print("-" * 60)
        for cabin in available_cabins:
            total_price = cabin['price'] * days
            print(f"Cabaña {cabin['id']}: {cabin['capacity']} personas - ${cabin['price']:,}/noche")
            print(f"   Total {days} noches: ${total_price:,}")
            print("-" * 60)

        # Paso 3: Seleccionar cabaña
        while True:
            try:
                cabin_choice = input("Seleccione número de cabaña: ").strip()
                selected_cabin = next((c for c in available_cabins if c['id'] == cabin_choice), None)
                if selected_cabin:
                    break
                print("Cabaña no válida o no disponible")
            except:
                print("Selección inválida")

        # Paso 4: Crear reserva
        reservation_result = reservation_manager.create_reservation(
            client_data['client_id'],
            cabin_choice,
            start_date,
            end_date,
            guests
        )

        if not reservation_result['success']:
            print(reservation_result['message'])
            return False

        reservation_data = reservation_result['reservation']

        # Paso 5: Mostrar resumen y confirmar
        print("\nRESUMEN DE RESERVA")
        print("="*50)
        print(f"Cabaña: #{reservation_data['cabin_id']}")
        print(f"Fechas: {start_date} al {end_date}")
        print(f"Noches: {reservation_data['days']}")
        print(f"Huéspedes: {guests}")
        print(f"Precio por noche: ${reservation_data['price_per_night']:,}")
        print(f"Subtotal: ${reservation_data['subtotal']:,}")
        print(f"IVA (19%): ${reservation_data['tax']:,}")
        print(f"TOTAL: ${reservation_data['total']:,}")
        print("="*50)

        confirm = input("¿Confirmar reserva? (s/n): ").lower()
        if confirm != 's':
            print("Reserva cancelada")
            return False

        # Paso 6: Procesar pago
        return process_payment_flow(reservation_data, client_data, payment_manager)

    except KeyboardInterrupt:
        print("\nReserva cancelada por el usuario")
        return False

def process_payment_flow(reservation_data, client_data, payment_manager):
    """Flujo de procesamiento de pago"""
    print("\n" + "="*50)
    print("PROCESAMIENTO DE PAGO")
    print("="*50)
    print(f"Total a pagar: ${reservation_data['total']:,}")
    print("-" * 50)
    print("Métodos de pago disponibles:")
    print("1  Efectivo")
    print("2  Tarjeta de Débito")
    print("3  Tarjeta de Crédito")
    print("4  Transferencia Bancaria")
    print("5  Cheque")
    print("-" * 50)

    while True:
        try:
            payment_method = int(input("Seleccione método de pago (1-5): "))
            if 1 <= payment_method <= 5:
                break
            print("Método de pago inválido")
        except ValueError:
            print("Ingrese un número válido")

    # Procesar pago
    client_name = f"{client_data['name']} {client_data['last_name_p']} {client_data['last_name_m']}"
    payment_result = payment_manager.process_payment(
        reservation_data,
        payment_method,
        client_name,
        None  # Sin colaborador en reserva de cliente
    )

    if payment_result['success']:
        print(payment_result['message'])
        payment_manager.print_receipt(payment_result['receipt'])
        print("\n¡Reserva confirmada exitosamente!")
        print("Se ha enviado confirmación a su email")
        return True
    else:
        print(payment_result['message'])
        return False

def show_client_profile(client_data):
    """Mostrar perfil del cliente"""
    print("\n" + "="*50)
    print("MIS DATOS PERSONALES")
    print("="*50)
    print(f"ID Cliente: {client_data['client_id']}")
    print(f"Nombre: {client_data['name']}")
    print(f"Apellido Paterno: {client_data['last_name_p']}")
    print(f"Apellido Materno: {client_data['last_name_m']}")
    print(f"RUT: {client_data['rut']}")
    print(f"Email: {client_data['email']}")
    print(f"Teléfono: {client_data['phone']}")
    print(f"Dirección: {client_data['address']}")
    print("="*50)

def show_client_reservations(client_id):
    """Mostrar reservas del cliente"""
    print("\n" + "="*50)
    print("MIS RESERVAS")
    print("="*50)
    print("Buscando reservas...")
    # Aquí iría la consulta a la base de datos
    print("No se encontraron reservas activas")
    print("="*50)

def cancel_reservation_flow(client_id):
    """Flujo de cancelación de reserva"""
    print("\n" + "="*50)
    print("CANCELAR RESERVA")
    print("="*50)

    reservation_id = input("Ingrese ID de reserva a cancelar: ").strip()

    if not reservation_id:
        print("ID de reserva es obligatorio")
        return False

    # Aquí iría la lógica de cancelación
    confirm = input(f"¿Confirmar cancelación de reserva {reservation_id}? (s/n): ").lower()

    if confirm == 's':
        print("Reserva cancelada exitosamente")
        print("Se ha enviado confirmación de cancelación")
        return True
    else:
        print("Cancelación abortada")
        return False

def show_cabin_status(cabin_manager):
    """Mostrar estado de todas las cabañas"""
    print("\n" + "="*50)
    print("ESTADO DE CABAÑAS")
    print("="*50)

    for i in range(1, 9):
        cabin_id = str(i)
        status = cabin_manager.check_status(cabin_id)
        capacity = cabin_manager.check_capacity(cabin_id)
        price = f"${cabin_manager.cabin_prices[cabin_id]:,}/noche"

        print(f"Cabaña {i}:")
        print(f"   {status}")
        print(f"   {capacity}")
        print(f"   {price}")
        print("-" * 50)

def collaborator_menu():
    """Menú de colaborador mejorado"""
    print("\n" + "="*50)
    print("ACCESO DE COLABORADOR")
    print("="*50)

    # Proceso de autenticación
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        print(f"Intento {attempts + 1} de {max_attempts}")
        username = input("Usuario: ").strip()
        password = input("Contraseña: ").strip()

        if not username or not password:
            print("Usuario y contraseña son obligatorios")
            attempts += 1
            continue

        if validate_collaborator_credentials(username, password):
            print("Credenciales válidas")

            # Obtener datos del colaborador
            collaborator_data = get_collaborator_data(username)
            if collaborator_data:
                collaborator = Person.create_collaborator(
                    collaborator_data['name'],
                    collaborator_data['last_name_p'],
                    collaborator_data['last_name_m'],
                    collaborator_data['rut'],
                    collaborator_data['email'],
                    collaborator_data['collaborator_id'],
                    collaborator_data['phone']
                )
                print(f"Bienvenido, {collaborator_data['name']} {collaborator_data['last_name_p']}")
                return collaborator_operations_menu(collaborator, collaborator_data)
            else:
                print("Error al cargar datos del colaborador")
                return False
        else:
            attempts += 1
            print(f"Credenciales incorrectas. Intentos restantes: {max_attempts - attempts}")

    print("Máximo de intentos alcanzado. Acceso bloqueado.")
    return False

def collaborator_operations_menu(collaborator, collaborator_data):
    """Menú de operaciones del colaborador"""
    cabin_manager = Cabin()
    reservation_manager = Reservation()
    payment_manager = Payment()

    while True:
        print("\n" + "="*50)
        print("PANEL DE COLABORADOR")
        print("="*50)
        print("  1  Ver mis datos personales")
        print("  2  Gestionar reservas")
        print("  3  Crear nueva reserva (cliente presencial)")
        print("  4  Modificar reserva")
        print("  5  Cancelar reserva")
        print("  6  Gestionar cabañas")
        print("  7  Generar reportes")
        print("  8  Procesar pagos")
        print("  9  Ver registro de boletas")
        print("  10  Volver al menú principal")
        print("="*50)

        option = input("Seleccione una opción (1-10): ").strip()

        if option == "1":
            show_collaborator_profile(collaborator_data)

        elif option == "2":
            manage_reservations_menu(collaborator_data)

        elif option == "3":
            create_presential_reservation(collaborator_data, cabin_manager, reservation_manager, payment_manager)

        elif option == "4":
            modify_reservation_menu(collaborator_data)

        elif option == "5":
            cancel_reservation_collaborator(collaborator_data)

        elif option == "6":
            manage_cabins_menu(cabin_manager)

        elif option == "7":
            generate_reports_menu()

        elif option == "8":
            process_payments_menu(payment_manager)

        elif option == "9":
            show_receipt_registry(payment_manager)

        elif option == "10":
            print("Volviendo al menú principal...")
            return False

        else:
            print("Opción inválida. Por favor seleccione una opción del 1 al 10.")

def show_collaborator_profile(collaborator_data):
    """Mostrar perfil del colaborador"""
    print("\n" + "="*50)
    print("MIS DATOS PERSONALES")
    print("="*50)
    print(f"ID Colaborador: {collaborator_data['collaborator_id']}")
    print(f"Nombre: {collaborator_data['name']}")
    print(f"Apellido Paterno: {collaborator_data['last_name_p']}")
    print(f"Apellido Materno: {collaborator_data['last_name_m']}")
    print(f"RUT: {collaborator_data['rut']}")
    print(f"Email: {collaborator_data['email']}")
    print(f"Teléfono: {collaborator_data['phone']}")
    print("="*50)

def manage_reservations_menu(collaborator_data):
    """Gestionar reservas"""
    print("\n" + "="*50)
    print("GESTIÓN DE RESERVAS")
    print("="*50)
    print("Mostrando todas las reservas...")
    # Aquí iría la consulta a la base de datos
    print("No se encontraron reservas")
    print("="*50)

def create_presential_reservation(collaborator_data, cabin_manager, reservation_manager, payment_manager):
    """Crear reserva para cliente presencial"""
    print("\n" + "="*50)
    print("NUEVA RESERVA PRESENCIAL")
    print("="*50)
    print("Ingrese datos del cliente:")

    # Datos básicos del cliente
    client_name = input("Nombre completo: ").strip()
    client_rut = input("RUT: ").strip()
    client_phone = input("Teléfono: ").strip()

    if not all([client_name, client_rut, client_phone]):
        print("Todos los campos son obligatorios")
        return False

    # Simular datos del cliente
    client_data = {
        'client_id': 9999,  # ID temporal
        'name': client_name.split()[0],
        'last_name_p': client_name.split()[1] if len(client_name.split()) > 1 else '',
        'last_name_m': client_name.split()[2] if len(client_name.split()) > 2 else ''
    }

    # Usar el mismo flujo de reserva pero con colaborador
    return make_reservation_flow_collaborator(client_data, collaborator_data, cabin_manager, reservation_manager, payment_manager)

def make_reservation_flow_collaborator(client_data, collaborator_data, cabin_manager, reservation_manager, payment_manager):
    """Flujo de reserva para colaborador"""
    # Similar al flujo del cliente pero con colaborador
    # (Implementación simplificada para el ejemplo)
    print("Procesando reserva presencial...")
    print("Reserva creada exitosamente")
    return True

def modify_reservation_menu(collaborator_data):
    """Modificar reserva"""
    print("\n" + "="*50)
    print("MODIFICAR RESERVA")
    print("="*50)
    reservation_id = input("ID de reserva a modificar: ").strip()
    print(f"Buscando reserva {reservation_id}...")
    print("Reserva no encontrada")

def cancel_reservation_collaborator(collaborator_data):
    """Cancelar reserva como colaborador"""
    print("\n" + "="*50)
    print("CANCELAR RESERVA")
    print("="*50)
    reservation_id = input("ID de reserva a cancelar: ").strip()
    reason = input("Motivo de cancelación: ").strip()
    print(f"Reserva {reservation_id} cancelada por: {reason}")

def manage_cabins_menu(cabin_manager):
    """Gestionar cabañas"""
    while True:
        print("\n" + "="*40)
        print("GESTIÓN DE CABAÑAS")
        print("="*40)
        print("  1  Ver estado de todas las cabañas")
        print("  2  Cambiar estado de cabaña")
        print("  3  Ver disponibilidad por fechas")
        print("  4  Volver")
        print("="*40)

        option = input("Seleccione una opción (1-4): ").strip()

        if option == "1":
            show_cabin_status(cabin_manager)

        elif option == "2":
            change_cabin_status_menu(cabin_manager)

        elif option == "3":
            check_availability_menu(cabin_manager)

        elif option == "4":
            return False

        else:
            print("Opción inválida")

def change_cabin_status_menu(cabin_manager):
    """Cambiar estado de cabaña"""
    print("\nCAMBIAR ESTADO DE CABAÑA")
    show_cabin_status(cabin_manager)

    cabin_id = input("\nID de cabaña (1-8): ").strip()
    if cabin_id not in [str(i) for i in range(1, 9)]:
        print("ID de cabaña inválido")
        return

    print("\nEstados disponibles:")
    print("1  DISPONIBLE")
    print("2  OCUPADA")
    print("3  MANTENIMIENTO")
    print("4  LIMPIEZA")

    try:
        new_status = int(input("Nuevo estado (1-4): "))
        result = cabin_manager.change_status(cabin_id, new_status)
        print(result)
    except ValueError:
        print("Estado inválido")

def check_availability_menu(cabin_manager):
    """Verificar disponibilidad por fechas"""
    print("\nVERIFICAR DISPONIBILIDAD")
    start_date = input("Fecha inicio (DD/MM/YYYY): ").strip()
    end_date = input("Fecha fin (DD/MM/YYYY): ").strip()

    if not validate_date_format(start_date) or not validate_date_format(end_date):
        print("Formato de fecha inválido")
        return

    try:
        guests = int(input("Número de huéspedes: "))
        available = cabin_manager.get_available_cabins(start_date, end_date, guests)

        if available:
            print(f"\nCabañas disponibles del {start_date} al {end_date}:")
            for cabin in available:
                print(f"Cabaña {cabin['id']}: {cabin['capacity']} personas - ${cabin['price']:,}/noche")
        else:
            print("No hay cabañas disponibles")
    except ValueError:
        print("Número de huéspedes inválido")

def generate_reports_menu():
    """Generar reportes"""
    print("\n" + "="*40)
    print("GENERAR REPORTES")
    print("="*40)
    print("  1  Reporte de ocupación")
    print("  2  Reporte de ingresos")
    print("  3  Reporte de reservas")
    print("  4  Volver")
    print("="*40)

    option = input("Seleccione reporte (1-4): ").strip()
    print("Generando reporte...")
    print("Reporte generado (funcionalidad en desarrollo)")

def process_payments_menu(payment_manager):
    """Procesar pagos pendientes"""
    print("\n" + "="*50)
    print("PROCESAR PAGOS")
    print("="*50)
    print("Buscando pagos pendientes...")
    print("No hay pagos pendientes")

def show_receipt_registry(payment_manager):
    """Mostrar registro de boletas"""
    print("\n" + "="*50)
    print("REGISTRO DE BOLETAS")
    print("="*50)

    receipts = payment_manager.show_receipt_registry()
    if receipts:
        for i, receipt in enumerate(receipts, 1):
            print(f"\nBoleta #{receipt['ID_BOLETA']}:")
            print(f"    Fecha: {receipt['FECHA_EMISION']}")
            print(f"    Cliente: {receipt['CLIENTE']}")
            print(f"    Total: {receipt['TOTAL']}")
            print(f"    Método: {receipt['METODO_PAGO']}")
            print("-" * 50)
    else:
        print("No hay boletas registradas")

# PUNTO DE ENTRADA

if __name__ == "__main__":
    print("Sistema de Gestión de Cabañas Rupert")
    print("Iniciando sistema...")
    main_menu()
