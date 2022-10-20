from django import forms

from .models import Realstate, RealstateImage


class RealstateForm(forms.ModelForm):
    error_class= 'error-field'
    required_css_class = 'required-field'
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            new_data = {
                "placeholder": 'realstate {}'.format(str(field)),
                "class":"form-control",

            }

            self.fields[str(field)].widget.attrs.update(new_data)
        self.fields['realstate_description'].widget.attrs.update({"rows":'3'})
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
        widget=forms.ClearableFileInput(attrs={"multiple":True,})
    )
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['image'].widget.attrs.update({"class":"form-control"})
    class Meta:
        model = RealstateImage
        fields = ("image",)
    