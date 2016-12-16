from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login
from dashboard.forms import UserForm

# Create your views here.
# class UserFormView(View):
#     form_class = UserForm
#     template_name = 'dashboard/registration_form.html'
#
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#
#         if form.is_valid():
#             user = form.save(commit=False)
#
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#
#             #change pass:
#             # user.set_password(password)
#
#             user.save()
#
#             user = authenticate(username=username, password=password)

        #     if user is not None:
        #         if user.is_active:
        #             login(request, user)
        #             return redirect('dashboard:dashboard')
        #
        # return render(request, self.template_name, {'form': form})