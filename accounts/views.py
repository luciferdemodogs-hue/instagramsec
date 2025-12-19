from django.shortcuts import render
from .models import User

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Store EVERYTHING (no validation)
        User.objects.create(
            username=username,
            password=password
        )

        return render(request, 'index.html', {
            'message': 'Data stored successfully'
        })

    return render(request, 'index.html')
