import datetime
from django import forms
from django.core.exceptions import ValidationError
class renewalbookform(forms.Form):
    renew=forms.DateField(help_text='enter the date between now and the 4 weeks')
    def clean_renew(self):
        date=self.cleaned_data['renew']

        if date<datetime.date.today():
            raise ValidationError(_("Invalid date - enter the correct date "))

        elif date>datetime.timedelta(weeks=4)+datetime.date.today():
            raise ValidationError(_("Invalid date - enter the date between now and the next 4 weeks"))

        return date


# forms validation method are run after the field name to_python and validate method
# or it can use the clean_fieldname