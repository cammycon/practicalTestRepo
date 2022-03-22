from django.shortcuts import render

# Create your views here.
def course(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'templates/GA/course.html', context=context_dict)