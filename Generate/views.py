from django.shortcuts import render
import random
# Create your views here.
def home(request):
    context = {
        
    }
    return render(request, 'home.html', context)

def password(request):
    characters = list('abcdef')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEF'))
        
    if request.GET.get('numbers'):
        characters.extend(list('0123456789')) 
    
    if request.GET.get('special'): 
        characters.extend(list('@#$%&*'))
              
    length = int(request.GET.get('length', 12))
    
    generate_password = ''
    
    for i in range(length):
        generate_password += random.choice(characters)     
        
    context= {
        'picked_one':generate_password
    }
    return render(request, 'password.html', context)

def about(request):
    
    context = {
        
    }
    return render(request, 'about.html', context)