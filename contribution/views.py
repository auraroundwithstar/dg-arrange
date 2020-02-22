from django.shortcuts import render
from django.utils import timezone

from .models import Contribution

def post_list(request):
    contributions = Contribution.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'contribution/post_list.html', {'contributions': contributions})
