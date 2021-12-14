from django.shortcuts import render

# Method to display the application home page
def display_home_page(request):
    recommendations = []
    return render(request, 'index.html')
