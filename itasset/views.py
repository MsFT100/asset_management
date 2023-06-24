from django.shortcuts import render


def error_403(request, exception):
    return render(request, 'templates/adminlte/403.html', status=403)