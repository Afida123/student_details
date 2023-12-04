from django import forms
from work.models import emp
from work.models import Book
from work.models import Person,Mobiles,Students



class EmpForm(forms.Form):
    name=forms.CharField()
    place=forms.CharField()
    salary=forms.CharField()
    contact=forms.CharField()


class BookForm(forms.ModelForm):
    class Meta():
        model=Book
        fields='__all__'

class PersonForm(forms.ModelForm):
    class Meta():
        model=Person
        fields='__all__'
        
        
        # ['title','author','genre']
class MobileForm(forms.ModelForm):
    class Meta():
        model=Mobiles
        fields='__all__'
class StudentForm(forms.ModelForm):
    class Meta():
        model=Students
        fields='__all__'
