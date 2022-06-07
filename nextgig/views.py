from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from nextgig.models import Post

# skills = [
#     {
#         'category':'IT',
#         'skill': 'graphics',
#         'name': 'Brian',
#         'skill_level': 'beginer'
#     },
#     {
#         'category':'casual',
#         'skill': 'mowing',
#         'name': 'sam',
#         'skill_level': 'expert'
#     },
#     {
#         'category':'Tutoring',
#         'skill': 'English',
#         'name': 'Izo',
#         'skill_level': 'Intermdiate'
#     },

# ]

def startPage(request):
    return render(request, 'nextgig/startPage.html')


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'nextgig/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'nextgig/home.html' # <app> / <model>_<viewtype>.html
    context_object_name = 'posts'

    
class PostDetailView(DetailView):
    model = Post
    template_name = 'nextgig/post_detail.html'



class PostCreateView(LoginRequiredMixin, CreateView):  # we can not use decorators on classes thats why we a using a loginrequired mixin
    model = Post
    #template_name = 'nextgig/post_form.html'
    fields = ['category', 'skill', 'skill_level']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['category', 'skill', 'skill_level']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_invalid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request, 'nextgig/about.html')
