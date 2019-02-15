from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView,FormView

from django.template.context_processors import csrf
from robot.form import PersonForm
from robot.models import *


class RobotTopView(TemplateView):
    template_name = "top.html"

    def get(self, request, *args, **kwargs):
        context = super(RobotTopView, self).get_context_data(**kwargs)
        return render(self.request, self.template_name, context)


class RobotInputView(FormView):
    template_name = "input.html"


    def form_valid(self, form):
        return render(self.request, 'input.html', {'form': form})

class RobotConfirmView(FormView):
    template_name = "confirm.html"


    def form_valid(self, form):
        return render(self.request, self.template_name, {'form': form})

    def form_invalid(self, form):
        return render(self.request, 'input.html', {'form': form})

class RobotCompleteView(TemplateView):
    template_name = "complete.html"

    def get(self, request, *args, **kwargs):
        context = super(RobotCompleteView, self).get_context_data(**kwargs)
        return render(self.request, self.template_name, context)