# Задание №1


# from django.http import HttpResponse
  
# def index(request):
#     return HttpResponse("<h2>Главная</h2>")
 
# def about(request):
#     return HttpResponse("<h2>О сайте</h2>")
 
# def contact(request):
#     return HttpResponse("<h2>Контакты</h2>")








# Задание №2


# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("<h2>Главная</h2>")

# def admin_information(request):
#     # Получаем все необходимые параметры с безопасным извлечением
#     meta_info = {
#         # Длина содержимого запроса (в байтах)
#         # Если не указана, будет выведено "Не определен"
#         'CONTENT_LENGTH': request.META.get('CONTENT_LENGTH', 'Не определен'),
        
#         # MIME-тип содержимого запроса (например, application/json, multipart/form-data)
#         # Если не указан, будет выведено "Не определен"
#         'CONTENT_TYPE': request.META.get('CONTENT_TYPE', 'Не определен'),
        
#         # Типы контента, которые клиент готов принять в ответе
#         # Например, text/html, application/json
#         # Если не указан, будет выведено "Не определен"
#         'HTTP_ACCEPT': request.META.get('HTTP_ACCEPT', 'Не определен'),
        
#         # Поддерживаемые клиентом методы кодирования (compress, deflate, gzip)
#         # Если не указана, будет выведено "Не определен"
#         'HTTP_ACCEPT_ENCODING': request.META.get('HTTP_ACCEPT_ENCODING', 'Не определен'),
        
#         # Предпочтительные языки для ответа (en-US, ru-RU)
#         # Если не указан, будет выведено "Не определен"
#         'HTTP_ACCEPT_LANGUAGE': request.META.get('HTTP_ACCEPT_LANGUAGE', 'Не определен'),
        
#         # Доменное имя сервера, к которому выполняется запрос
#         # Например, localhost:8000 или example.com
#         # Если не указан, будет выведено "Не определен"
#         'HTTP_HOST': request.META.get('HTTP_HOST', 'Не определен'),
        
#         # URL страницы, с которой был выполнен переход
#         # Если прямого перехода не было, будет выведено "Нет реферера"
#         'HTTP_REFERER': request.META.get('HTTP_REFERER', 'Нет реферера'),
        
#         # Информация о браузере и операционной системе клиента
#         # Включает тип браузера, версию, операционную систему
#         # Если не определен, будет выведено "Не определен"
#         'HTTP_USER_AGENT': request.META.get('HTTP_USER_AGENT', 'Не определен'),
        
#         # Параметры, переданные в строке запроса (после знака ?)
#         # Например, ?param1=value1&param2=value2
#         # Если параметров нет, будет выведено "Пустая строка"
#         'QUERY_STRING': request.META.get('QUERY_STRING', 'Пустая строка'),
        
#         # IP-адрес клиента, выполняющего запрос
#         # Если не определен, будет выведено "Не определен"
#         'REMOTE_ADDR': request.META.get('REMOTE_ADDR', 'Не определен'),
        
#         # Имя хоста клиента (если определяется)
#         # Если не определено, будет выведено "Не определен"
#         'REMOTE_HOST': request.META.get('REMOTE_HOST', 'Не определен'),
        
#         # Имя аутентифицированного пользователя (если есть)
#         # Если пользователь не аутентифицирован, будет выведено "Не аутентифицирован"
#         'REMOTE_USER': request.META.get('REMOTE_USER', 'Не аутентифицирован'),
        
#         # HTTP-метод запроса (GET, POST, PUT, DELETE и т.д.)
#         # Если не определен, будет выведено "Не определен"
#         'REQUEST_METHOD': request.META.get('REQUEST_METHOD', 'Не определен'),
        
#         # Имя сервера (домен или localhost)
#         # Если не определено, будет выведено "Не определен"
#         'SERVER_NAME': request.META.get('SERVER_NAME', 'Не определен'),
        
#         # Порт, на котором работает сервер
#         # Например, 8000, 80, 443
#         # Если не определен, будет выведено "Не определен"
#         'SERVER_PORT': request.META.get('SERVER_PORT', 'Не определен'),
#     }
    
