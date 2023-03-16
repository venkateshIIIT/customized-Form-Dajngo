from django import forms
from .models import Candidate
from django.core.validators import RegexValidator

# Every letters to LowerCase
class Lowercase(forms.CharField):
    def to_python(self,value):
        return value.lower()

#Every letters to UpperCase
class Uppercase(forms.CharField):
    def to_python(self,value):
        return value.upper()



class CandidateForm(forms.ModelForm):
    
    #validations
    firstname=forms.CharField(
        label='First Name',
        min_length=3,
        max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',message="only letters is allowed !!")],
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
        )
    lastname=forms.CharField(
        label='First Name',
        min_length=3,
        max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',message="only letters is allowed !!")],
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}),
        required=False
        )
    job=Uppercase(
        label='Job Code',
        max_length=5,
        min_length=5,
        widget=forms.TextInput(attrs={'placeholder' :'Eg FR-13'})
    )
    email=forms.CharField(
        label='Email',
        min_length=6,
        max_length=20,
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',message='Enter the valid Email address  !!')],
        widget=forms.TextInput(attrs={'placeholder' :'Email'})
    )
    message=forms.CharField(
         widget=forms.Textarea(attrs={'rows': 4, 'cols': 40,'placeholder' :'Tell about your experience'}),
         label="cover letter ",
         required=False
        
    )
    Age=forms.CharField(
        label='Age',
        min_length=2,
        max_length=3,
        validators=[RegexValidator(r'^[0-9]*$',message='only numbers is allowed !!')],
        widget=forms.TextInput(attrs={'placeholder' :'Age'})
    )
        
    #Age=forms.IntegerField(label='Age')

    class Meta:
        model=Candidate
        fields=['firstname','lastname','email','message','Age','phone','job','Situation']
        #fields='__all__'

        #outside widget
        widgets={
            'phone':forms.TextInput(attrs={
                'style':'font-size: 13px',
                'placeholder':'Phone',
                'data-mask':'(+00)0000000000'
            })
        }

        
