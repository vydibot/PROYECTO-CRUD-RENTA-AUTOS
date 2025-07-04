from db import Database

class Auto:
    def __init__(self):
        self.db = Database()

    def create(self, idAUTO, modelo, marca, precioPorDia, estado):
        query = """
        INSERT INTO AUTO (idAUTO, modelo, marca, precioPorDia, estado)
        VALUES (%s, %s, %s, %s, %s)
        """
        self.db.execute(query, (idAUTO, modelo, marca, precioPorDia, estado))

    def read_all(self):
        query = "SELECT * FROM AUTO"
        self.db.execute(query)
        return self.db.fetchall()

    def update(self, idAUTO, modelo=None, marca=None, precioPorDia=None, estado=None):
        fields = []
        params = []
        if modelo is not None:
            fields.append("modelo=%s")
            params.append(modelo)
        if marca is not None:
            fields.append("marca=%s")
            params.append(marca)
        if precioPorDia is not None:
            fields.append("precioPorDia=%s")
            params.append(precioPorDia)
        if estado is not None:
            fields.append("estado=%s")
            params.append(estado)
        params.append(idAUTO)
        query = f"UPDATE AUTO SET {', '.join(fields)} WHERE idAUTO=%s"
        self.db.execute(query, params)

    def delete(self, idAUTO):
        query = "DELETE FROM AUTO WHERE idAUTO=%s"
        self.db.execute(query, (idAUTO,))

    def close(self):
        self.db.close()
