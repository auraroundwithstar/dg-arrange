from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Contribution

def contribution_list(request):
    contributions = Contribution.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'contribution/contribution_list.html', {'contributions': contributions})

def contribution_detail(request, pk):
    contribution = get_object_or_404(Contribution, pk=pk)
    return render(request, 'contribution/contribution_detail.html', {'contribution': contribution})
