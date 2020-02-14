from django.shortcuts import redirect


def redirect_to_blog(request):
    return redirect('lists_url', permanent=True)
