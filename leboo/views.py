# Create your views here.

from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template.context import RequestContext

from models import UserLents, UserBorrows, Transactions
from django.db.transaction import Transaction


class LentForm(forms.Form):
    item = forms.CharField(max_length=100)
    quantity = forms.IntegerField();
    date_given = forms.DateField(required = False);
    date_return = forms.DateField(required = False);

class NewLentForm():
    item = forms.CharField(max_length=100)
    quantity = forms.IntegerField();
    to_whom = forms.CharField(max_length = 100)
    date_given = forms.DateField(required = False);
    date_return = forms.DateField(required = False);

class Output():
    item = "";
    quantity = "";
    person = "";
    initialTime = ""
    dueDate = ""
    returned = "";

def generateOutput():
    output = []
    lent_items = UserLents.objects.filter(user_id = 100, status = False)
    
     
    
def getLentFields():
    return ["Item", "Quantity", "Date Given", "Date Return"];


def index(request):
    print "Hey satish"
    lentform = LentForm()
    lentFields = getLentFields();
    history = Transactions.objects.all()
    return render_to_response('leboo/index.html', {'history' : history},
                              context_instance=RequestContext(request))#, {'lentFields' : lentFields})

def lentitem(request):
    #return render_to_response('leboo/index.html')
    if request.method == 'POST': # If the form has been submitted...
        #lentform = NewLentForm(request.POST)
        row = Transactions(item = request.POST['lentitem'], user_id = 100, date_init = request.POST['lentdategiven'],
                           date_due = request.POST['lentdatereturn'], lent_borrowed_flag = True,
                           quantity = request.POST['lentquantity'], status = False, person = request.POST['lentperson'])
        #UserLents(item = request.POST['lentitem'], user_id = 100, date_lent = request.POST['lentdategiven'])
        row.save()
    history = Transactions.objects.all()
    return render_to_response('leboo/index.html', {'history' : history},
                              context_instance=RequestContext(request))#, {'lentFields' : lentFields})

def borroweditem(request):
    if request.method == 'POST': # If the form has been submitted...
        row = Transactions(item = request.POST['borroweditem'], user_id = 100, date_lent = request.POST['borroweddategiven'],
                           date_due = request.POST['borroweddatereturn'], lent_borrowed_flag = False,
                           quantity = request.POST['borrowedquantity'], status = False, person = request.POST['borrowedperson'])
        #UserLents(item = request.POST['lentitem'], user_id = 100, date_lent = request.POST['lentdategiven'])
        row.save()
    history = Transactions.objects.all()
    return render_to_response('leboo/index.html', {'history' : history},
                              context_instance=RequestContext(request))#, {'lentFields' : lentFields})

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

def lentform(request):
    return render_to_response('lent_form.html')

def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render_to_response('contact.html', {
        'form': form,
    })