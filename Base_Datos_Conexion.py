import mysql.connector


class Conexion_Base_Datos():

    def conexion(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="zeus",
            password="1234567890",
            database="socialnet"
        )
        return mydb
    
    def Conexion_User1(self, user):

        Conex = self.conexion()
        mycursor = Conex.cursor()
        orden = "SELECT email FROM Usuario WHERE email=%s and password=%s"
        mycursor.execute(orden, user)
        myresult = mycursor.fetchall()
        mycursor.close()
        Conex.close()
        if myresult==[]:
            return False
        else:
            return True
            

    
    




#print(mydb) 

#x=Conexion_User1()
#print(x)

#mydb.close()
