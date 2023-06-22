# itasset/context_processors.py

def active_menu(request):
    current_path = request.path
    return {
        'active_menu': current_path
    }
