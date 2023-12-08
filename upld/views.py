from django.shortcuts import render,redirect
from django.conf import settings
from upld.models import Content 

# Create your views here.
def home(request):
    if request.method == 'GET':
        message = request.GET.get("message")
        print(message)

        if message is not None:
            # Create a new Content object only if there's a valid message
            Content.objects.create(content=message)

            # Redirect to the same view to avoid form resubmission
            return redirect('home')  # Update 'home' to the actual URL name of your view

    # If it's not a POST request or an invalid form submission, render the initial form
    ct = Content.objects.all().order_by('-id')
    
    return render(request, 'index.html', {'ct': ct})