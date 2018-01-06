from django import forms
from django.core import validators
from AppTwo.models import Users

class NewUserForm(forms.ModelForm):
    # Validation on fields goes here
    class Meta:
        model = Users # the model with which we want to connect the form comes here.
        fields = '__all__'



def check_for_s(value):
    if value[0].lower() != 's':
        raise forms.ValidationError('Name should start with s ')

class FromName(forms.Form):
    #name = forms.CharField(validators=[check_for_s])
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter the email again')
    text = forms.CharField(widget=forms.Textarea)

    #botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        verify_email = all_clean_data['verify_email']

        if verify_email != email:
            raise forms.ValidationError('Make sure emails are same')

    def bk_clean_botcatcher(self):
        bc = self.cleaned_data['botcatcher']

        if len(bc) > 0:
            raise forms.ValidationError('GOTCHA BOT !')

        return bc
