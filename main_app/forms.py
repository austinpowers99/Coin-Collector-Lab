from django.forms import ModelForm
from .models import Minting

class MintingForm(ModelForm):
    class Meta:
        model = Minting
        fields = ['date', 'mint_mark']