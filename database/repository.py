import database.connector as db_connector

def insert_cep(cep, logradouro, complemento, bairro, localidade, uf):
    cnx, cursor = db_connector.connector()
    sql = "insert into ceps(cep, logradouro, complemento, bairro, localidade, uf) values (%s, %s, %s, %s, %s, %s);"
    data_insert = (cep, logradouro, complemento, bairro, localidade, uf)
    cursor.execute(sql, data_insert)
    cnx.commit()
    cnx.close()
