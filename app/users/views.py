from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm


class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserCreationForm
    success_url = '/register'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
