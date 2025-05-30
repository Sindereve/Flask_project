 # 🧑‍💻 Flask-проект: Sindilitik 

Это веб-приложение, разработанное с использованием Flask и множества полезных расширений. Проект поддерживает регистрацию и авторизацию пользователей, работу с базой данных через ORM, локализацию интерфейса, загрузку изображений, отображение временных меток и настроенное логирование.


 ## **🔧 Основные функции:**

* Регистрация и вход пользователей (Flask-Login)
* ORM для работы с данными (SQLAlchemy + Flask-SQLAlchemy)
* Миграции базы данных (Flask-Migrate)
* Формы и валидация (Flask-WTF)
* Локализация интерфейса (Flask-Babel)
* Отображение временных меток (Flask-Moment)
* Загрузка изображений (Flask-Uploads)
* Настроенное логирование (RotatingFileHandler)
* Проект включает RESTful API с поддержкой аутентификации(Flask-HTTPAuth)


 ## 📦 Технологии: 

* python 3.10.x
* больше информации найдёте в файле requirements.txt

---

 ## 🛠️ Установка и запуск

 1. Клонируйте репозиторий:
```bash
git clone https://github.com/Sindereve/Flask_project
cd Flask_project
```

 2. Создайте виртуальное окружение и установите зависимости:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

 3. Запустите приложение

В репозитории уже хранится тестовый вариант миграции. Поэтому можно пропустить пункт связанный с миграцией и перейти к запуску

```bash
flask run
```

 ## Скриншоты (2560x1440)

<div align="center">
 <h2>Авторизация</h2>
 <p>Вход в учетную запись</p>
 <img src="https://github.com/user-attachments/assets/95766699-c0af-4cf2-aa67-7c7765d08dcc"  width="800" />
</div>

<div align="center">
 <h2>Регистрация</h2>
 <p>Создание новой учетной записи</p>
 <img src="https://github.com/user-attachments/assets/1a5487c5-840d-4a51-81af-0d59aebfda2b"  width="800" />
</div>

<div align="center">
 <h2>Домашняя страница</h2>
 <p>Посты пользователя и тех, на кого оформлены подписки</p>
 <img src="https://github.com/user-attachments/assets/0b01986d-7a9e-4812-8173-96b2df9ca274"  width="800" />
 <img src="https://github.com/user-attachments/assets/7d277a55-576c-4280-8e7b-d76d8adba195"  width="800" />
</div>

<div align="center">
 <h2>Профиль пользователя</h2>
 <p>Отображение информации о пользователе (токен, статистика, посты)</p>
 <img src="https://github.com/user-attachments/assets/ebdde5a4-f725-4657-aaf0-aaa0f12e6896"  width="800" />
</div>

<div align="center">
 <h2>Все посты</h2>
 <p>Просмотр всех существующих постов</p>
 <img src="https://github.com/user-attachments/assets/a4175956-843b-42e2-bc58-5d08aeebfcf8"  width="800" />
</div>

<div align="center">
 <h2>Примеры локализации</h2>
 <p>Интерфейс на русском и немецком языках</p>
 <img src="https://github.com/user-attachments/assets/bda7a064-b8eb-4652-9eba-0bb8860cc172"  width="800" />
 <img src="https://github.com/user-attachments/assets/29cc9e0a-22c4-4f1d-b59c-0cb1973cb295"  width="800" />
</div>

