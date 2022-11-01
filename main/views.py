from urllib import request
from django.shortcuts import render,reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.views.generic import TemplateView
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
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
    
    

class AssessmentToMe(ListView):
    context_object_name = "data_for_me"
    template_name = "my_template.html"

    def get_queryset(self):
        myset = {
            "first": ComprehensiveControl.objects.filter(teacher=self.request.user),
            "second": Teaching.objects.filter(teacher=self.request.user),
            "third": PlanningLesson.objects.filter(teacher=self.request.user),
            "forth": AssessmentStudentLearning.objects.filter(teacher=self.request.user),
           
        }
        return myset

class AssessmentFromMe(ListView):
    context_object_name = "data_from_me"
    template_name = "template_fromme.html"

    def get_queryset(self):
        myset = {
            "first": ComprehensiveControl.objects.filter(observer=self.request.user),
            "second": Teaching.objects.filter(observer=self.request.user),
            "third": PlanningLesson.objects.filter(observer=self.request.user),
            "forth": AssessmentStudentLearning.objects.filter(observer=self.request.user),
           
        }
        return myset