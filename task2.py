import random
import requests


# "Rick and Morty" API посвящён одноимённому мультсериалу.
# Основной url: https://rickandmortyapi.com/api

# print("\nДоступные ресурсы.")
# response = requests.get("https://rickandmortyapi.com/api/")
# print(response.json())

#C помощью API можно узнать различную информацию о персонажах, локациях и эпизодах мультсериала

# Добавив поля /character, /location, /episode мы получим информацию о всех первых персонажах, локациях или эпизодах соответсвенно
# При этом у каждого объекта есть информация под заголовком "info"
# Там собрана информация о количестве объектов ('count'), попадающих под запрос, количество страниц с информацией о персонажах ("pages")
# и ссылки на следующую или предыдущую страницы

# Пример для /character

# url = "https://rickandmortyapi.com/api/character"
# response = requests.get(url)
# print(response.json())

# Запросы информации о персонажах
# После /character можно написать определённые поля запроса.
# /id - id персонажа (int)
# /name - имя персонажа (str)
# /status - статус персонажа (жив, мёртв или неизвестно) (str)
# /species - биологичческий вид персонажа (str)
# /type - подвид/тип персонажа (str)
# /gender - пол персонажа (женщина/мужчина/бесполый/неизвестно)(str)
# /origin - оригинальная/родная локация персонажа (url локации)
# /location - локация, в которой персонаж был псоледний раз (url локации)
# /image - картинка, на которой изображён персонаж (url)
# /episode - список эпизодов с участием персонажа (спсиок url)
# /url - url персонажа
# /created - время добавления песронажа в базу данных
# c помощью ? можно фильтровать перслонажей по конкретным значениям name, status, species, type, gender

# Примеры запросов

# print("\nРандомный персонаж из 826 возможных.")
# url = f"https://rickandmortyapi.com/api/character/{random.randint(1,826)}"
# response = requests.get(url)
# print(response.json())

# print("\nЖенские персонажи с Земли")
# url = "https://rickandmortyapi.com/api/character/?gender=female&location=Earth,"
# response = requests.get(url)
# print(response.json())

# print("\nМёртвые Рики из разных вселенных")
# url = "https://rickandmortyapi.com/api/character/?name=rick&status=dead"
# response = requests.get(url)
# print(response.json())

# Запросы информации о локациях
# После /location можно написать определённые поля запроса.
# /id - id локации (int)
# /name - навзание локации (str)
# /type - тип локации (str)
# /dimension - вселенная, в которой присутствует данная локация(str)
# /residents - список персонажей, которые были псоледний раз в этой локации (array)
# /url - url локации (str)
# /created - время добавления локации в базу данных (str)
# c помощью ? можно фильтровать перслонажей по конкретным значениям name, type, dimension

# Примеры

# print("\nРандомная локация из 126 возможных.")
# url = f"https://rickandmortyapi.com/api/location/{random.randint(1,126)}"
# response = requests.get(url)
# print(response.json())

# print("\nИнформация о локациях типа 'Космическая станция'")
# url = "https://rickandmortyapi.com/api/location/?type=Space station"
# response = requests.get(url)
# print(response.json())

# print("\nИнформация о локациях, в которых фигурирует имя Рика")
# url = "https://rickandmortyapi.com/api/location/?name=Rick"
# response = requests.get(url)
# print(response.json())

# Запросы информации об эпизодах
# После /episode можно написать определённые поля запроса.
# /id - id эпизода (int)
# /name - навзание эпизода (str)
# /air_date - дата выхода эпизода (str)
# /episode - код эпизода (str)
# /characters - спсиок персонажей, показанных в эпизоде (array)
# /url - url эпизода (str)
# /created - время добавления эпизода в базу данных (str)
# c помощью ? можно фильтровать эпизоды по конкретным значениям name, episode

# Примеры

# print("\nРандомный эпизод из 51 возможного.")
# url = f"https://rickandmortyapi.com/api/episode/{random.randint(1,51)}"
# response = requests.get(url)
# print(response.json())

# print("\nЭпизоды из второго сезона мультсериала, в названии которых фигурирует имя 'Рик'.")
# url = f"https://rickandmortyapi.com/api/episode/?name=rick&episode=S02"
# response = requests.get(url)
# print(response.json())