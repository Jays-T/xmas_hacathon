from django.shortcuts import render
from django.contrib import messages


def index(request):
    """ A view to return index page """
    if not request.user.is_authenticated:
        messages.warning(request, f"Santa's elves are hangry,\
                         can you feed them in time to save Christmas?")
        messages.success(request, f"A success message!")
        messages.info(request, f"An info message!")
        messages.error(request, f"An error message!")

    return render(request, 'northpole/index.html')
