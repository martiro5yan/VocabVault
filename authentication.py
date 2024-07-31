import psycopg2

class user:
    def __init__(self,username = None) -> None:
        self.username = username

uservv = user()

def connect_to_db():
    connection = psycopg2.connect(
        host='localhost',
        dbname='vocabvault',
        user='postgres',
        password='Hesoyam1',
        port=5432,
        options='-c client_encoding=UTF8')
    print("Подключение установлено")
    return connection


def dict_values_to_tuple(value):
    key, values = list(value.items())[0]
    return tuple(values)


def registration(values):
    value = dict_values_to_tuple(values)
    print(value)
    
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users(login,password) VALUES(%s,%s)",value)
    connection.commit()
    return True
    # else:
    #     return False

def authorization(values):
    value = dict_values_to_tuple(values)
    login = value[0]
    password = value[1]
    uservv.username = login
    connection = connect_to_db()
    cursor = connection.cursor()
    
    query_string = """
    SELECT EXISTS (
        SELECT 1
        FROM users
        WHERE login = %s
    ) AND EXISTS (
        SELECT 1
        FROM users
        WHERE password = %s
    );
    """
    cursor.execute(query_string, (login, password))
    result = cursor.fetchone()[0]
    
    cursor.close()
    connection.close()
    if result == True:
        return True
    else:
        return False