#     return HttpResponse(f"""
#         <!DOCTYPE html>
#         <html lang="ru">
#         <head>
#             <meta charset="UTF-8">
#             <meta name="viewport" content="width=device-width, initial-scale=1.0">
#             <title>Полная информация о запросе</title>
#             <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
#             <style>
#                 body {{
#                     font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#                     background-color: #f4f7f6;
#                     max-width: 900px;
#                     margin: 0 auto;
#                     padding: 30px;
#                     line-height: 1.6;
#                     color: #2c3e50;
#                 }}

#                 h1 {{
#                     text-align: center;
#                     color: #34495e;
#                     border-bottom: 3px solid #3498db;
#                     padding-bottom: 10px;
#                     margin-bottom: 30px;
#                 }}

#                 .info-block {{
#                     background-color: white;
#                     border-radius: 10px;
#                     padding: 20px;
#                     margin-bottom: 20px;
#                     box-shadow: 0 6px 12px rgba(0, 0, 0, 0.08);
#                     transition: all 0.3s ease;
#                     border-left: 5px solid #3498db;
#                 }}

#                 .info-block:hover {{
#                     transform: translateX(5px);
#                     box-shadow: 0 8px 16px rgba(0, 0, 0, 0.12);
#                 }}

#                 .info-block h2 {{
#                     color: #2980b9;
#                     margin-top: 0;
#                     border-bottom: 2px solid #3498db;
#                     padding-bottom: 10px;
#                     font-size: 1.2em;
#                 }}

#                 .label {{
#                     font-weight: 600;
#                     color: #2c3e50;
#                     display: inline-block;
#                     width: 200px;
#                     opacity: 0.8;
#                 }}

#                 .value {{
#                     color: #34495e;
#                     font-weight: 400;
#                 }}

#                 @media (max-width: 600px) {{
#                     body {{
#                         padding: 15px;
#                     }}
                    
#                     .label {{
#                         display: block;
#                         width: 100%;
#                         margin-bottom: 5px;
#                     }}
                    
#                     .value {{
#                         display: block;
#                     }}
#                 }}
#             </style>
#         </head>
#         <body>
#             <h1>Детали HTTP-запроса</h1>
            
#             <div class="info-block">
#                 <h2>Основная информация о запросе</h2>
#                 <div><span class="label">Метод запроса:</span> <span class="value">{meta_info['REQUEST_METHOD']}</span></div> <div><span class="label">Строка запроса:</span> <span class="value">{meta_info['QUERY_STRING']}</span></div>
#             </div>
            
#             <div class="info-block">
#                 <h2>Информация о сервере</h2>
#                 <div><span class="label">Имя сервера:</span> <span class="value">{meta_info['SERVER_NAME']}</span></div>
#                 <div><span class="label">Порт сервера:</span> <span class="value">{meta_info['SERVER_PORT']}</span></div>
#                 <div><span class="label">Хост:</span> <span class="value">{meta_info['HTTP_HOST']}</span></div>
#             </div>
            
#             <div class="info-block">
#                 <h2>Информация о клиенте</h2>
#                 <div><span class="label">IP-адрес:</span> <span class="value">{meta_info['REMOTE_ADDR']}</span></div>
#                 <div><span class="label">Имя хоста:</span> <span class="value">{meta_info['REMOTE_HOST']}</span></div>
#                 <div><span class="label">Пользователь:</span> <span class="value">{meta_info['REMOTE_USER']}</span></div>
#             </div>
            
#             <div class="info-block">
#                 <h2>Информация о браузере и содержимом</h2>
#                 <div><span class="label">Браузер:</span> <span class="value">{meta_info['HTTP_USER_AGENT']}</span></div>
#                 <div><span class="label">Реферер:</span> <span class="value">{meta_info['HTTP_REFERER']}</span></div>
#                 <div><span class="label">Длина содержимого:</span> <span class="value">{meta_info['CONTENT_LENGTH']}</span></div>
#                 <div><span class="label">Тип содержимого:</span> <span class="value">{meta_info['CONTENT_TYPE']}</span></div>
#             </div>
            
