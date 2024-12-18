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