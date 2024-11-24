import mysql.connector
from mysql.connector import Error


# Função para conectar ao banco de dados
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="DutrSQL2321017",
            database="gestao_condominio"
        )
        if connection.is_connected():
            print("Conexão bem-sucedida!")
        return connection
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None


# Função para executar uma consulta
def run_query(query, params=None):
    connection = connect_to_db()
    if not connection:
        return None
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, params)
        result = None
        if query.strip().lower().startswith("select"):
            result = cursor.fetchall()
        connection.commit()
        return result
    except Error as e:
        print(f"Erro ao executar a consulta: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
