from django.shortcuts import render
from django.contrib import messages


def index(request):
    """ A view to return index page """
    if not request.user.is_authenticated:
        messages.warning(request, f"Santa's elves are hangry,\
                         can you feed them in time to save Christmas?")
        return render(request, 'northpole/index.html')

    return render(request, 'profiles/profile.html')
