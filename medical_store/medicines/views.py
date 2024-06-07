from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, MedicineForm
from .models import Medicine
from django.urls import reverse

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_medicines')
    else:
        form = MedicineForm()
    return render(request, 'add_medicine.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from .forms import MedicineForm
from .models import Medicine

def edit_medicine(request, medicine_id=None):
    if medicine_id is None:
        # If medicine_id is not provided, create a new Medicine instance
        medicine = Medicine()
    else:
        # Retrieve the Medicine object if it exists, otherwise return a 404 error
        medicine = get_object_or_404(Medicine, pk=medicine_id)

    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('list_medicines')
    else:
        form = MedicineForm(instance=medicine)
    return render(request, 'edit_medicine.html', {'form': form, 'medicine': medicine})





def delete_medicine(request, id):
    medicine = get_object_or_404(Medicine, id=id)
    if request.method == 'POST':
        # Confirm if the medicine exists before deleting
        if medicine:
            medicine.delete()
            return redirect('list_medicines')  # Redirect to a success page
        else:
            return redirect('list_medicines')  # Redirect to a failure page or display a message
    else:
        # Render the delete confirmation page for GET requests
        return render(request, 'delete_medicine.html', {'medicine': medicine})


def list_medicines(request):
    medicines = Medicine.objects.all()
    return render(request, 'list_medicine.html', {'medicines': medicines})

def search_medicine(request):
    query = request.GET.get('query')
    if query:
        medicines = Medicine.objects.filter(name__icontains=query)
    else:
        medicines = []  # or any other default value when query is None
    return render(request, 'search_medicine.html', {'medicines': medicines, 'query': query})

