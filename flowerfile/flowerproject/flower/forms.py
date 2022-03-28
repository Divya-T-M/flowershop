from django import forms

from .models import Seller, Customer


class AddAddressForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['seller'].queryset = Seller.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('place'))
                self.fields['seller'].queryset = Seller.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['seller'].queryset = self.instance.district.seller_set.all()
