from django.core.management.base import BaseCommand
from myapp3.models import Post, Author


class Command(BaseCommand):
    help = "Create post."
    def add_arguments(self, parser):
        parser.add.add_argument('pk', type=int, help='UserID')
        parser.add.add_argument('title', type=str, help='Title')
        parser.add.add_argument('content', type=str, help='content')
        parser.add.add_argument('is_published', type=bool, help='is_published')
    def handle(self, *args, **kwargs):
        author = Author.objects.get(pk=kwargs['pk'])
        post = Post(title=kwargs['title'], author=author, content=kwargs['content'], is_published=kwargs['is_published'])
        post.save()
        self.stdout.write(f'{post}')
