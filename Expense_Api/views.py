from django.shortcuts import render ,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from .form import ExpenseForm
from .models import ExpensePage

# Create your views here.
def indexpage(request):
  if request.method == 'GET':
    return render(request,'index.html')
  
  
def register_user(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login_page')
  else:
    form=UserCreationForm()
  return render(request,'register.html',{'form':form})
  
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_page')  
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, 'login.html')
   
def logout_user(request):
  logout(request)
  return redirect('index_page')


def maniPage(request):
  if request.method == 'GET':
    return render (request,'main.html',{'MEDIA_URL': settings.MEDIA_URL})
  
@login_required 
def expense(request):
  if request.method == 'POST':
    form = ExpenseForm(request.POST)
    if form.is_valid():
      expense = form.save(commit=False)
      expense.user = request.user
      expense.save()
      messages.success(request,'Expense added successfully')
      return redirect('expense_page')
    else:
      messages.error(request,'Failed to add expense')
        
          
  else:
      form = ExpenseForm()
  return render(request, 'expense.html', {'form': form})

@login_required
def showcase_expenses(request):
    expenses = ExpensePage.objects.filter(user=request.user)
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')

    if from_date and to_date:
        expenses = expenses.filter(date__range=[from_date, to_date])

    total_amount = sum(exp.amount for exp in expenses)

    return render(request, 'showcase.html', {
        'expenses': expenses,
        'total_amount': total_amount,
    })

@login_required
def delete_expense(request,expense_id):
  expense = get_object_or_404(ExpensePage,id=expense_id,user=request.user)
  
  expense.delete()
  
  messages.success(request,'Expense deleted successfully')
  
  return redirect('showcase_page',)