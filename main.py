from app import cli 
from app import app

if __name__ == "__main__":
    import os
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

# задаём переменной FLASK_APP значение main.py
# (.venv) PS C:\Users\Your_name\Desktop\Flask_project> set FLASK_APP=main.py
# запускаем flask (ищет экземпляр приложения указанный в переменной FLASK_APP)
# (.venv) PS C:\Users\Your_name\Desktop\Flask_project> flask run