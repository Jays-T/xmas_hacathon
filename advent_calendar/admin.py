from django.contrib import admin
from .models import AdventCalendar, Day


class AdventCalendarAdmin(admin.ModelAdmin):
    list_display = (
        'advent_calendar_number',
        'user_profile',
    )


class DayAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'advent_calendar',
        'days_recipe',
    )


admin.site.register(AdventCalendar, AdventCalendarAdmin)
admin.site.register(Day, DayAdmin)
