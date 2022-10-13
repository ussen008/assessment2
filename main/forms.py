from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'lesson') 


class CustomUserChangeForm(UserChangeForm):
   
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class ControlForm(forms.ModelForm):
    class Meta:
        model = ComprehensiveControl
        fields = '__all__'


class TeachingForm(forms.ModelForm):
    class Meta:
        model = Teaching
        fields = '__all__'


class PlanningForm(forms.ModelForm):
    class Meta:
        model = PlanningLesson
        fields = '__all__'


class EducationalAchievmentsForm(forms.ModelForm):
    class Meta:
        model = AssessmentStudentLearning
        fields = '__all__'
        
