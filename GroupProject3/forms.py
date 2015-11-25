from django import forms
from GroupProject3 import models


class assetForm(forms.ModelForm):

	class Meta:
		model = models.asset
		fields = '__all__'
		widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
			'location': forms.Select(attrs={'class': 'form-control'}),
			'organization': forms.Select(attrs={'class': 'form-control'}),
			'manufacturer': forms.Select(attrs={'class': 'form-control'}),
			'part_number': forms.NumberInput(attrs={'class': 'form-control'}),
			'description': forms.Textarea(attrs={'class': 'form-control'}),
			'implemented': forms.DateInput(attrs={'class': 'form-control'}),
			'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }


class organizationForm(forms.ModelForm):

	class Meta:
		model = models.organization
		fields = '__all__'
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'contact_phone': forms.TextInput(attrs={'class': 'form-control'}),
		}


class locationForm(forms.ModelForm):

	class Meta:
		model = models.location
		fields = '__all__'
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'office_number': forms.NumberInput(attrs={'class': 'form-control'}),
		}


class manufacturerForm(forms.ModelForm):

	class Meta:
		model = models.manufacturer
		fields = '__all__'
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'hq_state': forms.TextInput(attrs={'class': 'form-control'}),
			'contact_phone': forms.TextInput(attrs={'class': 'form-control'}),
		}