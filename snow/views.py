from django.shortcuts import render, get_object_or_404, HttpResponseRedirect


def snow(request):
    context = {}
    return render(request, "snow.html", context)