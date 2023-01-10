from django.shortcuts import render
import random
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def stopwatch(request):
    elapsed_time = 0  # replace this with the elapsed time from the database
    return render(
        request,
        "stopwatch.html",
        {"elapsed_time": elapsed_time},
    )
