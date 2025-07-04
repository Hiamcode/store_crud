from database.connection import get_connection

def test_connection():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users;")
        results = cursor.fetchall()

        print("Conexión exitosa. Aquí están los datos de la tabla 'users':")
        for row in results:
            print(row)

    except Exception as e:
        print("Error al conectar o consultar:", e)

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    test_connection()