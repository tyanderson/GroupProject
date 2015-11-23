from django import forms
from GroupProject3 import models


class assetForm(forms.ModelForm):

	class Meta:
		model = models.asset
		fields = '__all__'


class organizationForm(forms.ModelForm):

	class Meta:
		model = models.organization
		fields = '__all__'


class locationForm(forms.ModelForm):

	class Meta:
		model = models.location
		fields = '__all__'


class manufacturerForm(forms.ModelForm):

	class Meta:
		model = models.manufacturer
		fields = '__all__'