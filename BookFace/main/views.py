from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, AddUserForm, UpdateUserForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, BlogPost, CommentBlog, Message
from random import shuffle


class Home(View):
    def get(self, request):
        return redirect("/home")


class Base(View):

    template_name = 'base.html'

    def get(self, request):
        random_users = list(User.objects.all())
        shuffle(random_users)
        return render(request, self.template_name, {"random_users": random_users[0:3]})


class AddUserView(View):
    template_name = "add_user.html"

    def get(self, request):
        return render(request, self.template_name, {"form": AddUserForm})

    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            # Profile.objects.create(user=instance)
            message = "Registration completed"
            return redirect("/")
        else:
            message = "Something went wrong, please try again"
            return render(request, self.template_name, {"form": form, "message": message})


class LoginView(View):
    template_name = "login.html"

    def get(self, request):
        return render(request, self.template_name, {"form": LoginForm})

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("/")
        else:
            message = 'Something went wrong, please try again'
            return render(request, self.template_name, {"form": LoginForm, "message": message})


@login_required
def log_out(request):
    template_name = 'base.html'
    logout(request)
    message = "You logged out"
    return render(request, template_name, {"message": message})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})


class AddPost(View):

    def get(self, request):
        return render(request, 'add_post.html')

    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.user
        if title and content:
            BlogPost.objects.create(title=title, content=content, author=author)
            return redirect("/home/")


class ProfileView(View):
    template_name = "profile_view.html"

    def get(self, request, pk):
        user_data = User.objects.get(pk=pk)
        posts_list = BlogPost.objects.filter(author_id=user_data.pk)
        return render(request, self.template_name, {"posts": posts_list, "user_data": user_data})


class PostView(View):
    template_name = "post_view.html"

    def get(self, request, pk):
        postview = BlogPost.objects.get(pk=pk)
        comments = CommentBlog.objects.all().filter(post_id=postview.id)
        return render(request, self.template_name, {"postview": postview, "comments": comments})


class MakeCommentBlog(View):
    template_name = "make_comment_blog.html"

    def get(self, request, pk):
        postview = BlogPost.objects.get(pk=pk)
        return render(request, self.template_name, {"postview": postview})

    def post(self, request, pk):
        postview = BlogPost.objects.get(pk=pk)
        content = request.POST.get("content")
        CommentBlog.objects.create(author=request.user, post=postview, content=content)

        return redirect(f"/post/{postview.id}/")


class SendMessage(View):
    template_name = "send_message.html"

    def get(self, request, pk):
        return render(request, self.template_name)

    def post(self, request, pk):
        msg_content = request.POST.get("msg_content")
        receiver = User.objects.get(pk=pk)
        sender = request.user
        Message.objects.create(sender=sender, receiver=receiver, msg_content=msg_content)
        return redirect("/")


class ReadMessages(View):
    template_name = "read_messages.html"

    def get(self, request):
        messages = Message.objects.all().filter(receiver=request.user)
        return render(request, self.template_name, {"messages": messages})
