from datetime import datetime
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
	ListView, DetailView, CreateView, UpdateView, DeleteView,
)
from .models import News
from .filters import NewsFilter
from .forms import NewsForm


class NewsList(ListView):
    
    model = News
    ordering: str = ['-date']
    template_name: str = "news/news.html"
    context_object_name: str  = "news"
    paginate_by: int = 10
    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
       # Получаем обычный запрос
       queryset = super().get_queryset()
       # Используем наш класс фильтрации.
       # self.request.GET содержит объект QueryDict, который мы рассматривали
       # в этом юните ранее.
       # Сохраняем нашу фильтрацию в объекте класса,
       # чтобы потом добавить в контекст и использовать в шаблоне.
       self.filterset = NewsFilter(self.request.GET, queryset)
       # Возвращаем из функции отфильтрованный список товаров
       return self.filterset.qs
    
    def get_context_data(self, **kwargs) -> list:
        context: list = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        #context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset

        return context


class PostDetail(DetailView):
    
    model = News
    template_name: str = 'news/post.html'
    context_object_name: str = 'post'


class NewsCreate(CreateView):
	
	form_class = NewsForm
	model = News
	template_name: str = 'news/news_edit.html'


class NewsUpdate(UpdateView):
	
	form_class = NewsForm
	model = News
	template_name: str = 'news/news_edit.html'
	

class NewsDelete(DeleteView):

    model = News
    template_name: str = 'news/news_delete.html'
    success_url = reverse_lazy('news_list')


def create_news(request):
	form = NewsForm()

	if request.method == 'POST':
		form = NewsForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('news/')
		

	return render(request, 'news/news_edit.html', {'form': form})
