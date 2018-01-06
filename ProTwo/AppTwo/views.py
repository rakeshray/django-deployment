from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import Topic, AccessRecord, Webpage, Users
from AppTwo import forms
from AppTwo.forms import NewUserForm

# Create your views here.
def index(request):
    my_dic = {"insert_me":"From view.py file"}
    return render(request, 'AppTwo/index.html', context=my_dic)
    #return HttpResponse('<em> My Second App </em>')
def help(request):
    my_context = {'insert_into_help_page':'Help page template disign comes here'}
    return render(request, 'AppTwo/help.html', context=my_context)

def access_record(request):
    wp_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record':wp_list}

    return render(request, 'AppTwo/access_record.html', context=date_dict)

def access_users(request):
    return render(request, 'AppTwo/users.html')
def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request) #TODO
        else:
            print('ERROR COUNTERED !')

    return render(request, 'AppTwo/users.html', {'form':form})

    """
    user_list = Users.objects.order_by('first_name')
    user_dict = {'users':user_list}

    return render(request, 'AppTwo/users.html', context=user_dict)
    """

def form_name_view(request):
    form = forms.FromName()

    if request.method == 'POST':
        form = forms.FromName(request.POST)

        if form.is_valid():
            print('VALIDATION SUCCESS')
            print('Name'+form.cleaned_data['name'])
            print('Email'+form.cleaned_data['email'])
            print('Text'+form.cleaned_data['text'])

    return render(request, 'AppTwo/form_page.html', {'form':form})
