from django.forms import ModelForm
from .models import Question

#put the form here

class NameForm(ModelForm):
	class Meta:
		model = Question
		fields = ['question_text', 'id_text']

class IdForm(ModelForm):
	class Meta:
		model = Question
		fields = ['id_text']