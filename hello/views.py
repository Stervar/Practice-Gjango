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


# from django.http import HttpResponse
   
# def index(request):
#     return HttpResponse("<h2>Главная</h2>")
  
# def user(request, name, age):
#     return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")