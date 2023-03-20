import mysql.connector


def connector():
    cnx = mysql.connector.connect(
            user="root", password="12345",
            host="127.0.0.1",
            database="apresentacao"
        )
    return cnx, cnx.cursor()
