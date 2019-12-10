import datetime
from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Bookinstances
class renewalbookform(forms.Form):
    renew=forms.DateField(help_text='enter the date between now and the 4 weeks')
    def clean_renew(self):
        date=self.cleaned_data['renew']

        if date<datetime.date.today():
            raise ValidationError(_("Invalid date - enter the correct date "))

        elif date>datetime.timedelta(weeks=4)+datetime.date.today():
            raise ValidationError(_("Invalid date - enter the date between now and the next 4 weeks"))

        return date




class issuessystemform(forms.ModelForm):
    # user=forms.CharField(help_text='enter the name of user to be issued',widget=forms.Select(choices))
    due_date=forms.DateField(help_text='enter the date between now and the 4 weeks')
      
    class Meta:
        model=Bookinstances
        fields=['borrower'] 
    



    def clean_renew(self):
        date=self.cleaned_data['renew']
        
        if date<datetime.date.today():
            raise ValidationError(_("Invalid date - enter the correct date "))

        elif date>datetime.timedelta(weeks=4)+datetime.date.today():
            raise ValidationError(_("Invalid date - enter the date between now and the next 4 weeks"))

        return date
    






# forms validation method are run after the field name to_python and validate method
# or it can use the clean_fieldname