#             <div class="info-block">
#                 <h2>Параметры принимаемого ответа</h2>
#                 <div><span class="label">Принимаемые типы:</span> <span class="value">{meta_info['HTTP_ACCEPT']}</span></div>
#                 <div><span class="label">Кодировка:</span> <span class="value">{meta_info['HTTP_ACCEPT_ENCODING']}</span></div>
#                 <div><span class="label">Язык:</span> <span class="value">{meta_info['HTTP_ACCEPT_LANGUAGE']}</span></div>
#             </div>
#         </body>
#         </html>
#     """)







# Задание №3

# from django.http import HttpResponse
   
# def index(request):
#     return HttpResponse("<h2>Главная</h2>")
  
# def user(request, name, age):
#     return HttpResponse(f"<h2>Имя: {name}  Возраст:{age}</h2>")

	
# http://127.0.0.1:8000/user/Tom/38










# Задание №4

# from django.http import HttpResponse
   
# def index(request):
#     return HttpResponse("<h2>Главная</h2>")
  
# def user(request, name="Undefined", age =0):
#     return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")


# # http://127.0.0.1:8000/user/Tom/38









# Задание №5

# Определение параметров через функцию re_path




# from django.http import HttpResponse
   
# def index(request):
#     return HttpResponse("<h2>Главная</h2>")
  
# def user(request, name, age):
#     return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")



# # http://127.0.0.1:8000/user/Tom/38





# Задание №6

# Также мы можем указать для определенных параметров значения по умолчанию:


# from django.http import HttpResponse
   
# def index(request):
#     return HttpResponse("<h2>Главная</h2>")

# def user(request, name="Undefined", age =0):
#     return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")



# # http://127.0.0.1:8000/user/Tom/38




# Задание №7



# from django.http import HttpResponse
 
# def index(request):
#     return HttpResponse("Главная страница")
 
# def products(request):
#     return HttpResponse("Список товаров")
 
# def new(request):
#     return HttpResponse("Новые товары")
 
# def top(request):
#     return HttpResponse("Наиболее популярные товары")


# # /products/top





# Задание №8

# Получение параметров



# from django.http import HttpResponse
 
# def index(request):
#     return HttpResponse("Главная страница")
 
# def products(request, id):
#     return HttpResponse(f"Товар {id}")
 
# def comments(request, id):
#     return HttpResponse(f"Комментарии о товаре {id}")
 
# def questions(request, id):
#     return HttpResponse(f"Вопросы о товаре {id}")

# # /products/6/

# # /products/6/comments

# # /products/6/questions











# Переадресация и отправка статусных кодов

# Задание №9

# from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
 
# def index(request):
#     return HttpResponse("Index")
 
# def about(request):
#     return HttpResponse("About")
 
# def contact(request):
#     return HttpResponseRedirect("/about")
 
# def details(request):
#     return HttpResponsePermanentRedirect("/")







# Задание №10




# from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest
 
 
# def index(request, id):
#     people = ["Tom", "Bob", "Sam"]
#     # если пользователь найден, возвращаем его
#     if id in range(0, len(people)):
#         return HttpResponse(people[id])
#     # если нет, то возвращаем ошибку 404
#     else:
#         return HttpResponseNotFound("Not Found")
 
# def access(request, age):
#     # если возраст НЕ входит в диапазон 1-110, посылаем ошибку 400
#     if age not in range(1, 111):
#         return HttpResponseBadRequest("Некорректные данные")
#     # если возраст больше 17, то доступ разрешен
#     if(age > 17):
#         return HttpResponse("Доступ разрешен")
#     # если нет, то возвращаем ошибку 403
#     else:
#         return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")












# Отправка json

# Задание №10








# from django.http import JsonResponse
# from django.core.serializers.json import DjangoJSONEncoder
 
# def index(request):
#     bob = Person("Bob", 41)
#     return JsonResponse(bob, safe=False, encoder=PersonEncoder)
 
# class Person:
  
#     def __init__(self, name, age):
#         self.name = name    # имя человека
#         self.age = age        # возраст человека
 
# class PersonEncoder(DjangoJSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, Person):
#             return {"name": obj.name, "age": obj.age}
#             # return obj.__dict__
#         return super().default(obj)














# Задание №11


# Отправка и получение куки



