import uuid

from django.db import models
from recipes.models import Recipe
from profiles.models import UserProfile


class AdventCalendar(models.Model):
    """
    AdventCalendar Model will relate to Day Model via ForeignKey
    """
    advent_calendar_number = models.CharField(max_length=32, null=False, editable=False)  # noqa: E501
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                                     null=True, blank=True,
                                     related_name='user_advent_calendar')
    days = models.ManyToManyField("advent_calendar.Day", blank=True)

    def _generate_advent_calendar_number(self):
        """
        Private Method, Generate random unique order number with UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override save method
        Set order_number if none has been set then save
        """
        if not self.advent_calendar_number:
            self.advent_calendar_number = self._generate_advent_calendar_number()  # noqa: E501
        super().save(*args, **kwargs)

    def __str__(self):
        return self.advent_calendar_number


class Day(models.Model):
    """
    Day Model will take in a recipe / date / advent calendar
    A date for each day of the first 25 days of December will be assigned
    """
    date = models.DateField(null=True, blank=True)
    advent_calendar = models.ForeignKey(AdventCalendar, on_delete=models.CASCADE, related_name="advent_calendar_days")  # noqa: E501
    days_recipe = models.ForeignKey(Recipe, null=True, blank=True, on_delete=models.CASCADE)  # noqa: E501
    done = models.BooleanField(default=False)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.days_recipe.title
