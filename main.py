from auto import Auto
from admin import Admin
from pago import Pago
from reserva import Reserva
from usuario import Usuario
def main_menu():
    while True:
        print("\n--- CRUD APP RENTA DE AUTOS---")
        print("1. Autos")
        print("2. Admins")
        print("3. Pagos")
        print("4. Reservas")
        print("5. Usuarios")
        print("0. Salir")
        choice = input("Seleccione una opción: ")
        if choice == '1':
            crud_menu(Auto(), 'Auto')
        elif choice == '2':
            crud_menu(Admin(), 'Admin')
        elif choice == '3':
            crud_menu(Pago(), 'Pago')
        elif choice == '4':
            crud_menu(Reserva(), 'Reserva')
        elif choice == '5':
            crud_menu(Usuario(), 'Usuario')
        elif choice == '0':
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

def crud_menu(obj, name):
    while True:
        print(f"\n--- CRUD {name} ---")
        print("1. Crear")
        print("2. Leer todo")
        print("3. Actualizar")
        print("4. Eliminar")
        print("0. Volver")
        choice = input("Seleccione una opción: ")
        if choice == '1':
            create_entry(obj, name)
        elif choice == '2':
            for row in obj.read_all():
                print(row)
        elif choice == '3':
            update_entry(obj, name)
        elif choice == '4':
            delete_entry(obj, name)
        elif choice == '0':
            obj.close()
            break
        else:
            print("Opción inválida.")

def create_entry(obj, name):
    print(f"\nCrear nuevo {name}:")
    if name == 'Auto':
        idAUTO = int(input("idAUTO: "))
        modelo = int(input("modelo: "))
        marca = input("marca: ")
        precioPorDia = float(input("precioPorDia: "))
        estado = input("estado: ")
        obj.create(idAUTO, modelo, marca, precioPorDia, estado)
    elif name == 'Admin':
        idADMIN = int(input("idADMIN: "))
        nombre = input("nombre: ")
        correo = input("correo: ")
        contrasena = input("contraseña: ")
        obj.create(idADMIN, nombre, correo, contrasena)
    elif name == 'Pago':
        idPAGO = int(input("idPAGO: "))
        fechaInicio = input("fechaInicio (YYYY-MM-DD): ")
        fechaFin = input("fechaFin (YYYY-MM-DD): ")
        monto = float(input("monto: "))
        metodoPago = input("metodoPago: ")
        obj.create(idPAGO, fechaInicio, fechaFin, monto, metodoPago)
    elif name == 'Reserva':
        idRESERVA = int(input("idRESERVA: "))
        fechaInicio = input("fechaInicio (YYYY-MM-DD): ")
        fechaFin = input("fechaFin (YYYY-MM-DD): ")
        obj.create(idRESERVA, fechaInicio, fechaFin)
    elif name == 'Usuario':
        idUSUARIO = int(input("idUSUARIO: "))
        nombre = input("nombre: ")
        correo = input("correo: ")
        cedula = input("cedula: ")
        telefono = input("telefono: ")
        obj.create(idUSUARIO, nombre, correo, cedula, telefono)
    print(f"{name} creado correctamente.")

def update_entry(obj, name):
    print(f"\nActualizar {name}:")
    id_field = {
        'Auto': 'idAUTO',
        'Admin': 'idADMIN',
        'Pago': 'idPAGO',
        'Reserva': 'idRESERVA',
        'Usuario': 'idUSUARIO'
    }[name]
    id_value = int(input(f"{id_field}: "))
    if name == 'Auto':
        modelo = input("modelo (dejar vacío para no cambiar): ")
        marca = input("marca (dejar vacío para no cambiar): ")
        precioPorDia = input("precioPorDia (dejar vacío para no cambiar): ")
        estado = input("estado (dejar vacío para no cambiar): ")
        obj.update(id_value,
            int(modelo) if modelo else None,
            marca if marca else None,
            float(precioPorDia) if precioPorDia else None,
            estado if estado else None)
    elif name == 'Admin':
        nombre = input("nombre (dejar vacío para no cambiar): ")
        correo = input("correo (dejar vacío para no cambiar): ")
        contrasena = input("contraseña (dejar vacío para no cambiar): ")
        obj.update(id_value,
            nombre if nombre else None,
            correo if correo else None,
            contrasena if contrasena else None)
    elif name == 'Pago':
        fechaInicio = input("fechaInicio (YYYY-MM-DD, dejar vacío para no cambiar): ")
        fechaFin = input("fechaFin (YYYY-MM-DD, dejar vacío para no cambiar): ")
        monto = input("monto (dejar vacío para no cambiar): ")
        metodoPago = input("metodoPago (dejar vacío para no cambiar): ")
        obj.update(id_value,
            fechaInicio if fechaInicio else None,
            fechaFin if fechaFin else None,
            float(monto) if monto else None,
            metodoPago if metodoPago else None)
    elif name == 'Reserva':
        fechaInicio = input("fechaInicio (YYYY-MM-DD, dejar vacío para no cambiar): ")
        fechaFin = input("fechaFin (YYYY-MM-DD, dejar vacío para no cambiar): ")
        obj.update(id_value,
            fechaInicio if fechaInicio else None,
            fechaFin if fechaFin else None)
    elif name == 'Usuario':
        nombre = input("nombre (dejar vacío para no cambiar): ")
        correo = input("correo (dejar vacío para no cambiar): ")
        cedula = input("cedula (dejar vacío para no cambiar): ")
        telefono = input("telefono (dejar vacío para no cambiar): ")
        obj.update(id_value,
            nombre if nombre else None,
            correo if correo else None,
            cedula if cedula else None,
            telefono if telefono else None)
    print(f"{name} actualizado correctamente.")

def delete_entry(obj, name):
    print(f"\nEliminar {name}:")
    id_field = {
        'Auto': 'idAUTO',
        'Admin': 'idADMIN',
        'Pago': 'idPAGO',
        'Reserva': 'idRESERVA',
        'Usuario': 'idUSUARIO'
    }[name]
    id_value = int(input(f"{id_field}: "))
    obj.delete(id_value)
    print(f"{name} eliminado correctamente.")

if __name__ == "__main__":
    main_menu()