# from django.shortcuts import render
# from django.http import HttpResponse
# from datetime import timedelta, datetime
# import json

# def home(request):
#     """
#     Главная страница с навигацией по функциям куки
#     """
#     html_content = '''
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>Управление куки</title>
#         <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
#     </head>
#     <body>
#         <div class="container mt-5">
#             <h1 class="mb-4">Демонстрация работы с куки</h1>
#             <div class="list-group">
#                 <a href="/set-cookies/" class="list-group-item list-group-item-action">
#                     Установка куки
#                 </a>
#                 <a href="/get-cookies/" class="list-group-item list-group-item-action">
#                     Просмотр куки
#                 </a>
#                 <a href="/delete-cookies/" class="list-group-item list-group-item-action">
#                     Удаление куки
#                 </a>
#                 <a href="/complex-cookies/" class="list-group-item list-group-item-action">
#                     Расширенные настройки куки
#                 </a>
#             </div>
#         </div>
#     </body>
#     </html>
#     '''
#     return HttpResponse(html_content)

# def set_cookie_view(request):
#     """
#     Демонстрация установки куки с различными параметрами
#     """
#     response = HttpResponse('''
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>Установка куки</title>
#         <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
#     </head>
#     <body>
#         <div class="container mt-5">
#             <h1>Установка куки</h1>
#             <div class="alert alert-success">
#                 Куки были установлены с различными параметрами
#             </div>
#             <div class="mt-3">
#                 <a href="/get-cookies/" class="btn btn-primary me-2">Просмотр куки</a>
#                 <a href="/" class="btn btn-secondary">На главную</a>
#             </div>
#         </div>
#     </body>
#     </html>
#     ''')

#     # 1. Базовая куки
#     response.set_cookie('user_id', '12345')

#     # 2. Куки с временем жизни
#     response.set_cookie(
#         key='session_token', 
#         value='abc123xyz',
#         max_age=timedelta(hours=2)  # Живет 2 часа
#     )

#     # 3. Защищенная куки
#     response.set_cookie(
#         key='auth_token',
#         value='secure_token_123',
#         secure=True,      # Только https
#         httponly=True,    # Защита от XSS
#         samesite='Lax'    # Безопасность cross-site
#     )

#     # 4. Куки сложным JSON-значением
#     user_data = {
#         'username': 'john_doe',
#         'email': 'john@example.com',
#         'roles': ['user', 'admin']
#     }
#     response.set_cookie(
#         key='user_profile',
#         value=json.dumps(user_data),
#         max_age=timedelta(days=7)
#     )

#     return response

# def get_cookie_view(request):
#     """
#     Получение и отображение всех куки
#     """
#     # Получаем все куки
#     all_cookies = request.COOKIES

#     # Подготовка данных для таблицы
#     cookie_rows = []
#     for key, value in all_cookies.items():
#         try:
#             # Пытаемся распарсить JSON
#             parsed_value = json.loads(value)
#             formatted_value = json.dumps(parsed_value, indent=2)
#         except (json.JSONDecodeError, TypeError):
#             formatted_value = value

#         cookie_rows.append({
#             'key': key,
#             'value': formatted_value
#         })

#     # Генерация HTML
#     cookie_table_html = "".join([
#         f"""
#         <tr>
#             <td>{row['key']}</td>
#             <td><pre>{row['value']}</pre></td>
#         </tr>
#         """ for row in cookie_rows
#     ])

#     response_html = f'''
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>Список куки</title>
#         <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
#         <style>
#             pre {{ 
#                 background-color: #f4f4f4;
#                 padding: 10px;
#                 border-radius: 5px;
#             }}
#         </style>
#     </head>
#     <body>
#         <div class="container mt-5">
#             <h1>Установленные куки</h1>
#             <table class="table table-bordered">
#                 <thead>
#                     <tr>
#                         <th>Ключ</th>
#                         <th>Значение</th>
#                     </tr>
#                 </thead>
#                 <tbody>
#                     {cookie_table_html}
#                 </tbody>
#             </table>
#             <div class="mt-3">
#                 <a href="/delete-cookies/" class="btn btn-danger me-2">Удалить все куки</a>
#                 <a href="/" class="btn btn-secondary">На главную</a>
#             </div>
#         </div>
#     </body>
#     </html>
#     '''
    
