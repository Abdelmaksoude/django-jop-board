from django.shortcuts import render , redirect
from .models import Jop , Comment , Apply
from django.core.paginator import Paginator
from .form import ApplyForm , JopForm , CommentsForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import JopFilter
from django.contrib.auth.models import User

# Create your views here.
def jop_list(request):
    jop_list = Jop.objects.all()
    myfilter = JopFilter(request.GET , queryset=jop_list)
    jop_list = myfilter.qs
    paginator = Paginator(jop_list, 5) # Show 3 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jops': page_obj , 'myfilter':myfilter}
    return render(request , 'jop/jop_list.html' , context)

@login_required(login_url='accounts:signin')
def jop_details(request , slug):
    jop_details = Jop.objects.get(slug=slug)
    num_applications = Apply.objects.filter(jop=jop_details).count()
    users_applications = Apply.objects.filter(jop=jop_details)
    if request.method=='POST':
        form = ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.jop = jop_details
            myform.name = request.user
            myform.save()
    else:
        form = ApplyForm()
    context = {'jop': jop_details , 'form':form , 'num_applications':num_applications , 'users_applications':users_applications}
    return render(request , 'jop/jop_details.html' , context)

def jop_details_edit(request , slug):
    jop = Jop.objects.get(slug=slug)
    if request.method=='POST':
        jopform = JopForm(request.POST , instance=jop)
        if jopform.is_valid():
            jopform.save()
            myprofile = jopform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(f'/jops/{slug}')
    else:
        jopform = JopForm(instance=jop)
    return render(request , 'jop/jop_edit.html' , {'jopform':jopform})

def jop_delete(request , slug):
    jop_del = Jop.objects.get(slug=slug).delete()
    return render(request , 'jop/index.html' , {'jop_del':jop_del})

@login_required(login_url='accounts:signin')
def add_jop(request):
    if request.method == 'POST':
        form = JopForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jops:jop_list'))
    else:
        form = JopForm()
    return render(request , 'jop/add_jop.html' , {'form':form})

def home(request):
    return render(request , 'jop/index.html' , {"home": home})


def about(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentsForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user
                form.save()
                return redirect('jops:about')
        else:
            return redirect('accounts:signin')
    else:
        form = CommentsForm()
    comments = Comment.objects.all()
    context = {
        'form': form,
        'about': about,
        'comments': comments,
    }
    return render(request , 'jop/about.html' , context)

def roadmap(request):
    return render(request , 'jop/roadmap.html' , {"roadmap": roadmap})