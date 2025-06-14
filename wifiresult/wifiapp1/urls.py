from . import views
from django.urls import path, include

from django.urls import path

from .views import trigger_error
from .views import test_403_view

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.results, name='results'),
    path('admitcard/', views.admitcards, name='admitcards'),
    path('answerkey/', views.answerkey, name='answerkeys'),
    path('job/', views.jobs, name='jobs'),
    path('admission/', views.admission, name='admissions'),
    path('syllabus/', views.syllabus, name='syllabus'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('privacy/', views.privacy, name='privacy'),

    
    path("result/<slug:slug>/", views.resultpost, name="resultpost"),
    path("admitcard/<slug:slug>/", views.admitcardpost, name="admidcardpost"),
    path("answerkey/<slug:slug>/", views.answerkeypost, name="answerkeypost"),
    path("syllabus/<slug:slug>/", views.syllabuspost, name="syllabuspost"),
    path("job/<slug:slug>/", views.jobpost, name="jobpost"),
    path("admission/<slug:slug>/", views.admissionpost, name="admissionpost"),
    
    
    path('error/', trigger_error),
    path('test403/', test_403_view),


]


