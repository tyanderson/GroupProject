from django.forms import ModelForm
import models as md


class assetForm(ModelForm):

    class Meta:
        model = md.asset
        fields = ['location', 'organization', 'manufacturer', 'part',
                       'description', 'implemented', 'notes']
