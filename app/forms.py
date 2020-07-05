from django.forms import ModelForm
from .models import Que

class add(ModelForm):
	class Meta:
		model=Que
		fields=['que_id',' question']