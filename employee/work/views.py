from django.shortcuts import render,redirect
from django.views.generic import View
from work.forms import EmpForm,BookForm,PersonForm,MobileForm,StudentForm
from work.models import emp,Book,Person,Mobiles,Students


# Create your views here.
class Employee(View):
 def get(self,request):
    form=EmpForm()
    return render(request,'add.html',{'form':form})
 def post(self,request):
   form=EmpForm(request.POST)
   if form.is_valid():
     print(form.cleaned_data)
     emp.objects.create(**form.cleaned_data)
     

     return render(request,'add.html',{'form':form})
   else:
     return render(request,'add.html',{'form':form})


class BookView(View):
  def get(self,request):
    form=BookForm
    return render(request,'book.html',{'form':form})
  def post(self,request):
    form=BookForm(request.POST)
    if form.is_valid():
      form.save()
      print("created")
      # print(form.cleaned_data)
      # Book.objects.create(**form.cleaned_data)
      return render(request,'book.html',{'form':form})
    else:
      return render(request,'book.html',{'form':form})
class Booklist(View):
  def get(self,request):
    qs=Book.objects.all()
    return render(request,'booklist.html',{'qs':qs})
  
class BookDetails(View):
  def get(self,request,*args,**kwargs):
    id=kwargs.get("pk")

    qs=Book.objects.get(id=id)
    return render(request,'book_details.html',{'data':qs})
  





  

class PersonView(View):
  def get(self,request):
    form=PersonForm
    return render(request,'Person.html',{'form':form})
  def post(self,request):
    form=PersonForm(request.POST)
    if form.is_valid():
      form.save()
      print("created")
      return render(request,'person.html',{'form':form})
    else:
      return render(request,'person.html',{'form':form})
class Personlist(View):
  def get(self,request):
    res=Person.objects.all()
    return render(request,'personlist.html',{'res':res})
class MobileView(View):
  def get(self,request):
    form=MobileForm
    return render(request,'mobile.html',{'form':form})
  def post(self,request):
    form=MobileForm(request.POST)
    if form.is_valid():
     form.save()
     print("created")
     return render(request,'mobile.html',{'form':form})
    else:
       return render(request,'mobile.html',{'form':form})
    
class Mobilelist(View):
  def get(self,request):
    res=Mobiles.objects.all()
    return render(request,'mobilelist.html',{'res':res})
  

class StudentView(View):
  def get(self,request):
    form=StudentForm
    return render(request,'student.html',{'form':form})
  def post(self,request):
    form=StudentForm(request.POST)
    if form.is_valid():
      print(form.cleaned_data)
      Students.objects.create(**form.cleaned_data)
      form = StudentForm()
      return render(request,'student.html',{'form':form})
    else:
      return render(request,'student.html',{'form':form})
    
class Studentlist(View):
  def get(self,request):
    res=Students.objects.all()
    return render(request,'studentlist.html',{'res':res})
class StudentDetails(View):
  def get(self,request,**kwargs):
    print(kwargs)
    id=kwargs.get('pk')
    qs=Students.objects.get(id=id)
    return render(request,'s_details.html',{'data':qs})

class Student_Delete(View):
  def get(self,request,*args,**kwargs):
    id=kwargs.get('pk')
    Students.objects.get(id=id).delete()
    return redirect('student-al')
  
  
 

