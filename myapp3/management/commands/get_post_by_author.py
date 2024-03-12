from django.core.management import BaseCommand
from myapp3.models import Author, Post

class Command(BaseCommand):
    help = 'Get all posts title name'
    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='Title')


    def handle(self, *args, **kwargs):
        title = kwargs.get('title')
        post = Post.objects.filter(title=title).first()
        self.stdout.write(f'{post}')