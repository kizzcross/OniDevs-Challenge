from django import forms
from .models import Music

class MusicForm(forms.ModelForm):

    class Meta:
        model = Music
        fields = '__all__'
        labels = {
            'foreign_key':'Author'
        }

    def __init__(self, *args, **kwargs):
        super(MusicForm,self).__init__(*args, **kwargs)
        self.fields['foreign_key'].empty_label = "Select"