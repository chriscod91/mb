from django.views.generic import ListView
from .models import Post


class HomePageView(ListView):
    models = Post
    template_name = "posts_list.html"
    context_object_name = "all_posts_list"