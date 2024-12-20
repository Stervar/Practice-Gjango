"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Задание №1


# from django.urls import path, re_path
# from hello import views
 
# urlpatterns = [
#     re_path(r'^about/contact/', views.contact),
#     re_path(r'^about', views.about),
#     path('', views.index),
# ]






# Задание №2

# from django.urls import path
# from hello import views

# urlpatterns = [
#     path("", views.index),  
#     path('admin_information', views.admin_information),
# ]



# Задание №3

# from django.urls import path
# from hello import views
  
# urlpatterns = [
#     path("", views.index),
#     path("user/<name>/<int:age>", views.user),
# ]

	
# http://127.0.0.1:8000/user/Tom/38






# Задание №4

# from django.urls import path
# from hello import views
  
# urlpatterns = [
#     path("", views.index),
#     path("user", views.user),
#     path("user/<name>", views.user),
#     path("user/<name>/<int:age>", views.user),
# ]

# # http://127.0.0.1:8000/user/Tom/38










# Задание №5

# Определение параметров через функцию re_path



# from django.urls import path, re_path
# from hello import views
  
# urlpatterns = [
#     path("", views.index),
#     re_path(r"^user/(?P<name>\D+)/(?P<age>\d+)", views.user),
# ]








# Задание №6

# Также мы можем указать для определенных параметров значения по умолчанию:



# from django.urls import path, re_path
# from hello import views
  
# urlpatterns = [
#     path("", views.index),
#     re_path(r"^user/(?P<name>\D+)/(?P<age>\d+)", views.user),
#     re_path(r"^user/(?P<name>\D+)", views.user),
#     re_path(r"^user", views.user),
# ]



# # http://127.0.0.1:8000/user/Tom/38






# Задание №7



# from django.urls import path, include
# from hello import views
  
# product_patterns = [
#     path("", views.products),
#     path("new", views.new),
#     path("top", views.top),
# ]
 
# urlpatterns = [
#     path("", views.index),
#     path("products/", include(product_patterns)),
# ]


# # /products/top






# Задание №8

# Получение параметров



# from django.urls import path, include
# from hello import views
 
# product_patterns = [
#     path("", views.products),
#     path("comments", views.comments),
#     path("questions", views.questions),
# ]
 
# urlpatterns = [
#     path("", views.index),
#     path("products/<int:id>/", include(product_patterns)),
# ]



# # /products/6/

# # /products/6/comments

# # /products/6/questions










# Переадресация и отправка статусных кодов

# Задание №9



# from django.urls import path
# from hello import views
  
# urlpatterns = [
#     path("", views.index),
#     path("about/", views.about),
#     path("contact/", views.contact),
#     path("details/", views.details),
# ]






# Задание №10





# from django.urls import path
# from django.views.generic import RedirectView
# from hello import views

# urlpatterns = [
#     path("", RedirectView.as_view(url='/index/0')),  # Перенаправление на первый индекс
#     path("index/<int:id>", views.index, name="index"),
#     path("access/<int:age>", views.access, name="access"),
# ]












# Отправка json


# Задание №10





# from django.urls import path
# from hello import views
  
# urlpatterns = [
#     path("", views.index),]






# Отправка и получение куки


# Задание №11


# from django.urls import path
# from hello import views

# urlpatterns = [
#     path("", views.home),
#     path('set-cookies/', views.set_cookie_view, name='set_cookies'),
#     path('get-cookies/', views.get_cookie_view, name='get_cookies'),
#     path('delete-cookies/', views.delete_cookie_view, name='delete_cookies'),
#     path('complex-cookies/', views.complex_cookie_view, name='complex_cookies'),
# ]



# document.addEventListener('DOMContentLoaded', function() {
#     // Трекинг времени взаимодействия
#     let startTime = Date.now();
    
#     function trackAction(actionType) {
#         const trackData = {
#             action_id: `action_${Date.now()}`,
#             action_type: actionType,
#             start_time: startTime,
#             duration: Date.now() - startTime,
#             additional_info: {
#                 screen_width: window.screen.width,
#                 screen_height: window.screen.height,
#                 color_depth: window.screen.colorDepth,
#                 pixel_ratio: window.devicePixelRatio,
#                 timezone_offset: new Date().getTimezoneOffset(),
#                 referrer: document.referrer,
#                 page_url: window.location.href
#             }
#         };

#         fetch('/track-action/', {
#             method: 'POST',
#             headers: {
#                 'Content-Type': 'application/json',
#             },
#             body: JSON.stringify(trackData)
#         })
#         .then(response => response.json())
#         .then(data => console.log('Действие отслежено:', data))
#         .catch(error => console.error('Ошибка трекинга:', error));
#     }

#     // Примеры трекинга различных действий
#     document.addEventListener('click', () => trackAction('click'));
#     document.addEventListener('scroll', () => trackAction('scroll'));
# });










# Задание №12

#Получение информации через cookie
    # и полная визуализация для более удобного использования

# from django.urls import path
# from django.views.generic import TemplateView
# from django.contrib.auth.decorators import login_required, user_passes_test
# from hello import views

# def is_staff_or_superuser(user):
#     """
#     Проверка, является ли пользователь сотрудником или суперпользователем
#     """
#     return user.is_staff or user.is_superuser

# urlpatterns = [
#     # Главная страница с куки-баннером
#     path('', views.home, name='home'),
    
#     # Обработчик согласия на куки (без аутентификации)
#     path('set-cookie-consent/', 
#          views.set_cookie_consent, 
#          name='set_cookie_consent'),
    
#     # Трекинг действий пользователя (с проверкой согласия на куки)
#     path('track-action/', 
#          views.track_action, 
#          name='track_action'),
    
#     # Страница аналитики (только для авторизованных пользователей)
#     path('analytics/', 
#          login_required(views.analytics_view), 
#          name='analytics'),
    
#     # Статические страницы с политикой куки (публичный доступ)
#     path('cookie-policy/', 
#          TemplateView.as_view(template_name='cookie_policy.html'), 
#          name='cookie_policy'),
    
#     # Страница настроек куки (только для авторизованных)
#     path('cookie-settings/', 
#          login_required(TemplateView.as_view(template_name='cookie_settings.html')), 
#          name='cookie_settings'),
    
#     # REST-эндпоинт статистики (только для персонала)
#     path('api/cookie-stats/', 
#          user_passes_test(is_staff_or_superuser)(views.cookie_stats_view), 
#          name='cookie_stats'),
# ]






# Задание №13


# from django.urls import path
# from hello import views

# urlpatterns = [
#     path("", views.home, name="home"),
#     path("track-action/", views.track_action, name="track_action"), 
# ]