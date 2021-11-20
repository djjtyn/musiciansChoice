from django.shortcuts import render
import os
if os.path.exists("env.py"):
    import env

# Method to display the application home page
def display_home_page(request):
    print(f"{env.host}")
    return render(request, 'index.html')
