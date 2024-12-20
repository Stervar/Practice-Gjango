
# # Задание №12

# #Получение информации через cookie
#     # и полная визуализация для более удобного использования

# from django.db import models
# from django.contrib.auth.models import User
# import uuid

# class CookieConsent(models.Model):
#     """
#     Модель для отслеживания согласия пользователей
#     """
#     user = models.ForeignKey(
#         User, 
#         on_delete=models.SET_NULL, 
#         null=True, 
#         blank=True
#     )
#     ip_address = models.GenericIPAddressField(null=True, blank=True)
#     accepted = models.BooleanField(default=False)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     user_agent = models.TextField(blank=True, null=True)
    
#     # Дополнительные опции согласия
#     analytics_consent = models.BooleanField(default=False)
#     marketing_consent = models.BooleanField(default=False)

#     def __str__(self):
#         return f"Consent by {self.user or 'Anonymous'} at {self.timestamp}"

#     class Meta:
#         verbose_name = 'Cookie Consent'
#         verbose_name_plural = 'Cookie Consents'
#         ordering = ['-timestamp']

# class UserActivity(models.Model):
#     """
#     Модель для отслеживания действий пользователя
#     """
#     ACTIVITY_TYPES = [
#         ('click', 'Клик'),
#         ('scroll', 'Прокрутка'),
#         ('page_view', 'Просмотр страницы'),
#         ('form_submit', 'Отправка формы'),
#         ('other', 'Другое')
#     ]

#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     user = models.ForeignKey(
#         User, 
#         on_delete=models.SET_NULL, 
#         null=True, 
#         blank=True,
#         related_name='activities'
#     )
#     action_id = models.CharField(max_length=255, unique=True)
#     action_type = models.CharField(
#         max_length=50, 
#         choices=ACTIVITY_TYPES, 
#         default='other'
#     )
    
#     # Используем TextField для совместимости
#     client_info = models.TextField(null=True, blank=True)
#     additional_data = models.TextField(null=True, blank=True)
    
#     # Временные метки
#     timestamp = models.DateTimeField(auto_now_add=True)
#     start_time = models.FloatField(null=True, blank=True)
    
#     # IP и другие метаданные
#     ip_address = models.GenericIPAddressField(null=True, blank=True)
#     user_agent = models.TextField(null=True, blank=True)
    
#     def __str__(self):
#         return f"{self.action_type} - {self.timestamp}"
    
#     class Meta:
#         verbose_name = 'User Activity'
#         verbose_name_plural = 'User Activities'
#         ordering = ['-timestamp']
#         indexes = [
#             models.Index(fields=['user', 'timestamp']),
#             models.Index(fields=['action_type', 'timestamp'])
#         ]