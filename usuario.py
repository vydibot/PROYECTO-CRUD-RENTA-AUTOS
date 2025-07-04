from db import Database

class Usuario:
    def __init__(self):
        self.db = Database()

    def create(self, idUSUARIO, nombre, correo, cedula, telefono):
        query = """
        INSERT INTO USUARIO (idUSUARIO, nombre, correo, cedula, telefono)
        VALUES (%s, %s, %s, %s, %s)
        """
        self.db.execute(query, (idUSUARIO, nombre, correo, cedula, telefono))

    def read_all(self):
        query = "SELECT * FROM USUARIO"
        self.db.execute(query)
        return self.db.fetchall()

    def update(self, idUSUARIO, nombre=None, correo=None, cedula=None, telefono=None):
        fields = []
        params = []
        if nombre is not None:
            fields.append("nombre=%s")
            params.append(nombre)
        if correo is not None:
            fields.append("correo=%s")
            params.append(correo)
        if cedula is not None:
            fields.append("cedula=%s")
            params.append(cedula)
        if telefono is not None:
            fields.append("telefono=%s")
            params.append(telefono)
        if not fields:
            return
        params.append(idUSUARIO)
        query = f"UPDATE USUARIO SET {', '.join(fields)} WHERE idUSUARIO=%s"
        self.db.execute(query, params)

    def delete(self, idUSUARIO):
        query = "DELETE FROM USUARIO WHERE idUSUARIO=%s"
        self.db.execute(query, (idUSUARIO,))

    def close(self):
        self.db.close()