#     return HttpResponse(response_html)

# def delete_cookie_view(request):
#     """
#     Удаление куки
#     """
#     response = HttpResponse('''
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>Удаление куки</title>
#         <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
#     </head>
#     <body>
#         <div class="container mt-5">
#             <h1>Куки удалены</h1>
#             <div class="alert alert-warning">
#                 Все установленные куки были удалены
#             </div>
#             <div class="mt-3">
#                 <a href="/" class="btn btn-primary">На главную</a>
#             </div>
#         </div>
#     </body>
#     </html>
#     ''')
    
#     # Получаем список всех текущих куки
#     cookies = request.COOKIES

#     # Удаляем каждую куки
#     for key in cookies.keys():
#         response.delete_cookie(key)

#     return response

# def complex_cookie_view(request):
#     """
#     Расширенные настройки куки с подробной информацией
#     """
#     response = HttpResponse('''
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>Расширенные настройки куки</title>
#         <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
#     </head>
#     <body>
#         <div class="container mt-5">
#             <h1>Расширенные настройки куки</h1>
#             <div class="card">
#                 <div class="card-body">
#                     <h5 class="card-title">Установл енные куки с расширенными параметрами</h5>
#                     <p class="card-text">Куки были установлены с параметрами безопасности и ограничениями.</p>
#                     <a href="/get-cookies/" class="btn btn-primary">Просмотр куки</a>
#                     <a href="/" class="btn btn-secondary">На главную</a>
#                 </div>
#             </div>
#         </div>
#     </body>
#     </html>
#     ''')

#     # Установка защищенной куки с расширенными параметрами
#     response.set_cookie(
#         key='secure_session',
#         value='session_token_456',
#         max_age=timedelta(days=7),  # Живет 7 дней
#         secure=True,                # Только https
#         httponly=True,              # Защита от XSS
#         samesite='Strict'           # Строгие ограничения cross-site
#     )

#     return response

















# Задание №12

#Получение информации через cookie
    # и полная визуализация для более удобного использования


# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.http import require_http_methods
# import json

# def home(request):
#     # Проверяем согласие на куки
#     cookie_consent = request.COOKIES.get('cookie_consent', 'not_set')
    
#     html_content = f'''
#     <!DOCTYPE html>
#     <html lang="ru">
#     <head>
#         <meta charset="UTF-8">
#         <title>Сайт с управлением куки</title>
#         <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
#         <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" rel="stylesheet">
#         <style>
#             #cookie-consent-banner {{
#                 position: fixed;
#                 bottom: 20px;
#                 right: 20px;
#                 width: 300px;
#                 background-color: #f8f9fa;
#                 border-radius: 10px;
#                 box-shadow: 0 4px 6px rgba(0,0,0,0.1);
#                 z-index: 1000;
#                 display: {'' if cookie_consent == 'not_set' else 'none'};
#             }}
            
#             .cookie-icon {{
#                 position: fixed;
#                 bottom: 20px;
#                 right: 20px;
#                 background-color: #007bff;
#                 color: white;
#                 width: 50px;
#                 height: 50px;
#                 border-radius: 50%;
#                 display: flex;
#                 align-items: center;
#                 justify-content: center;
#                 box-shadow: 0 4px 6px rgba(0,0,0,0.1);
#                 cursor: pointer;
#                 z-index: 1000;
#                 display: {'' if cookie_consent == 'not_set' else 'none'};
#             }}

#             .content-with-cookies {{
#                 opacity: {0.5 if cookie_consent == 'not_set' else 1};
#                 pointer-events: {'' if cookie_consent == 'not_set' else 'auto'};
#                 transition: opacity 0.3s ease;
#             }}
#         </style>
#     </head>
#     <body>
#         <!-- Иконка куки -->
#         <div id="cookie-icon" class="cookie-icon">
#             <i class="fas fa-cookie-bite"></i>
#         </div>

