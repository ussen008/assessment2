from django.urls import path
from django.views.generic import TemplateView
from .views import SignUpView, HomeView, ComplexForm, PlanForm, TeachForm, AchievmentForm

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('complex_form/', ComplexForm.as_view(), name='complex_form'),
    path('plan_form/', PlanForm.as_view(), name='plan_form'),
    path('teach_form/', TeachForm.as_view(), name='teach_form'),
    path('achievment_form/', AchievmentForm.as_view(), name='achievment_form')
]
