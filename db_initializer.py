from datetime import datetime
import authentication



def dictName():
    # Получаем текущую дату и время
    now = datetime.now()
    
    # Определяем список с именами месяцев на русском языке
    months = [
        "января", "февраля", "марта", "апреля", "мая", "июня",
        "июля", "августа", "сентября", "октября", "ноября", "декабря"
    ]
    
    # Получаем имя месяца на русском языке
    month_name = months[now.month - 1]
    
    # Получаем день и год
    day = now.day
    year = now.year
    
    # Формируем строку в нужном формате
    date_string = f"{day} {month_name} {year}"
    

    return date_string

def sendData(data):
    try:
        data = data['Value']
        data.insert(0, dictName())
        data.insert(0, authentication.uservv.username)
        
        connection = authentication.connect_to_db()
        cursor = connection.cursor()
        print(data)
        if len(data) == 4:
            cursor.execute("INSERT INTO dictionary_entries (username, dictionary_name, word, translation) VALUES (%s, %s, %s, %s)", tuple(data))
        else:
            cursor.execute("INSERT INTO dictionary_entries (username, dictionary_name, word) VALUES (%s, %s, %s)", tuple(data))
            
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except Exception as e:
        print(f"Error occurred: {e}")
        return False