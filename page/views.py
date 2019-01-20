from django.shortcuts import render
from .models import About, Project


def main(request):
	admin = About.objects.get(id=1)
	context = {
	'admin': admin,
	'projects': Project.objects.all()
	}
	return render(request, 'base.html', context)
