import django
from django.shortcuts import redirect, render

def ld_view(request):
    name = "John Doe"
    age = 30
    if request.method == "POST":
        name = request.POST.get("name", name)
        age = request.POST.get("age", age)
        request.session["ld_data"] = {"name": name, "age": age}
        return redirect("ld_result")
        if not name or not age:
            name = "Nameless"
            age = 0
    context = {"name": name, "age": age}
    return render(request, "main/ld.html", context)