from django.shortcuts import render
from django.http import HttpResponse
from .models import mysolarrr
# Create your views here.


def home_page_view(request):
    return render(request,'solarr.html')

def solr(request):
    mysolr=mysolarrr()
    if request.method == "POST":
     
        # Retrieve form data
    
            total=request.POST['total']
            production=request.POST['production']
            bkk=request.POST['bkk']
            
        
            # Create a new user
       
        
            mysolr.total=total
            mysolr.production=production
            mysolr.bkk=bkk
            
      
            mysolr.save()
        
        

      

        # Handle other logic (e.g., activation email, redirect, etc.)

    # Render your registration template
       
    return render(request,'htfile.html')
    




