from django.shortcuts import render


def error_403(request, exception):
    return render(request, 'adminlte/403.html', status=403)


def error_404(request, exception):
    return render(request, 'adminlte/404.html', status=404)
