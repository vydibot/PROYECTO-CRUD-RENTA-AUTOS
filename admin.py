from db import Database

class Admin:
    def __init__(self):
        self.db = Database()

    def create(self, idADMIN, nombre, correo, contrasena):
        query = """
        INSERT INTO ADMIN (idADMIN, nombre, correo, contraseña)
        VALUES (%s, %s, %s, %s)
        """
        self.db.execute(query, (idADMIN, nombre, correo, contrasena))

    def read_all(self):
        query = "SELECT * FROM ADMIN"
        self.db.execute(query)
        return self.db.fetchall()

    def update(self, idADMIN, nombre=None, correo=None, contrasena=None):
        fields = []
        params = []
        if nombre is not None:
            fields.append("nombre=%s")
            params.append(nombre)
        if correo is not None:
            fields.append("correo=%s")
            params.append(correo)
        if contrasena is not None:
            fields.append("contraseña=%s")
            params.append(contrasena)
        if not fields:
            return
        params.append(idADMIN)
        query = f"UPDATE ADMIN SET {', '.join(fields)} WHERE idADMIN=%s"
        self.db.execute(query, params)

    def delete(self, idADMIN):
        query = "DELETE FROM ADMIN WHERE idADMIN=%s"
        self.db.execute(query, (idADMIN,))

    def close(self):
        self.db.close()
