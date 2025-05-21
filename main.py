def main():
    from app import app

if __name__ == "__main__":
    main()

# задаём переменной FLASK_APP значение main.py
# (.venv) PS C:\Users\Your_name\Desktop\Flask_project> set FLASK_APP=main.py
# запускаем flask (ищет экземпляр приложения указанный в переменной FLASK_APP)
# (.venv) PS C:\Users\Your_name\Desktop\Flask_project> flask run