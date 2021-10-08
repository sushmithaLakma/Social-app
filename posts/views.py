from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.http import JsonResponse
from django.core import serializers
from django.urls import reverse_lazy

# Create your views here.
def home_view(request):
	qs = Post.objects.all()
	context = {
		'hello': 'hello world',
		'qs': qs,
	}
	return render(request, 'main.html', context)

def post_view_json(request):
	qs = Post.objects.all()
	data = serializers.serialize('json', qs)
	return JsonResponse({'data':data})

class PostDeleteView(DeleteView):
	model = Post	
	template_name = 'post_delete.html'
	success_url = reverse_lazy('test_profile')
	#login_url = 'login'		

	def test_func(self):
		obj = self.get_object()
		return obj.author == self.request.user

class PostCreateView(CreateView):
	model = Post 
	template_name = 'post_new.html'
	fields = ('picture', 'body', 'author')
	#login_url = 'login'

	#def form_valid(self, form):
	#	form.instance.author = self.request.user 
	#	return super().form_valid(form)