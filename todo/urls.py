from django.contrib import admin
from django.urls import path, include
from .views import home, delete, cross_off, edit, uncross

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('delete/<list_id>', delete, name='delete'),
    path('cross_off/<list_id>', cross_off, name='cross_off'),
    path('uncross/<list_id>', uncross, name='uncross'),
    path('edit/<list_id>', edit, name='edit'),


]