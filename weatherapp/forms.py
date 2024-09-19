from django import forms
from .models import ImageModel, ContactModel, UserModel


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'


class BmiForm(forms.Form):
    height = forms.FloatField(label='Height in cm',
                              widget=forms.TextInput(attrs=
                                                     {'placehoder': 'Enter '
                                                                    'Height in '
                                                                    'cm'}))
    weight = forms.FloatField(label='Weight in kg',
                              widget=forms.TextInput(attrs=
                                                     {'placehoder': 'Enter '
                                                                    'Weight in '
                                                                    'kg'}))


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'
