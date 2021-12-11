from django.shortcuts import render

# Create your views here.


def advent(request):
    """ A view to return calendar page """

    return render(request, 'advent_calendar/advent.html')
