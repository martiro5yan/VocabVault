# VocabVault
## Установка
Клонируйте репозиторий:

bash
Копировать код
git clone https://github.com/yourusername/vocabulary-vault.git
cd vocabulary-vault
Создайте и активируйте виртуальное окружение:

bash
Копировать код
python -m venv venv
source venv/bin/activate  # На Windows используйте `venv\Scripts\activate`
Установите зависимости:

bash
Копировать код
pip install -r requirements.txt
Настройте базу данных:

Убедитесь, что PostgreSQL установлен и работает.
Создайте базу данных с именем vocabvault.
Создайте пользователя и установите пароль (если это необходимо) и укажите их в коде (см. connect_to_db в authentication.py).
Инициализируйте базу данных:

Запустите скрипт для создания начальных таблиц и данных. Этот скрипт должен быть в проекте, возможно, его нужно будет создать вручную.

Запустите сервер Flask:

bash
Копировать код
python app.py
Откройте веб-браузер и перейдите по адресу:

arduino
Копировать код
http://127.0.0.1:5000/
