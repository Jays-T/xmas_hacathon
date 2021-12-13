from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

import datetime
import random
from random import sample

from recipes.models import Recipe
from advent_calendar.models import AdventCalendar, Day
from profiles.models import UserProfile


def advent(request):
    """ A view to return calendar page """

    template = 'advent_calendar/advent.html'
    if request.user.is_authenticated:

        profile = get_object_or_404(UserProfile, user=request.user)
        try:
            users_calendar = profile.user_advent_calendar.get()
        except ObjectDoesNotExist:
            messages.warning(request, 'Our elves found that you have no calendar \
                                       please wait while we work our magic')
            return(redirect(reverse(create_advent)))

        has_days = users_calendar.days.all()

        date_today = datetime.date.today()

        context = {
            'calendar': users_calendar,
            'days': has_days,
            'current_date': date_today
        }
        messages.warning(request, 'Hmmmm, my records show you already have a calendar!\
                         Yet the elves have not been fed? ')

        return render(request, template, context)

    return render(request, template)


@login_required
def create_advent(request):
    """ 
    A view to return calendar page
    Will create advent calendar for user
    Will create a unique Day object for each day of the first 25 days in December
    Will pick a random selection of 25 recipes and assign one to each Day object
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    success_message = 'Success! Our elves have chosen the foods they would like to try.\
                       Hurry, there is no time to waste!'
    try:
        users_calendar = profile.user_advent_calendar.get()
    except ObjectDoesNotExist:

        calendar = AdventCalendar.objects.create(user_profile=profile)
        recipes = Recipe.objects.all()
        random_selection = random.sample(list(recipes), 25)

        date = datetime.date.today()
        year = date.strftime("%Y")
        month = 12
        days = range(1, 26)

        for obj, day in zip(random_selection, days):
            date = datetime.date(int(year), int(month), int(day))
            day = Day.objects.create(advent_calendar=calendar, days_recipe=obj, date=date)  # noqa: E501
            calendar.days.add(day)

        users_calendar = get_object_or_404(AdventCalendar, advent_calendar_number=calendar)  # noqa: E501
        has_days = users_calendar.days.all()
        messages.warning(request, 'Rummaging through supplies')
        messages.info(request, 'Constructing calendar!')
        messages.info(request, 'Our elves are hard at work selecting the recipes\
                                they want to try!')
        messages.success(request, success_message)

        """
        If Day objects not created but user has Advent calendar
        Will create Day objects (one for each day in December)
        And assign one of 25 random recipes per Day object
        """
        if not has_days:
            recipes = Recipe.objects.all()
            random_selection = random.sample(list(recipes), 25)

            date = datetime.date.today()
            year = date.strftime("%Y")
            month = 12
            days = range(1, 26)

            for obj, day in zip(random_selection, days):
                date = datetime.date(int(year), int(month), int(day))
                day = Day.objects.create(advent_calendar=users_calendar, days_recipe=obj, date=date)  # noqa: E501
                users_calendar.days.add(day)
            messages.success(request, success_message)
    messages.warning(request, 'Hmmmm, my records show you already have a calendar!\
        Yet the elves have not been fed? ')

    date_today = datetime.date.today()
    template = 'advent_calendar/advent.html'
    context = {
        'calendar': users_calendar,
        'current_date': date_today
    }

    return render(request, template, context)


@login_required
def naughty(request):
    """
    Display toast messages to the user if they try to open a recipe
    not yet unlocked
    """
    # set custom message level
    naughty = 50

    messages.add_message(request, naughty, "Now now, be careful or you'll be\
                                            put on the NAUGHTY list....")

    return(redirect(reverse(advent)))


@login_required
def set_day_recipe_complete(request, day_id, calendar_id):

    Day.objects.filter(id=day_id).update(done=True)

    profile = get_object_or_404(UserProfile, user=request.user)
    try:
        users_calendar = profile.user_advent_calendar.get()
    except ObjectDoesNotExist:
        messages.error(request, "We can't find your calendar!")
        return(redirect(reverse(advent)))

    try:
        done_count = users_calendar.days.filter(done=True).count()
        messages.success(request, f'What a tasty treat that was!\
                               You have completed {done_count} recipes\
                                so far. Well done!')
    except ObjectDoesNotExist:
        messages.error(request, "You haven't done any recipes yet!")

    return(redirect(reverse(advent)))
