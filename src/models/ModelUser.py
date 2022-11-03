from .entities.User import User

class ModelUser():
    @classmethod
    def login(self, db, user):
        '''
        @db param = variable de conexion desde la aplicion
        @user param = usuario
        '''
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id_terapeuta, nombre, apellidos, username , password, turno, sueldo, especialidad, cedula FROM terapeuta where username='{}'".format(user.username)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                # * si hay un usuario
                print("usuario encontrado")
                user = User(row[0], row[1], row[2], row[3], User.check_password(row[4], user.password), row[5],row[6],row[7],row[8])
                return user
            else:
                print("Usuario none")
                return None
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "select id_terapeuta, nombre, apellidos, username from terapeuta where id_terapeuta={}".format(id)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                logged_user = User(row[0], row[1], row[2], row[3], None, "", 0, "","")
                return logged_user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
