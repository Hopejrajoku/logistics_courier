from django import forms
from .models import Shipment, ShipmentUpdate

class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ['tracking_number', 'sender_name', 'receiver_name', 'receiver_address', 'receiver_phone', 'status', 'courier']

class ShipmentUpdateForm(forms.ModelForm):
    class Meta:
        model = ShipmentUpdate
        fields = ['shipment', 'update_message', 'status']
