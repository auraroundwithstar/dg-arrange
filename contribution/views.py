from django.shortcuts import render

def post_list(request):
    return render(request, 'contribution/post_list.html')
