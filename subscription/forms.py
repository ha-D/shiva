from django 			import forms
from subscription.models import Subscriber

class SubscribeForm(forms.ModelForm):
	class Meta:
		model = Subscriber