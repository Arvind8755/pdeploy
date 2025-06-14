from django.shortcuts import render
from django.http import HttpResponse
from wifiapp1.models import Result,Admitcard,Answerkey, Syllabus, Job,Admission, Contact
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def index(request):
    results=Result.objects.all()
    jobs=Job.objects.all()
    admitcards=Admitcard.objects.all()
    answerkeys=Answerkey.objects.all()
    syllabuss=Syllabus.objects.all()
    admissions=Admission.objects.all()
    return render(request, 'mainfile/index.html',{'results': results, 'jobs': jobs, 'admitcards': admitcards, 'answerkeys':answerkeys, 'syllabuss':syllabuss, 'admissions':admissions})

def results(request):
    results=Result.objects.filter()
    return render(request, 'mainfile/results.html',{'results': results})

def admitcards(request):
    admitcards=Admitcard.objects.all()
    return render(request, 'mainfile/admitcards.html', {'admitcards': admitcards})

def answerkey(request):
    answerkeys=Answerkey.objects.all()
    return render(request, 'mainfile/answerkeys.html', {'answerkeys': answerkeys})

def jobs(request):
    jobs=Job.objects.all()
    return render(request, 'mainfile/jobs.html', {'jobs': jobs})

def syllabus(request):
    syllabuss=Syllabus.objects.all()
    return render(request, 'mainfile/syllabus.html',{'syllabuss':syllabuss})

def admission(request):
    admissions=Admission.objects.all()
    return render(request, 'mainfile/admission.html',{'admissions':admissions})

def about(request):
    # Render the about.html template
    return render(request, 'mainfile/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        content = request.POST.get('content', '')

        if len(name) < 2 or len(phone) < 10 or len(email) < 3 or len(content) < 4:
            messages.error(request, "Please correct the errors below.")
        else:
            contact = Contact(name=name, phone=phone, email=email, content=content)
            contact.save()
            messages.success(request, "Your message has been sent successfully! We will get back to you soon.")

    return render(request, 'mainfile/contact.html')



def search(request):

    query=request.GET.get('q')

    admissions=None
    results=None
    jobs=None
    admitcards=None
    syllabuss=None
    answerkeys=None
    
    if query:
        admissions=Admission.objects.filter(
          Q(title__icontains=query) | Q(description__icontains=query))
        results=Result.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query))
        jobs=Job.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query))
        admitcards=Admitcard.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query))
        syllabuss=Syllabus.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query))
        answerkeys=Answerkey.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query))
      

        context={
        'query':query,
        'admissions':admissions,
        'results':results,
        'jobs':jobs,
        'admitcards':admitcards,
        'syllabuss':syllabuss,
        'answerkeys': answerkeys,
      }
        
    else:
        # Query खाली है तो empty context return करो
        context = {
            'query': '',
            'admissions': [],
            'results': [],
            'jobs': [],
            'admitcards': [],
            'syllabuss': [],
            'answerkeys': [],
        }
    return render(request, 'mainfile/search.html', context)


# from django.shortcuts import redirect

# def search(request):
#     query = request.GET.get('q')
#     if not query:
#         return redirect('index')  # या कोई default पेज

#     results = Result.objects.filter(title__icontains=query)
#     context = {
#         'results': results,
#         'query': query,
#     }
#     return render(request, 'mainfile/search.html', context)




def privacy(request):
    # Render the privacy.html template
    return render(request, 'mainfile/privacy.html')


def resultpost(request, slug):
    result = get_object_or_404(Result, slug=slug)
    return render(request, "result/resultslug.html", {"result": result,})

def admitcardpost(request, slug):
    admitcard = get_object_or_404(Admitcard, slug=slug)
    return render(request, "admitcard/admitcardslug.html", {"admitcard": admitcard,})

def answerkeypost(request, slug):
    answerkey = get_object_or_404(Answerkey, slug=slug)
    return render(request, "answerkey/answerkeyslug.html", {"answerkey": answerkey,})

def syllabuspost(request, slug):
    syllabus = get_object_or_404(Syllabus, slug=slug)
    return render(request, "syllabus/syllabusslug.html", {"syllabus": syllabus,})


def jobpost(request, slug):
    job = get_object_or_404(Job, slug=slug)
    return render(request, "job/jobslug.html", {"job": job,})

def admissionpost(request, slug):
    admission = get_object_or_404(Admission, slug=slug)
    return render(request, "admission/admissionslug.html", {"admission": admission,})












def trigger_error(request):
    division_by_zero = 1 / 0

from django.core.exceptions import PermissionDenied

from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

def test_403_view(request):
    raise PermissionDenied  # Ye 403 error trigger karega

