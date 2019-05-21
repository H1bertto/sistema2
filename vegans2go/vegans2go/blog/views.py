from django.shortcuts import render


# Create your views here.
def blog(request):
    return render(request, 'blog-home.html')


def blog_details(request):
    return render(request, 'blog-details.html')
