from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request,"index.html")

def create_user(request):
    print("Got Post Info....................")
    name_from_form = request.POST['name']
    location_from_form = request.POST['locations']
    language_from_form = request.POST['languages']
    comment_from_form = request.POST['comment']

    context = {
        "name_on_template" : name_from_form,
        "location_on_template" : location_from_form,
        "language_on_template" : language_from_form,
        "comment_on_template" : comment_from_form,
    }

    # print(name_from_form)
    # print(language_from_form)
    # print(comment_from_form)
    return redirect('/show')

def results(request):
    return render(request, "show.html")