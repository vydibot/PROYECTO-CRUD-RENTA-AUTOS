from db import Database

class Reserva:
    def __init__(self):
        self.db = Database()

    def create(self, idRESERVA, fechaInicio, fechaFin, idUSUARIO, idAUTO, idPAGO):
        query = """
        INSERT INTO RESERVA (idRESERVA, fechaInicio, fechaFin, idUSUARIO, idAUTO, idPAGO)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.db.execute(query, (idRESERVA, fechaInicio, fechaFin, idUSUARIO, idAUTO, idPAGO))

    def read_all(self):
        query = "SELECT * FROM RESERVA"
        self.db.execute(query)
        return self.db.fetchall()

    def update(self, idRESERVA, fechaInicio=None, fechaFin=None, idUSUARIO=None, idAUTO=None, idPAGO=None):
        fields = []
        params = []
        if fechaInicio is not None:
            fields.append("fechaInicio=%s")
            params.append(fechaInicio)
        if fechaFin is not None:
            fields.append("fechaFin=%s")
            params.append(fechaFin)
        if idUSUARIO is not None:
            fields.append("idUSUARIO=%s")
            params.append(idUSUARIO)
        if idAUTO is not None:
            fields.append("idAUTO=%s")
            params.append(idAUTO)
        if idPAGO is not None:
            fields.append("idPAGO=%s")
            params.append(idPAGO)
        if not fields:
            return
        params.append(idRESERVA)
        query = f"UPDATE RESERVA SET {', '.join(fields)} WHERE idRESERVA=%s"
        self.db.execute(query, params)

    def delete(self, idRESERVA):
        query = "DELETE FROM RESERVA WHERE idRESERVA=%s"
        self.db.execute(query, (idRESERVA,))

    def close(self):
        self.db.close()