#         <!-- Баннер согласия на куки -->
#         <div id="cookie-consent-banner" class="card">
#             <div class="card-body">
#                 <h5 class="card-title">
#                     <i class="fas fa-cookie-bite me-2"></i> 
#                     Использование куки
#                 </h5>
#                 <p class="card-text">
#                     Мы используем куки для улучшения работы сайта и персонализации контента. 
#                     Продолжая использовать сайт, вы соглашаетесь с использованием куки.
#                 </p>
#                 <div class="d-flex justify-content-between">
#                     <button id="manage-cookies" class="btn btn-secondary btn-sm">
#                         <i class="fas fa-cog me-1"></i> Настроить
#                     </button>
#                     <div>
#                         <button id="reject-cookies" class="btn btn-outline-danger btn-sm me-2">
#                             <i class="fas fa-times me-1"></i> Отклонить
#                         </button>
#                         <button id="accept-cookies" class="btn btn-primary btn-sm">
#                             <i class="fas fa-check me-1"></i> Принять
#                         </button>
#                     </div>
#                 </div>
#             </div>
#         </div>

#         <!-- Основной контент сайта -->
#         <div id="main-content" class="container mt-5 content-with-cookies">
#             <h1>Главная страница сайта</h1>
#             <div class="row">
#                 <div class="col-md-6">
#                     <div class="card">
#                         <div class="card-body">
#                             <h5 class="card-title">Раздел 1</h5>
#                             <p class="card-text">
#                                 Содержимое первого раздела. 
#                                 {'' if cookie_consent == 'not_set' else 'Контент доступен после согласия с куки.'}
#                             </p>
#                         </div>
#                     </div>
#                 </div>
#                 <div class="col-md-6">
#                     <div class="card">
#                         <div class="card-body">
#                             <h5 class="card-title">Раздел 2</h5>
#                             <p class="card-text">
#                                 Содержимое второго раздела. 
#                                 {'' if cookie_consent == 'not_set' else 'Контент доступен после согласия с куки.'}
#                             </p>
#                         </div>
#                     </div>
#                 </div>
#             </div>
#         </div>

#         <script>
#             document.addEventListener('DOMContentLoaded', function() {{
#                 const banner = document.getElementById('cookie-consent-banner');
#                 const cookieIcon = document.getElementById('cookie-icon');
#                 const mainContent = document.getElementById('main-content');
#                 const acceptBtn = document.getElementById('accept-cookies');
#                 const rejectBtn = document.getElementById('reject-cookies');
#                 const manageBtn = document.getElementById('manage-cookies');

#                 // Показ баннера по клику на иконку
#                 cookieIcon.addEventListener('click', () => {{
#                     cookieIcon.style.display = 'none';
#                     banner.style.display = 'block';
#                 }});

#                 function setCookieConsent(consent, options = {{}}) {{
#                     fetch('/set-cookie-consent/', {{
#                         method: 'POST',
#                         headers: {{
#                             'Content-Type': 'application/json',
#                             'X-CSRFToken': getCookie('csrftoken')
#                         }},
#                         body: JSON.stringify({{ 
#                             'consent': consent, 
#                             'options': options 
#                         }})
#                     }})
#                     .then(response => response.json())
#                     .then(data => {{
#                         if (data.status === 'success') {{
#                             // Скрываем баннер и иконку
#                             banner.style.display = 'none';
#                             cookieIcon.style.display = 'none';
                            
#                             // Возвращаем полную интерактивность контенту
#                             mainContent.style.opacity = '1';
#                             mainContent.style.pointerEvents = 'auto';
#                         }}
#                     }});
#                 }}

#                 // Обработчики кнопок
#                 acceptBtn.addEventListener('click', () => setCookieConsent(true, {{
#                     analytics: true,
#                     marketing: true
#                 }}));

#                 rejectBtn.addEventListener('click', () => setCookieConsent(false));

#                 manageBtn.addEventListener('click', () => {{
#                     // Здесь можно реализовать модальное окно с детальными настройками куки
#                     alert('Функция настройки куки в разработке');
#                 }});

