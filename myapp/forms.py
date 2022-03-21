import imp
from django import forms
from .models import Resume


CHOICE=(
    ('M','Male'),
    ('F','Female')
)
JOB_CHOICE=(
    ('Delhi','Delhi'),
    ('Noida','Noida'),
    ('Benglur','Benglur'),
    ('Chenai','Chenai')
)
class ResumeForm(forms.ModelForm):
    job_city=forms.MultipleChoiceField(choices=JOB_CHOICE,label='Preferred Job',
    widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=Resume
        fields=['name','dob','gender','locality','city',
        'pin','state','mobile','email','job_city',
        'profile_image','my_file']
        labels={
            'name':'Full Name','dob':'Date of Birth',
            'pin':'Pin Code','mobile':'Mobile No',
            'my_file':'Document',
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name.'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker','placeholder':'Enter your dob.'}),
            'locality':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your locality.'}),
            'city':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your city.'}),
            'pin':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your pin.'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'moblie':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your number.'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your email.'}),
            'gender':forms.RadioSelect(choices=CHOICE),

        }