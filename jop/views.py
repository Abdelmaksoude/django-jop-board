from django.shortcuts import render , redirect
from .models import Jop
from django.core.paginator import Paginator
from .form import ApplyForm , JopForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import JopFilter
# Create your views here.
def jop_list(request):
    jop_list = Jop.objects.all()
    myfilter = JopFilter(request.GET , queryset=jop_list)
    jop_list = myfilter.qs
    paginator = Paginator(jop_list, 3) # Show 3 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jops': page_obj , 'myfilter':myfilter}
    return render(request , 'jop/jop_list.html' , context)

def jop_details(request , slug):
    jop_details = Jop.objects.get(slug=slug)
    if request.method=='POST':
        form = ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.jop = jop_details
            myform.save()
    else:
        form = ApplyForm()
    context = {'jop': jop_details , 'form':form}
    return render(request , 'jop/jop_details.html' , context)

@login_required
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