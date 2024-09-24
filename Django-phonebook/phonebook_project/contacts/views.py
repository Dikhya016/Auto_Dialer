from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from .models import Phonebook, Contact, CallRecords
from .forms import PhonebookForm, ContactForm

from contacts.mytwilio import mytwilio

def signup(request):    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)   #here i'm taking in-built signup form from django
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)  #here i'm taking in-built login form from django
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('phonebook_list')  # Redirect to phonebook list after login
    else:
        form = AuthenticationForm()
        
        form.fields['username'].widget.attrs['class'] = "username"
        form.fields['password'].widget.attrs['class'] = "password"
    return render(request, 'login.html', {'form': form})

 

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login  after logout


def phonebook_list(request):
    if request.user.is_authenticated:
        phonebooks = Phonebook.objects.filter(user=request.user)
        return render(request, 'phonebook_list.html', {'phonebooks': phonebooks,'user':request.user})
    else:
        return redirect('login')

def phonebook_detail(request, pk):
    phonebook = get_object_or_404(Phonebook, pk=pk)
    if phonebook.user == request.user:
        return render(request, 'phonebook_detail.html', {'phonebook': phonebook})
    else:
        return redirect('phonebook_list')

def phonebook_create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PhonebookForm(request.POST)
            if form.is_valid():
                phonebook = form.save(commit=False)
                phonebook.user = request.user
                phonebook.save()
                return redirect('phonebook_list')
        else:
            form = PhonebookForm()
        #phonebooks = Phonebook.objects.filter(user=request.user)
        return render(request, 'phonebook_create.html', {'form': form, 'user':request.user})
    else:
        return redirect('login')

def phonebook_edit(request, pk):
    phonebook = get_object_or_404(Phonebook, pk=pk)
    if phonebook.user == request.user:
        if request.method == 'POST':
            form = PhonebookForm(request.POST, instance=phonebook)
            if form.is_valid():
                form.save()
                return redirect('phonebook_list')
        else:
            form = PhonebookForm(instance=phonebook)
        return render(request, 'phonebook_edit.html', {'form': form})
    else:
        return redirect('phonebook_list')

def phonebook_delete(request, pk):
    phonebook = get_object_or_404(Phonebook, pk=pk)
    if phonebook.user == request.user:
        if request.method == 'POST':
            phonebook.delete()
            return redirect('phonebook_list')
        return render(request, 'phonebook_delete.html', {'phonebook': phonebook})
    else:
        return redirect('phonebook_list')

def contact_list(request):
    if request.user.is_authenticated:
        phonebooks=Phonebook.objects.filter(user=request.user)
        contacts = Contact.objects.filter(phonebooks__user=request.user).distinct()
        phid=request.GET.get('phid')
        if(phid and phid!='all'):
            phonebook = get_object_or_404(Phonebook, pk=phid)
            contacts = phonebook.contacts.all()
        return render(request, 'contact_list.html', {'contacts': contacts,'user':request.user,'phonebooks':phonebooks})
    else:
        return redirect('login')


def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if contact.phonebooks.filter(user=request.user).exists():
        return render(request, 'contact_detail.html', {'contact': contact,})
    else:
        return redirect('contact_list')


def contact_create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ContactForm(request.POST,user=request.user)
            if form.is_valid():
                contact = form.save(commit=False)
                contact.save()
                form.save_m2m()  # Save many-to-many relationships
                return redirect('contact_list')
            else:
                print('nothing '*20)
        else:
            form = ContactForm(user=request.user)
        # Filter phonebooks to show only those created by the logged-in user
        phonebooks = Phonebook.objects.filter(user=request.user)
        return render(request, 'contact_create.html', {'form': form, 'phonebooks': phonebooks,'user':request.user})
    else:
        return redirect('login')
    

def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if contact.phonebooks.filter(user=request.user).exists():
        if request.method == 'POST':
            form = ContactForm(request.POST, instance=contact,user=request.user)
            if form.is_valid():
                form.save() 
                return redirect('contact_list')
        else:
            form = ContactForm(instance=contact,user=request.user)
        return render(request, 'contact_edit.html', {'form': form,})
    else:
        return redirect('contact_list')

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if contact.phonebooks.filter(user=request.user).exists():
        if request.method == 'POST':
            contact.delete()
            return redirect('contact_list')
        return render(request, 'contact_delete.html', {'contact': contact,})
    else:
        return redirect('contact_list')

def phonebook_contacts(request):
    if request.user.is_authenticated:
        phonebooks = Phonebook.objects.filter(user=request.user)
        return render(request, 'phonebook_contacts.html', {'phonebooks': phonebooks})
    else:
        return redirect('login')

def phonebook_specific(request,pk):
    if request.user.is_authenticated:
        phonebooks = Phonebook.objects.filter(user=request.user,id=pk)
        return render(request, 'phonebook_specific.html', {'phonebooks': phonebooks})
    else:
        return redirect('login')

def dial_phonebook(request):
    if request.user.is_authenticated:
        pk=request.POST.get('phid')
        msg=request.POST.get('txt-msg')
        phonebook = get_object_or_404(Phonebook, pk=pk)
        contacts = phonebook.contacts.all()
        phs={}
        for c in contacts:
            phs[c.first_name+' '+c.last_name]=c.phone_number
        mytwilio.dial_all(request.user.id,msg,phs)
        return redirect('display_call_records')
    return redirect('login')


def display_call_records(request):
    if request.user.is_authenticated:
        records=CallRecords.objects.filter(user=request.user)
        return render(request,'call-records.html',{'records':records})
    else:
        return redirect('login')