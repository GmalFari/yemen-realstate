from django import forms

from .models import Realstate, RealstateImage


class RealstateForm(forms.ModelForm):
    error_class= 'error-field'
    required_css_class = 'required-field'
    # realstate_title = forms.CharField(widget=forms.TextInput(attrs={
    # "placeholder":"Realstate name"
    # }) ,help_text="This is your help text")
    
    class Meta:
        model= Realstate 
        fields = '__all__'
        exclude = ('company',)


class ImageRealstateForm(forms.ModelForm):
   
    image = forms.ImageField(
        label="Image",
        widget=forms.ClearableFileInput(attrs={"multiple":True})
    )
    class Meta:
        model = RealstateImage
        fields = ("image",)
