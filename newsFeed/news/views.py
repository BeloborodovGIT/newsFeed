from django.core.paginator import Paginator

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import login, logout

from django.contrib import messages

from .models import News

from .forms import NewsForm
from .forms import UserRegisterForm
from .forms import UserLoginForm


def test(request):
    objects = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    return render(request, 'news/test.html', {'page_obj': page_objects})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегестрированы')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('/login')


class HomeNews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'News Feed'
        context['pag_by'] = self.paginate_by
        return context

        return context

    def get_queryset(self):
        try:
            self.paginate_by = self.kwargs['pag_by']
        except:
            self.paginate_by = 10
        return News.objects.filter()


class ViewNews(DetailView):
    model = News
    template_name = 'news/view_news.html'
    context_object_name = 'news_item'


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    login_url = '/admin/'
    raise_exception = True
    success_url = reverse_lazy('home')

# def HomeNews(request, )

# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#     }
#     return render(request=request, template_name='news/index.html',
#                   context=context)


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request=request, template_name='news/category.html', context={'news': news,
#                                                                             'category': category})


# def view_news(request, news_id):
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request=request, template_name='news/view_news.html', context={'news_item': news_item})


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST, request.FILES)
#         if form.is_valid():
#             news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request=request, template_name='news/add_news.html', context={'form': form})
