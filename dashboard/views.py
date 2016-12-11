from django.shortcuts import render, redirect
from dashboard.models import *
from django.views.generic import View, ListView, CreateView
from django.core.exceptions import ObjectDoesNotExist
# import datetime

class Dashboard(View):
    def get(self,request):
        return render(request, 'home.html')


class Add_word(View):
    def get(self, request):
        return render(request, 'add_words.html')
+
    def post(self, request):
        en = request.POST.get('en_word', "")
        pl = request.POST.get('pl_word', "")

        try:
            word = Word.objects.get(english=en)

            msg = "Słówko: '" + str(en) + "' jest już w bazie."
            return render(request, 'add_words.html', {'err_message': msg})

        except ObjectDoesNotExist:
            Word.objects.create(english=en, polish=pl)
            msg = "Słówko: '" + str(en) + "' zostało dodane."
            return render(request, 'add_words.html', {'suc_message': msg})

        # now = datetime.datetime.now()
        # html = "<html><body>It is now %s.</body></html>" % now
        # return HttpResponse(html)

class AddWord(CreateView):
    object = Word
    fields = ['english', 'polish']


class Dictionary(CreateView):
    template_name = 'dictionary.html'
    model = 'Dictionary'
    fields = 'Title'

class DictionaryList(ListView):
    template_name = 'dictionary.html'
    context_object_name = 'words'

    def get_queryset(self):
        return Word.objects.all()
