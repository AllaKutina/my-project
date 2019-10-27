from django.shortcuts import render
from .forms import FeedbackForm
from django.views.generic.edit import FormView
from django.contrib import messages
from django.urls import reverse_lazy

class FeedbackFormView(FormView):
    template_name = 'feedback/form.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('feedback:form')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Сообщение успешно отправлено')
        return super().form_valid(form)