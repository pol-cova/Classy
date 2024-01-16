from django.shortcuts import render

# Create your views here.
def index(request):
    form_options = {
        "web": "Sitio web",
        "book": "Libro",
        "article": "Articulo",}
    context = {
        'forms': form_options,
    }

    return render(request, 'generators.html', context)