#                 // Функция получения куки (для CSRF)
#                 function getCookie(name) {{
#                     let cookieValue = null;
#                     if (document.cookie && document.cookie !== '') {{
#                         const cookies = document.cookie.split(';');
#                         for (let i = 0; i < cookies.length; i++) {{
#                             const cookie = cookies[i].trim();
#                             if (cookie.substring(0, name.length +  1) === (name + '=')) {{
#                                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
#                                 break;
#                             }}
#                         }}
#                     }}
#                     return cookieValue;
#                 }}
#             }});
#         </script>
#     </body>
#     </html>
#     '''
#     return HttpResponse(html_content)

# @require_http_methods(["POST"])
# def set_cookie_consent(request):
#     """
#     Обработчик для установки согласия на куки
#     """
#     try:
#         data = json.loads(request.body)
#         consent = data.get('consent', False)
#         options = data.get('options', {})

#         # Создаем ответ
#         response = JsonResponse({
#             'status': 'success', 
#             'message': 'Настройки куки обновлены'
#         })

#         # Устанавливаем куки согласия
#         response.set_cookie(
#             key='cookie_consent', 
#             value='accepted' if consent else 'rejected',
#             max_age=60 * 60 * 24 * 365,  # 1 год
#             httponly=True,
#             samesite='Lax'
#         )

#         return response

#     except Exception as e:
#         return JsonResponse({
#             'status': 'error', 
#             'message': str(e)
#         }, status=400)

# def analytics_view(request):
#     """
#     Пример view с проверкой согласия на куки
#     """
#     cookie_consent = request.COOKIES.get('cookie_consent')
    
#     if cookie_consent == 'accepted':
#         # Логика для пользователей, давших согласие
#         return HttpResponse("Аналитика доступна")
#     else:
#         # Страница с предупреждением
#         return HttpResponse("Для доступа к аналитике необходимо дать согласие на куки")















# Задание №13


import json
import platform
import datetime
import uuid
import requests
import logging
import os
import hashlib
import traceback
from termcolor import colored
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

class UserActivityTracker:
    @staticmethod
    def log_action(action_id, client_info, additional_data=None):
        log_entry = {
            'timestamp': datetime.datetime.now().isoformat(),
            'action_id': action_id,
            'client_info': client_info,
            'additional_data': additional_data or {}
        }
        return log_entry

def get_client_info(request):
    # Расширенный сбор информации о клиенте
    return {
        'network': {
            'ip_address': request.META.get('REMOTE_ADDR', 'Не определен'),
            'forwarded_for': request.META.get('HTTP_X_FORWARDED_FOR', 'Отсутствует')
        },
        'client': {
            'user_agent': request.META.get('HTTP_USER_AGENT', 'Не определен'),
            'browser_info': {
                'language': request.META.get('HTTP_ACCEPT_LANGUAGE', 'Не определен'),
                'platform': platform.platform(),
                'python_version': platform.python_version()
            }
        },
        'system': {
            'hostname': platform.node(),
            'system': platform.system(),
            'release': platform.release()
        }
    }

