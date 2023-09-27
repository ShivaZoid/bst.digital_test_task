from django.contrib import admin

from .models import Robot, RobotModel


@admin.register(RobotModel)
class RobotModelAdmin(admin.ModelAdmin):
    """Конфигурация отображения данных.

    Attributes:
        list_display: отображаемые поля.
    """

    list_display = (
        'name',
        'id',
    )
    empty_value_display = '-пусто-'


@admin.register(Robot)
class RobotAdmin(admin.ModelAdmin):
    """Конфигурация отображения данных.

    Attributes:
        list_display: отображаемые поля.
        search_fields: интерфейс для поиска.
        list_filter: возможность фильтрации.
    """

    list_display = (
        'id',
        'model',
        'version',
        'created',
        'serial',
    )
    search_fields = ('id', 'serial',)
    list_filter = ('model', 'version',)
    empty_value_display = '-пусто-'
