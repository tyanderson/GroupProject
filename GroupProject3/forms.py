from django import forms
from GroupProject3 import models


class assetForm(forms.ModelForm):

	class Meta:
		model = models.asset
		fields = '__all__'

