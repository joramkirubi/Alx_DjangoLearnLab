from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from django.contrib.auth import login

# Register view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")  # redirect to some page, e.g. books list
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# Use Django built-in views for login/logout
LoginView = auth_views.LoginView.as_view(template_name="relationship_app/login.html")
LogoutView = auth_views.LogoutView.as_view(template_name="relationship_app/logout.html")
