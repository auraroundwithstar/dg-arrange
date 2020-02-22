from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Contribution
from .forms import ContributionForm


def contribution_list(request):
    contributions = Contribution.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'contribution/contribution_list.html', {'contributions': contributions})

def contribution_detail(request, pk):
    contribution = get_object_or_404(Contribution, pk=pk)
    return render(request, 'contribution/contribution_detail.html', {'contribution': contribution})

def contribution_new(request):
    if request.method == "POST":
        form = ContributionForm(request.POST)
        if form.is_valid():
            contribution = form.save(commit=False)
            contribution.author = request.user
            contribution.published_date = timezone.now()
            contribution.save()
            return redirect('contribution_detail', pk=contribution.pk)
    else:
        form = ContributionForm()
    return render(request, 'contribution/contribution_edit.html', {'form': form})

def contribution_edit(request, pk):
    contribution = get_object_or_404(Contribution, pk=pk)
    if request.method == "POST":
        form = ContributionForm(request.POST, instance=contribution)
        if form.is_valid():
            contribution = form.save(commit=False)
            contribution.author = request.user
            contribution.published_date = timezone.now()
            contribution.save()
            return redirect('contribution_detail', pk=contribution.pk)
    else:
        form = ContributionForm(instance=contribution)
    return render(request, 'contribution/contribution_edit.html', {'form': form})
