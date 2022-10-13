from urllib import request
from django.shortcuts import render,reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.views.generic import TemplateView
from django.views import View
from django.views.generic.edit import CreateView
from .models import *
# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class ComplexForm(CreateView):
    model = ComprehensiveControl
    template_name = 'complex_form.html'
    fields='__all__'
    success_url = reverse_lazy('home')
    

class PlanForm(CreateView):
    model = PlanningLesson
    template_name = 'plan_form.html'
    fields='__all__'
    success_url = reverse_lazy('home')

class TeachForm(CreateView):
    model = Teaching
    template_name = 'teach_form.html'
    fields='__all__'
    success_url = reverse_lazy('home')


class AchievmentForm(CreateView):
    model = AssessmentStudentLearning
    template_name = 'achievment_form.html'
    fields='__all__'
    success_url = reverse_lazy('home')

class AssessmentToMe(View):
    model = ComprehensiveControl
    context_object_name = complex
    def get_queryset(self):
        return super().get_queryset(ComprehensiveControl.objects.filter(teacher=request.user))
    