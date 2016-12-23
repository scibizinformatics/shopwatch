from django.http import Http404
from django.shortcuts import render, get_object_or_404
from lazada_scrape import Scrape_Lazada

# Create your views here.
def index(request):
	context = {}
	return render(request, 'main/index.html', context)

def search(request):
	query = request.GET['q']
	results = Scrape_Lazada(query)
	context = {
		'results': results,
		'query': query
	}
	return render(request, 'main/search.html', context)
