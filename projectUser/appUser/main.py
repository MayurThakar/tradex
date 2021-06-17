from .models import User, Post
from datetime import date


class Main:
    def __init__(self, request):
        self.request = request

    def is_exist(self):
        QuerySet = User.objects.filter(
            user_name=self.request.POST['user-name']).values_list('password').first()

        if QuerySet:
            paswd = list(QuerySet)

            if self.request.POST['password'] != paswd[0]:
                return 'Incorrect password'

            else:
                return True

        return 'User does not exist'

    def create_post(self):
        post = Post()
        current_user = User.objects.get(
            user_name=self.request.POST['post-button'])
        post.post_content = self.request.POST['post-content']
        post.user = current_user
        post.save()

    def fetch(self):
        return Post.objects.all().order_by('-created_at')
