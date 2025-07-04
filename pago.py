from db import Database

class Pago:
    def __init__(self):
        self.db = Database()

    def create(self, idPAGO, fechaInicio, fechaFin, monto, metodoPago):
        query = """
        INSERT INTO PAGO (idPAGO, fechaInicio, fechaFin, monto, metodoPago)
        VALUES (%s, %s, %s, %s, %s)
        """
        self.db.execute(query, (idPAGO, fechaInicio, fechaFin, monto, metodoPago))

    def read_all(self):
        query = "SELECT * FROM PAGO"
        self.db.execute(query)
        return self.db.fetchall()

    def update(self, idPAGO, fechaInicio=None, fechaFin=None, monto=None, metodoPago=None):
        fields = []
        params = []
        if fechaInicio is not None:
            fields.append("fechaInicio=%s")
            params.append(fechaInicio)
        if fechaFin is not None:
            fields.append("fechaFin=%s")
            params.append(fechaFin)
        if monto is not None:
            fields.append("monto=%s")
            params.append(monto)
        if metodoPago is not None:
            fields.append("metodoPago=%s")
            params.append(metodoPago)
        if not fields:
            return
        params.append(idPAGO)
        query = f"UPDATE PAGO SET {', '.join(fields)} WHERE idPAGO=%s"
        self.db.execute(query, params)

    def delete(self, idPAGO):
        query = "DELETE FROM PAGO WHERE idPAGO=%s"
        self.db.execute(query, (idPAGO,))

    def close(self):
        self.db.close()
