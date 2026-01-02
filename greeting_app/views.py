from django.shortcuts import render

# Create your views here.
def birthday(request):

    context ={ "greeting": "🎉Happy❤️Birthday🎉"}

    show_effects = False

    if request.method == "POST":

        name = request.POST.get("name")
        if name:
            context["greeting"] = f"Happy ❤️ Birthday🎂 {name}!🌹🌼💐🌷🎉"
            context["show_effects"] = True

      

    return render(request, "birthday.html", context)
