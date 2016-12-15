from django.shortcuts import render, redirect
from dashboard.models import Word
from dashboard.models import Dictionary as DictionaryModel
from django.views.generic import View, ListView, CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse_lazy
# import datetime

class Dashboard(ListView):
    template_name = 'dashboard/home.html'
    context_object_name = 'all_dicts'

    def get_queryset(self):
        return DictionaryModel.objects.all()


class Add_word(View):
    def get(self, request):
        return render(request, 'dashboard/add_words.html')

    def post(self, request):
        en = request.POST.get('en_word', "")
        pl = request.POST.get('pl_word', "")

        try:
            word = Word.objects.get(english=en)

            msg = "Słówko: '" + str(en) + "' jest już w bazie."
            return render(request, 'dashboard/add_words.html', {'err_message': msg})

        except ObjectDoesNotExist:
            Word.objects.create(english=en, polish=pl)
            msg = "Słówko: '" + str(en) + "' zostało dodane."
            return render(request, 'dashboard/add_words.html', {'suc_message': msg})

        # now = datetime.datetime.now()
        # html = "<html><body>It is now %s.</body></html>" % now
        # return HttpResponse(html)

class AddWord(CreateView):
    object = Word
    fields = ['english', 'polish']


class DictionaryCreate(CreateView):
    model = DictionaryModel
    fields = ['title','logo']

class DictionaryDetail(DetailView):
    template_name = 'dashboard/dictionary.html'
    model = DictionaryModel

    def get_context_data(self, **kwargs):
        context = super(DictionaryDetail, self).get_context_data(**kwargs)
        context['words'] = Word.objects.all()
        zawartosc = ""
        for c in context:
            zawartosc = zawartosc + str(c)
        context['title'] = zawartosc
        return context

class DictionaryDelete(DeleteView):
    model = DictionaryModel
    success_url = reverse_lazy('dashboard:dashboard')

class DictionaryUpdate(UpdateView):
    model = DictionaryModel
    fields = ['title']