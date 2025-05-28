# seed/seed_data.py

seed_data = {
    "users": [
        {
            "username": "john_doe",
            "email": "john@example.com",
            "password": "password",
            "about_me": "Python разработчик. Пишу о веб-разработке, Flask, SQLAlchemy и автоматизации."
        },
        {
            "username": "jane_smith",
            "email": "jane@example.com",
            "password": "password",
            "about_me": "Data Scientist. Люблю делиться знаниями о Pandas, машинном обучении и анализе данных."
        },
        {
            "username": "code_wizard",
            "email": "wizard@example.com",
            "password": "password",
            "about_me": "Full-stack разработчик. Пишу про JavaScript, Python, React и архитектуру приложений."
        },
        {
            "username": "travel_junkie",
            "email": "traveler@example.com",
            "password": "password",
            "about_me": "Любитель путешествий. Делюсь историями, советами и фотоотчетами из разных стран."
        },
        {
            "username": "tech_nerd",
            "email": "nerd@example.com",
            "password": "password",
            "about_me": "Обожаю всё, что связано с технологиями. Обзоры гаджетов, обсуждение ИИ, робототехники и IT-новинок."
        },
        {
            "username": "fitness_master",
            "email": "fitmaster@example.com",
            "password": "password",
            "about_me": "Фитнес-тренер. Советы по тренировкам, питанию и мотивации для здоровой жизни."
        },
        {
            "username": "art_lover",
            "email": "artist@example.com",
            "password": "password",
            "about_me": "Художник и любитель искусства. Рассказываю об истории искусства, современных художниках и своих работах."
        },
        {
            "username": "eco_warrior",
            "email": "greenman@example.com",
            "password": "password",
            "about_me": "Экологический активист. Пишу о защите окружающей среды, устойчивом образе жизни и климатических изменениях."
        },
        {
            "username": "history_buff",
            "email": "historian@example.com",
            "password": "password",
            "about_me": "Поклонник истории. Статьи о древних цивилизациях, войнах, культуре и интересных исторических фактах."
        },
        {
            "username": "foodie_expert",
            "email": "chef@example.com",
            "password": "password",
            "about_me": "Любитель еды и кулинарии. Рецепты, обзоры ресторанов, лайфхаки для кухни и кулинарные туры."
        }
    ],
    "posts": [
        # john_doe — 5 статей
        {
            "title": "Зачем нужен ORM?",
            "body": "ORM помогает работать с базами данных как с объектами, без необходимости писать сырой SQL. "
                    "Он абстрагирует работу с таблицами и позволяет легко манипулировать данными.",
            "username": "john_doe",
            "images": [{"url": "https://optimalgroup.ru/upload/iblock/bb0/3sthboj1ljyc62co9458qksmsydjg7p0.jpg", 
                        "caption": "ORM Diagram"}]
        },
        {
            "title": "Введение в Flask",
            "body": "Flask — это легковесный веб-фреймворк на Python. Он прост в освоении и идеально подходит для небольших проектов и API.",
            "username": "john_doe",
            "images": []
        },
        {
            "title": "SQLAlchemy: основы работы",
            "body": "SQLAlchemy — один из самых мощных ORM для Python. В этой статье мы рассмотрим базовые примеры его использования.",
            "username": "john_doe",
            "images": [{"url": "https://th.bing.com/th/id/OIP.2CD82cnBeroRaEVmgEXUhgHaDW?rs=1&pid=ImgDetMain", "caption": "SQLAlchemy Example"}]
        },
        {
            "title": "Как использовать Flask-Migrate",
            "body": "Flask-Migrate — это инструмент для управления миграциями БД в Flask. Узнайте, как он работает и как начать с ним работать.",
            "username": "john_doe",
            "images": []
        },
        {
            "title": "Работа с Flask-WTF",
            "body": "Flask-WTF упрощает работу с формами в Flask. Научитесь создавать формы, проверять их и обрабатывать данные.",
            "username": "john_doe",
            "images": [{"url": "https://assets.digitalocean.com/articles/how-to-code-in-flask-banner/how-to-code-in-flask.png", 
                        "caption": "Form example"}]
        },

        # jane_smith — 4 статьи
        {
            "title": "Анализ данных с Pandas",
            "body": "Pandas — мощная библиотека для анализа данных. Здесь мы рассмотрим основные методы и примеры работы с DataFrame.",
            "username": "jane_smith",
            "images": [{"url": "https://th.bing.com/th/id/OIP.HG4ZQ3esZRkX-0Zv7wTQSwHaEo?rs=1&pid=ImgDetMain", 
                        "caption": "Мишка"}]
        },
        {
            "title": "Машинное обучение для новичков",
            "body": "Что такое машинное обучение? Какие есть алгоритмы? Где применять? Начинаем с основ!",
            "username": "jane_smith",
            "images": [{"url": "https://248006.selcdn.ru/main/iblock/7fb/7fbf5f6df959f9cba3d3444632b5782a/da5360fd69c01fee6ea8793207be8f56.jpg", 
                        "caption": "ML Overview"}]
        },
        {
            "title": "Визуализация данных с matplotlib",
            "body": "Matplotlib — одна из самых популярных библиотек для построения графиков и диаграмм в Python. Примеры использования внутри Pandas.",
            "username": "jane_smith",
            "images": []
        },
        {
            "title": "Где брать данные для анализа",
            "body": "В этой статье я расскажу, где найти качественные открытые датасеты для обучения и исследований.",
            "username": "jane_smith",
            "images": [{"url": "https://wifigid.ru/wp-content/uploads/2022/09/01-58.jpg", 
                        "caption": "Dataset example"}]
        },

        # code_wizard — 4 статьи
        {
            "title": "JavaScript vs Python: кто лучше?",
            "body": "Сравниваем два популярных языка программирования: где какой лучше использовать, какие перспективы.",
            "username": "code_wizard",
            "images": [{"url":"https://www.programmingcube.com/wp-content/uploads/2021/05/python-vs-javascript.jpg,",
                        "caption": "image"}]
        },
        {
            "title": "React: начало работы",
            "body": "React — фреймворк (библиотека) от Facebook для создания интерфейсов. Этот гайд поможет тебе начать с него работать.",
            "username": "code_wizard",
            "images": [{"url": "https://i.ytimg.com/vi/s2skans2dP4/maxresdefault.jpg", "caption": "React"}]
        },
        {
            "title": "Тестирование кода: Jest и Pytest",
            "body": "Jest и Pytest — одни из лучших тестовых фреймворков. Узнайте, как их использовать в JS и Python.",
            "username": "code_wizard",
            "images": []
        },
        {
            "title": "Docker для разработчика",
            "body": "Docker — инструмент для контейнеризации приложений. Мы расскажем, как начать его использовать и зачем он нужен.",
            "username": "code_wizard",
            "images": [{"url": "https://rwsite.ru/wp-content/cache/thumb/6b/28ac06fda8ddf6b_1000x480.webp", 
                        "caption": "Docker container"}]
        },

        # travel_junkie — 4 статьи
        {
            "title": "Топ 10 стран для самостоятельных путешествий",
            "body": "Если вы хотите путешествовать самостоятельно — эта статья для вас. Мы собрали список безопасных и доступных стран.",
            "username": "travel_junkie",
            "images": [{"url": "https://th.bing.com/th/id/OIP.-xOhrcuX7aPEIB2sd5HK8wHaEi?rs=1&pid=ImgDetMain", 
                        "caption": "World map"}]
        },
        {
            "title": "Бюджетные отели в Европе",
            "body": "Как найти недорогие, но комфортные места для проживания в Европе? Советы и рекомендации.",
            "username": "travel_junkie",
            "images": []
        },
        {
            "title": "Камчатка: удивительная природа России",
            "body": "Путешествие по Камчатке — уникальный опыт. Вулканы, гейзеры, медведи и чистейшая природа.",
            "username": "travel_junkie",
            "images": [{"url": "https://set-travel.com/wp-content/uploads/2019/12/1cbdfb6436cb293066925767f2a0c9d3_xl.jpg", 
                        "caption": "Kamchatka nature"}]
        },

        # tech_nerd — 4 статьи
        {
            "title": "Чипы будущего: Intel, AMD, Apple M1",
            "body": "Сравнение процессоров и тренды развития компьютерной техники. Что ждать от новых поколений чипов?",
            "username": "tech_nerd",
            "images": [{"url": "https://th.bing.com/th/id/OIP.Clcac-Z_FHTDkvBuF2WjMAHaEG?rs=1&pid=ImgDetMain", 
                        "caption": "CPU chip"}]
        },
        {
            "title": "Что такое искусственный интеллект?",
            "body": "AI становится частью повседневности. Разбираемся, что это, и как он влияет на нашу жизнь.",
            "username": "tech_nerd",
            "images": []
        },
        {
            "title": "Будущее мобильных телефонов",
            "body": "Какими будут смартфоны через 5 лет? Гибкие экраны, нейросети, ультразвуковая зарядка и многое другое.",
            "username": "tech_nerd",
            "images": [{"url": "https://th.bing.com/th/id/OIP.CgOwYx4hBa-szhmdVyvMBAHaD2?rs=1&pid=ImgDetMain", 
                        "caption": "Future"}]
        },
        {
            "title": "Умный дом: технологии будущего",
            "body": "Устройства с голосовым управлением, системы безопасности и автоматизация — всё это уже здесь.",
            "username": "tech_nerd",
            "images": [{"url": "https://th.bing.com/th/id/OIP.9v2nE72O5Rj47Ff7b7TdcAHaEA?rs=1&pid=ImgDetMain", 
                        "caption": "Smart home"},
                        {"url": "https://th.bing.com/th/id/OIP.9v2nE72O5Rj47Ff7b7TdcAHaEA?rs=1&pid=ImgDetMain", 
                        "caption": "Smart home"}]
        },
    ],
    "follows": [
        {"follower": "jane_smith", "followed": "john_doe"},
        {"follower": "code_wizard", "followed": "john_doe"},
        {"follower": "travel_junkie", "followed": "john_doe"},
        {"follower": "tech_nerd", "followed": "john_doe"},

        {"follower": "john_doe", "followed": "jane_smith"},
        {"follower": "code_wizard", "followed": "jane_smith"},
        {"follower": "eco_warrior", "followed": "jane_smith"},

        {"follower": "john_doe", "followed": "code_wizard"},
        {"follower": "travel_junkie", "followed": "code_wizard"},
        {"follower": "fitness_master", "followed": "code_wizard"},

        {"follower": "jane_smith", "followed": "travel_junkie"},
        {"follower": "eco_warrior", "followed": "travel_junkie"},
        {"follower": "history_buff", "followed": "travel_junkie"}
    ]
}