from werkzeug.security import check_password_hash

class User():
    def __init__(self, id, nombre, apellidos, username, password, turno, sueldo, especialidad, cedula) -> None:
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.username = username
        self.password = password
        self.turno = turno
        self.sueldo = sueldo
        self.especialidad = especialidad
        self.cedula = cedula

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)


# print(generate_password_hash("santiagomor"))