def home(request):
    # HTML с встроенной кнопкой и JavaScript
    html_content = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Трекер активности</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f0f0f0;
            }
            .container {
                text-align: center;
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }
            #trackButton {
                background-color: #4CAF50;
                border: none;
                color: white;
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 5px;
                transition: background-color 0.3s;
            }
            #trackButton:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Трекер активности пользователя</h1>
            <button id="trackButton">Отследить действие</button>
        </div>

        <script>
            document.getElementById('trackButton').addEventListener('click', function() {
                const actionId = `action_${Date.now()}`;
                
                const trackData = {
                    action_id: actionId,
                    start_time: Date.now(),
                    additional_info: {
                        screen_width: window.screen.width,
                        screen_height: window.screen.height,
                        color_depth: window.screen.colorDepth,
                        pixel_ratio: window.devicePixelRatio,
                        timezone_offset: new Date().getTimezoneOffset()
                    }
                };

                fetch('/track-action/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(trackData)
                })
                .then(response => response.json())
                .then(data => {
                    console.log('Успешно отслежено:', data);
                    alert(`Действие ${actionId} отслежено!\nПодробности в терминале.`);
                })
                .catch(error => {
                    console.error('Ошибка:', error);
                    alert('Произошла ошибка при отслеживании действия');
                });
            });
        </script>
    </body>
    </html>
    """
    return HttpResponse(html_content)

@csrf_exempt
def track_action(request):
    """
    Расширенный обработчик для отслеживания действий пользователя с подробным логированием
    """
    if request.method != 'POST':
        return JsonResponse({
            'status': 'error',
            'message': 'Требуется POST-запрос'
        }, status=405)

    try:
        # Парсинг входящих данных
        data = json.loads(request.body)
        action_id = data.get('action_id', 'Не указано')
        start_time = data.get('start_time', 'Не указано')
        additional_info = data.get('additional_info', {})

        # Получение информации о клиенте
        client_info = get_client_info(request)

        # Создание структуры логирования
        log_info = {
            'action_id': action_id,
            'start_time': start_time,
            'client_info': client_info,
            'additional_info': additional_info
        }

        # Визуальный вывод с цветовой индикацией
        print(colored("\n🔍 ДЕТАЛЬНЫЙ АНАЛИЗ ДЕЙСТВИЯ ПОЛЬЗОВАТЕЛЯ 🔍", 'cyan', attrs=['bold']))
        
        # Базовая информация о действии
        print(colored("\n[ДЕЙСТВИЕ]", 'green'))
        print(f"➤ ID Действия: {colored(action_id, 'yellow')}")
        print(f"➤ Время начала: {colored(str(datetime.datetime.fromtimestamp(int(start_time)/1000)), 'yellow')}")
        
        # Сетевая информация
        print(colored("\n[СЕТЕВЫЕ ПАРАМЕТРЫ]", 'green'))
        network_info = client_info.get('network', {})
        print(f"➤ IP-адрес: {colored(network_info.get('ip_address', 'Н/Д'), 'yellow')}")
        print(f"➤ Переадресация: {colored(network_info.get('forwarded_for', 'Отсутствует'), 'yellow')}")
        
        # Информация о системе
        system_info = client_info.get('system', {})
        print(colored("\n[СИСТЕМНАЯ ИНФОРМАЦИЯ]", 'green'))
        print(f"➤ Хост: {colored(system_info.get('hostname', 'Н/Д'), 'yellow')}")
        print(f"➤ Операционная система: {colored(f"{system_info.get('system', 'Н/Д')} {system_info.get('release', '')}", 'yellow')}")
        
        # Информация о клиенте
        client_details = client_info.get('client', {})
        print(colored("\n[КЛИЕНТСКАЯ ИНФОРМАЦИЯ]", 'green'))
        print(f"➤ User Agent: {colored(client_details.get('user_agent', 'Н/Д'), 'yellow')}")
        
        # Дополнительная информация с клиента
        print(colored("\n[ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ]", 'green'))
        print(f"➤ Ширина экрана: {colored(str(additional_info.get('screen_width', 'Н/Д')), 'yellow')}")
        print(f"➤ Высота экрана: {colored(str(additional_info.get('screen_height', 'Н/Д')), 'yellow')}")
        print(f"➤ Глубина цвета: {colored(str(additional_info.get('color_depth', 'Н/Д')), 'yellow')}")
        print(f"➤ Пиксельное соотношение: {colored(str(additional_info.get('pixel_ratio', 'Н/Д')), 'yellow')}")
        print(f"➤ Смещение часового пояса: {colored(str(additional_info.get('timezone_offset', 'Н/Д')), 'yellow')}")

        # Логирование действия
        UserActivityTracker.log_action(
            action_id=action_id, 
            client_info=client_info, 
            additional_data={'start_time': start_time, 'additional_info': additional_info}
        )

        return JsonResponse({
            'status': 'success', 
            'message': 'Действие зафиксировано', 
            'data': log_info
        })

    except json.JSONDecodeError:
        return JsonResponse({
            'status': 'error',
            'message': 'Некорректный JSON'
        }, status=400)

    except Exception as e:
        print(colored("\n❌ ОШИБКА ПРИ ОБРАБОТКЕ ДЕЙСТВИЯ ❌", 'red', attrs=['bold']))
        print(colored(f"Тип ошибки: {type(e).__name__}", 'red'))
        print(colored(f"Описание: {str(e)}", 'red'))
        traceback.print_exc()

        return JsonResponse({
            'status': 'error', 
            'message': str(e)
        }, status=400)