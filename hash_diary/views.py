from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Pack, Trail

class PackDetail(generic.DetailView):
	model = Pack
	template_name = 'hash_diary/pack_detail.html'

class TrailDetail(generic.DetailView):
	model = Trail
	template_name = 'hash_diary/trail_detail.html'

class IndexView(generic.ListView):
	template_name = 'hash_diary/index.html'
	context_object_name = 'latest_trails_list'
	
	def get_queryset(self):
		# return all trails (for now)
		return get_list_or_404(Trail.objects.order_by('datetime'))

# Create your views here.
def index(request):
	latest_trails_list = get_list_or_404(Trail.objects.order_by('-datetime')[:5])
	context = {'latest_trails_list': latest_trails_list}
	return render(request, 'hash_diary/index.html', context)

def packs_list(request):
	packs_list = get_list_or_404(Pack.objects.order_by('name'))
	context = {'packs_list': packs_list}
	return render(request, 'hash_diary/packs_list.html', context)

def trails_list(request):
	# redirect to index for now - leaves option for different view to index, e.g. calendar index and list here
	return HttpResponseRedirect(reverse('hash_diary:index'))