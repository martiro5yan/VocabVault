import authentication
import db_initializer

def createDict(data):
    result_dict = {}
    for item in data:
        key = item[0]
        values = tuple(item[1:])  # Создаем кортеж из оставшихся элементов
        result_dict.setdefault(key, []).append(values)  # Добавляем кортеж в список
    return result_dict

dict_name_list =[]
def list_dict():
    username = authentication.uservv.username
    connection = authentication.connect_to_db()
    cursor = connection.cursor()

    cursor.execute('SELECT dictionary_name FROM dictionary_entries WHERE username = %s',(username,))
    listword = cursor.fetchall()
    listword_revers = listword[::-1]
    for i in listword_revers:
        if i[0] not in dict_name_list:
            dict_name_list.append(i[0])
    return dict_name_list


def load_data_toDay():
    print('dictToday')
    connection = authentication.connect_to_db()
    cursor = connection.cursor()
    username = authentication.uservv.username
    day = db_initializer.dictName()
    print(day)
   
    cursor.execute("SELECT dictionary_name, word, translation FROM dictionary_entries WHERE username = %s and dictionary_name = %s",(username,day))
    listword = cursor.fetchall()
    listword_revers = listword[::-1]
    
    result = createDict(listword_revers)
    
    if day in result:
        return result[day]
    else:
        return False
    
def getting_all_dictionaries():
    username = authentication.uservv.username
    connection = authentication.connect_to_db()
    cursor = connection.cursor()

    cursor.execute("SELECT dictionary_name, word, translation FROM dictionary_entries WHERE username = %s",(username,))
    listword = cursor.fetchall()
    listword_revers = listword[::-1]
    
    result = createDict(listword_revers)

    return result
