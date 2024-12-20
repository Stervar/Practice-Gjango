# Задание №12

#Получение информации через cookie
    # и полная визуализация для более удобного использования



# from django.contrib import admin
# from .models import CookieConsent, UserActivity

# @admin.register(CookieConsent)
# class CookieConsentAdmin(admin.ModelAdmin):
#     list_display = ('user', 'ip_address', 'accepted', 'timestamp', 'analytics_consent', 'marketing_consent')
#     list_filter = ('accepted', 'timestamp', 'analytics_consent', 'marketing_consent')
#     search_fields = ('user__username', 'ip_address', 'user_agent')

# @admin.register(UserActivity)
# class UserActivityAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'action_type', 'timestamp', 'ip_address')
#     list_filter = ('action_type', 'timestamp')
#     search_fields = ('user__username', 'action_id', 'ip_address')
#     readonly_fields = ('id', 'timestamp')